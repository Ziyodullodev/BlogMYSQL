
from django.contrib import admin
from django.urls import path
from Blog.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('maqola/<int:son>', Maqolalar.as_view(), name="maqola"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout),
    path('reg/', Register.as_view(), name="reg"),
    path('AddMaqola/', AddMaqola.as_view(), name="addmaqola"),

]
