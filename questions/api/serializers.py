from rest_framework import serializers

from questions.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        exclude = ["updated_at"]
        
    # self ist Klasse und instance ist das Objekt das wir serializen
    # alle folgenden Methoden sind die Methoden für obige models mit SerializerMethodField
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
    
    def get_answers_count(self, instance):
        return instance.answers.count() # answers is related_name in this case
    
    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answers.filter(author=request.user).exists()
    
class AnswerSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()
    
    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]
    
    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
    
    def get_likes_count(self, instance):
        return instance.voters.count()
    
    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()
    
    def get_question_slug(self, instance):
        return instance.question.slug