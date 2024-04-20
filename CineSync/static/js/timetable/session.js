    document.querySelectorAll('.seat_checkbox').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        var filmSession = checkbox.closest('.film_session');
        if (checkbox.checked) {
            filmSession.classList.add('selected');
        } else {
            filmSession.classList.remove('selected');
        }
    });
});