from django.urls import path
from .api import views
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('register', views.UserRegister.as_view(), name=None),
    path('login', views.StaticLogin.as_view(), name=None),
    path('refresh/token', refresh_jwt_token),
]

# curl --location --request POST '127.0.0.1:8000/api/v1/users/refresh/token' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFhYWFhYWFhYXFhYWF6enEiLCJpYXQiOjE2MzkwMzQ5NjgsImV4cCI6MTYzOTAzNTI2OCwidXNlcl9pZCI6OSwib3JpZ19pYXQiOjE2MzkwMzQ5Njh9.u0zjGX6ZnxA_UlPgXERyOA01MagJrlmDurMBlEXk1RU"
# }'
