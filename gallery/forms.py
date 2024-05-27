from django import forms

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = [
        (1, 'Парусники'),
        (2, 'Современные'),
        (3, 'Показать всё'),
    ]
    art_category = forms.ChoiceField(choices=CATEGORY_CHOICES, label='Choise')