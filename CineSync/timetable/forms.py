from django import forms

from timetable.models import Auditorium, Row


class SeatSelectionForm(forms.Form):
    def __init__(self, auditorium: Auditorium):
        super().__init__()
        self.selected_seats = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=[(str(seat.id), seat.row_number) for seat in auditorium.rows.all()],
        )
