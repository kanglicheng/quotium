from django.urls import path
from . import views


urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quote_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('success/', views.SubmissionSuccessView.as_view(), name='success'),
    path('post/new/', views.CreateSubmissionView.as_view(), name='post_new'),

]
