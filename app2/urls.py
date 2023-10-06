from django.urls import path
from .views import *
urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('employee_table/', employee_table, name='employee'),
]
