from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet, TagViewSet, AnswerViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register("tags", TagViewSet, basename="tag"),
router.register("questions", QuestionViewSet, basename="question"),
router.register("answers", AnswerViewSet, basename="answer"),
router.register("votes", VoteViewSet, basename="vote"),


urlpatterns = [
    path("", include(router.urls)),
]
