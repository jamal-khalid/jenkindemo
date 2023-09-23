from django.urls import path
from myapp.views import home,Test
urlpatterns = [
    path('', home,name='home'),
    path('test',Test.as_view()),
]