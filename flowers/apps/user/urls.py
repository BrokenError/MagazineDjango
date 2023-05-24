from django.urls import path

from apps.user.views import ChangePassword, RegisterUser, logout_user, delete_account, \
    user_personal, user_security, verify_code

urlpatterns = [
    path('', ChangePassword.as_view(), name='user'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    path('delete/', delete_account, name='delete-account'),
    path('security/', user_security, name='security'),
    path('personal/', user_personal, name='personal'),
    path('verify/', verify_code, name='verify'),
]
