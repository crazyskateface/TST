from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Question
from .serializers import QuestionSerializer, UserSerializer
from .forms import QuestionForm
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


def home(request):
    tmpl_vars = {'form':QuestionForm()}
    return render(request, 'index.html', tmpl_vars)

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'questions':reverse('question-collection', request=request, format=format)
    })

#########################
### class based views ###
#########################

class QuestionCollection(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
class QuestionMember(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    



# @api_view(['GET'])
# def question_collection(request):
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data)
#     
# @api_view(['GET'])
# def question_element(request, pk):
#     try:
#         question = Question.objects.get(pk=pk)
#     except Question.DoesNotExist:
#         return HttpResponse(status=404)
#     
#     if request.method == 'GET':
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data)