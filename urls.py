from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from quotium.views import QuoteListView

urlpatterns = [
    path('', include('quotium.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
]
