document.addEventListener('DOMContentLoaded', function () {
    const dateRangeSelector = document.getElementById('dateRangeSelector');
    const prevBtn = document.getElementById('prevRange');
    const nextBtn = document.getElementById('nextRange');
    let currentStartDate = getStartDate('week');

    // Utilitaries functions.
    function getStartDate(rangeType) {
        const now = new Date();
        const start = new Date(now);

        if (rangeType === 'week') {
            const day = now.getDay();
            const diff = now.getDate() - day + (day === 0 ? -6 : 1);
            start.setDate(diff);
        } else if (rangeType === 'month') {
            start.setDate(1);
        } else if (rangeType === 'year') {
            start.setMonth(0);
            start.setDate(1);
        }

        start.setHours(0, 0, 0, 0);
        return start;
    }

    function getRangeDates(startDate, rangeType) {
        const start = new Date(startDate);
        const end = new Date(startDate);

        if (rangeType === 'week') {
            end.setDate(end.getDate() + 6);
        } else if (rangeType === 'month') {
            end.setMonth(end.getMonth() + 1);
            end.setDate(0);
        } else if (rangeType === 'year') {
            end.setFullYear(end.getFullYear() + 1);
            end.setDate(0);
        }

        return { start, end };
    }

    function generateDateRange(startDate, endDate) {
        const dates = [];
        const current = new Date(startDate);
        while (current <= endDate) {
            const yyyy = current.getFullYear();
            const mm = String(current.getMonth() + 1).padStart(2, '0');
            const dd = String(current.getDate()).padStart(2, '0');
            dates.push(`${yyyy}-${mm}-${dd}`);
            current.setDate(current.getDate() + 1);
        }
        return dates;
    }

    function completeDataWithMissingDates(data, startDate, endDate) {
        const rangeDates = generateDateRange(startDate, endDate);
        const dataMap = new Map(data.map(d => [d.date, d.weight_kg]));

        const labels = [];
        const values = [];

        rangeDates.forEach(date => {
            labels.push(date);
            values.push(dataMap.has(date) ? parseFloat(dataMap.get(date)) : null);
        });

        return { labels, values };
    }

    function getWeekNumber(date) {
        const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
        const dayNum = d.getUTCDay() || 7;
        d.setUTCDate(d.getUTCDate() + 4 - dayNum);
        const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
        return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
    }

    function updateDateLabel(rangeType, startDate) {
        const label = document.getElementById("dateLabel");
        const year = startDate.getFullYear();
        const month = startDate.toLocaleString('en-US', { month: 'long' });
        const week = getWeekNumber(startDate);

        if (rangeType === 'week') {
            label.textContent = `Week ${week} – ${month} ${year}`;
        } else if (rangeType === 'month') {
            label.textContent = `${month} ${year}`;
        } else if (rangeType === 'year') {
            label.textContent = `${year}`;
        }
    }

    function shiftDate(rangeType, direction) {
        const delta = direction === 'prev' ? -1 : 1;
        if (rangeType === 'week') {
            currentStartDate.setDate(currentStartDate.getDate() + 7 * delta);
        } else if (rangeType === 'month') {
            currentStartDate.setMonth(currentStartDate.getMonth() + delta);
        } else if (rangeType === 'year') {
            currentStartDate.setFullYear(currentStartDate.getFullYear() + delta);
        }
    }

    function loadData() {
        const rangeType = dateRangeSelector.value;

        let timeUnit, timeFormat;
        if (rangeType === 'week') {
            timeUnit = 'day';
            timeFormat = 'yyyy-MM-dd';
        } else if (rangeType === 'month') {
            timeUnit = 'day';
            timeFormat = 'yyyy-MM-dd';
        } else if (rangeType === 'year') {
            timeUnit = 'month';
            timeFormat = 'MMM yyyy';
        }

        chart.options.scales.x.time.unit = timeUnit;
        chart.options.scales.x.time.displayFormats = {
            day: timeFormat,
            month: timeFormat,
            year: timeFormat
        };

        const { start, end } = getRangeDates(currentStartDate, rangeType);

        fetch("/api/v1/body-metrics/")
            .then(res => res.json())
            .then(data => {
                const filtered = data.filter(d => {
                    const date = new Date(d.date);
                    return date >= start && date <= end;
                });

                const completed = completeDataWithMissingDates(filtered, start, end);
                chart.data.labels = completed.labels;
                chart.data.datasets[0].data = completed.values;

                chart.update();
                updateDateLabel(rangeType, currentStartDate);
            })
            .catch(err => {
                console.error("Erreur chargement données:", err);
            });
    }

    // Initialize chart.
    const ctx = document.getElementById('myChart').getContext('2d');
    let chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Weight',
                data: [],
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
                tension: 0.1,
                spanGaps: true
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day',
                        tooltipFormat: 'yyyy-MM-dd',
                        displayFormats: {
                            day: 'yyyy-MM-dd'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Weight (kg)'
                    }
                }
            }
        }
    });

    // Events.
    dateRangeSelector.addEventListener('change', () => {
        currentStartDate = getStartDate(dateRangeSelector.value);
        loadData();
    });

    prevBtn.addEventListener('click', () => {
        shiftDate(dateRangeSelector.value, 'prev');
        loadData();
    });

    nextBtn.addEventListener('click', () => {
        shiftDate(dateRangeSelector.value, 'next');
        loadData();
    });

    const dateInput = document.querySelector('input[name="date"]');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.value = today;
    }

    const form = document.getElementById('form');
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const formData = new FormData(form);
        const payload = {
            date: formData.get("date"),
            weight_kg: parseFloat(formData.get("weight"))
        };

        fetch("/api/v1/body-metrics/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        })
            .then(async res => {
                if (!res.ok) {
                    const errorData = await res.json();
                    if (res.status === 422) {
                        const messages = errorData.detail.map(err => {
                            const loc = err.loc.join(".");
                            return `Champ "${loc}" : ${err.msg}`;
                        }).join("\n");
                        throw new Error(messages);
                    } else {
                        throw new Error("Erreur serveur inconnue.");
                    }
                }
                return res.json();
            })
            .then(() => {
                form.reset();
                M.Modal.getInstance(document.getElementById('add_modal')).close();
                loadData();
            })
            .catch(err => {
                console.error("Erreur:", err);
                alert(err.message);
            });
    });

    loadData();
});
