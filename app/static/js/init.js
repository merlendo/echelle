document.addEventListener('DOMContentLoaded', function () {
    const sidenavElems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenavElems, { edge: 'right' });

    const modalElems = document.querySelectorAll('.modal');
    M.Modal.init(modalElems, { inDuration: 0, outDuration: 0 });

    const selectElems = document.querySelectorAll('select');
    M.FormSelect.init(selectElems);
});
