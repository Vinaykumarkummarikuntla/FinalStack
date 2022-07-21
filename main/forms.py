from django.forms import ModelForm
from .models import Answer,Question,CustomUser

class AnswerForm(ModelForm):
    "creating a answer form for posting a answer for question"
    class Meta:
        model=Answer
        fields=('detail',)

class QuestionForm(ModelForm):
    "creating a Question form for posting question"
    class Meta:
        "assign the Question database and it fields"
        model=Question
        fields=('title','detail','tags')

class ProfileForm(ModelForm):
    "creating ProfileForm for User Profile"
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio','location')
