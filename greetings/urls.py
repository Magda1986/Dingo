
from django.urls import path
from .views import greeting, personal_greeting

urlpatterns = [
   path('', greeting),
   path('<a>', personal_greeting),

]

