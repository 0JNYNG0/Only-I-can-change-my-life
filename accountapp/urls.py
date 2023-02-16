from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [
    # 함수 방식은 그냥 함수 명을 넣으면 된다 - hello_world
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    # 클래스 방식은 클래스 명.as_view() 로 값을 넣어야 된다 - AccountCreateView.as_view()
    path('create/', AccountCreateView.as_view(), name='create'),
    # 몇 번 유저의 detail 정보를 보는지 pk 라는 int 형 정보 공간을 만들어 줌
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]