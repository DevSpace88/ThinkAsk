from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from questions.api.permissions import isAuthorOrReadOnly
from questions.api.serializers import AnswerSerializer, QuestionSerializer
from questions.models import Answer, Question


class QuestionViewSet(viewsets.ModelViewSet):
    
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, isAuthorOrReadOnly]
    lookup_field = "slug"
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
class AnswerCreateAPIView(generics.CreateAPIView):
    """Allow users to answer a question instance if they haven't already."""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)

        if question.answers.filter(author=request_user).exists():
            raise ValidationError("You have already answered this Question!")

        serializer.save(author=request_user, question=question)
        
class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, isAuthorOrReadOnly]
    
    lookup_field = "uuid"
    
class AnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, isAuthorOrReadOnly]
    
    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")
    
class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.voters.add(request.user)
        answer.save()
        
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, uuid):
        answer = get_object_or_404(Answer, uuid=uuid)
        answer.voters.remove(request.user)
        answer.save()
        
        serializer_context = {"request": request}
        serializer = self.serializer_class(answer, context=serializer_context)
        
        return Response(serializer.data, status=status.HTTP_200_OK)