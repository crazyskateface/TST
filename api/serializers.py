from rest_framework import serializers
from .models import Question
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'owner')
        
        
class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'questions')