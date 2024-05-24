from django.urls import path
from news import views
from django.contrib.auth import views as auth_views
urlpatterns = [
  path('',views.index,name='index'),
  path('scrape/<str:name>',views.scrape, name="scrape"),
  path('news_list/', views.news_list, name="home"),
  path('register/',views.register,name='register'),
  path('login/',views.login_page,name='login'),
  path('logout/',views.logout_page,name='logout'),
  path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
  path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name="password_reset_done"),
  path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name="password_reset_confirm"),
  path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),
]