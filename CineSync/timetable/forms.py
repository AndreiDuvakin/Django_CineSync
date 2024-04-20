import pprint
from json import loads

from django import forms

from timetable.models import Auditorium, Row


class SeatSelectionForm(forms.Form):
    selected_seats = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
    )

    def __init__(self, *args, auditorium: Auditorium, **kwargs):
        super().__init__(*args, **kwargs)
        choices = []
        for i, row in enumerate(auditorium.rows.all(), start=1):
            for seat in range(1, row.column_count + 1):
                choices.append((f'[{seat}, {str(i)}]', f'[{seat}, {str(i)}]'))
        self.fields['selected_seats'].choices = choices

        for field in self.visible_fields():
            field.field.widget.attrs.update({"class": "seat_checkbox"})

    def clean_selected_seats(self):
        selected_seats = self.cleaned_data['selected_seats']
        if list[str] is type(self.cleaned_data):
            selected_seats = [loads(field) for field in selected_seats]
        return selected_seats
