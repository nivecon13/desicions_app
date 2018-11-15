from django import forms


class DecisionForm(forms.Form):
    username_text = forms.CharField(label="Want to call yourself something (optional)?", max_length=30, required=False)
    question_text = forms.CharField(label="What are you having trouble deciding?", max_length=255)
    option_1_text = forms.CharField(label="option 1?", max_length=255)
    option_2_text = forms.CharField(label="option 2?", max_length=255)