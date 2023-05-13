from django.urls import path
from .views import loginView, loginResultView, registerView

urlpatterns = [
    path('register/', registerView, name='register'),
    path('ok/', loginResultView, name='login_result'),
    path('', loginView, name='login'),
]
