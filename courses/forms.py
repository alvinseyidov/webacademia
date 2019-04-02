
from django import forms
from.models import Course

class LevelsForm(forms.ModelForm):
    COURSE_LEVELS = ('beginner', 'intermediate', 'advanced')
    level = forms.ChoiceField(required=True, choices=COURSE_LEVELS)

    class MEta:
        model = Course
