from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),

    path('user/<str:pk>/', views.user_page, name='profile'),
    path('event/<str:pk>/', views.event, name='event'),
    path('registration-confirmation/<str:pk>/', views.registration_confirmation, name='registration-confirmation'),

    path('account/', views.acount_page, name='account'),
    path('project-submission/<str:pk>/', views.submission_form, name='project-submission'),
    path('update-submission/<str:pk>/', views.update_submission, name='update-submission'),

]