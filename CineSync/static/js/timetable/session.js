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

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.seats_card');
    const checkboxes = form.querySelectorAll('.seat_checkbox');
    const buyButton = form.querySelector('.buy_btn');

    function checkSelected() {
        let atLeastOneSelected = false;
        checkboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                atLeastOneSelected = true;
            }
        });

        if (atLeastOneSelected) {
            buyButton.style.display = 'block';
        } else {
            buyButton.style.display = 'none';
        }
    }

    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', checkSelected);
    });

    checkSelected();
});
