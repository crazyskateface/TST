from rest_framework import serializers
from .models import Question
from django.contrib.auth.models import User

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'owner')
        
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-member', read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'questions')
        
        
        
        
"""
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
"""