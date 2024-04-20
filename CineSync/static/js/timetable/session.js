    document.querySelectorAll('.seat_checkbox').forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        var filmSession = checkbox.closest('.film_session');
        if (checkbox.checked) {
            filmSession.classList.add('selected'); // Добавляем класс, если чекбокс выбран
        } else {
            filmSession.classList.remove('selected'); // Удаляем класс, если чекбокс не выбран
        }
    });
});