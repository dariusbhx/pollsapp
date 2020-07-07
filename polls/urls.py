from django.urls import path

from . import views
app_name = 'polls' #Adds namespace specific to polls app so other apps pages cant get confused with the polls apps pages.


urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
]
    
