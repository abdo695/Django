from django.urls import path

from .import views


urlpatterns= [
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
   
    path('home',views.home,name='home'),
    path('tasks',views.tasks,name='tasks'),
    path('courses',views.courses,name='courses'),
    path('account',views.account,name='account'),


    path('abdo',views.abdo,name='abdo'),
    path('index',views.index,name='index'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('books',views.books,name='books'),
    path('update/<int:id>',views.update,name='update'),

    

]
