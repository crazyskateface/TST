from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M:%S')