from django.urls import path
from warriors_app import views


urlpatterns = [
    path("warriors/", views.WarriorAPIView.as_view()),
    path("profession/create", views.ProfessionCreateView.as_view()),
    path("skills/", views.SkillView.as_view()),
    path("warriors/list/", views.WarriorListAPIView.as_view()),
    path("profession/generic_create/", views.ProfessionCreateAPIView.as_view()),
    path("warriors/profession/", views.WarriorWithProfessionView.as_view()),
    path("warriors/skill/", views.WarriorWithSkillView.as_view()),
    path("warriors/<int:pk>/", views.WarriorDetailView.as_view()),
    path("warriors/delete/<int:pk>/", views.WarriorDeleteView.as_view()),
    path("warriors/update/<int:pk>/", views.WarriorUpdateView.as_view()),
]
