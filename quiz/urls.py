from django.urls import path, include
from rest_framework import routers
from .views import QuestionViewSet, TagViewSet, AnswerViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register("tag", TagViewSet, basename="tag"),
router.register("question", QuestionViewSet, basename="question"),
router.register("answer", AnswerViewSet, basename="answer"),
router.register("vote", VoteViewSet, basename="vote"),


urlpatterns = [
    path("", include(router.urls)),
]
