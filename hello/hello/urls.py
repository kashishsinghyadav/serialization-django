 
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/<int:pk>',views.stu_det),
    path('info/',views.stu_list),

]
