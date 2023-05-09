from django.urls import path
from .views import loginView, loginResultView

urlpatterns = [
    path('', loginView, name='login'),
    path('ok/', loginResultView, name='login_result'),
]
