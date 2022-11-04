from django.urls import include, path
from rest_framework import routers
from polls.polls_api import views as api_views
from . import views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /polls/polls_api/
    path('polls_api/', include(router.urls)),
    # ex: /polls/polls_api/api-auth
    path('polls_api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

