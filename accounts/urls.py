from django.urls import path, re_path as url 
from django.contrib.auth import views as auth_views


from .views import(
    Login,
    signup,
)
urlpatterns = [
    url('^log/out/', auth_views.LogoutView.as_view(), name='logout'),
    url('^sign/up/', signup.as_view(), name='register'),
    url('^login/', Login.as_view(), name='login'),
    
]
