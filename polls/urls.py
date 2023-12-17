from django.urls import path
from . import views

from .views import ServeyLoginView, ServeyLogoutView

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('accounts/login/', ServeyLoginView.as_view(), name='login'),
    path('accounts/logout/', ServeyLogoutView.as_view(), name='logout'),
    path('delete/', views.DeleteUserView.as_view(), name='profile_delete'),
    path('change/', views.ChangeUserInfoView.as_view(), name='profile_change'),
]
