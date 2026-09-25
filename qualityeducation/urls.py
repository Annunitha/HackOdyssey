from django.urls import path

from .views import qualityeducation_add, home_view, qualityeducation_detail, qualityeducation_edit, qualityeducation_delete, login_view, logout_view, signup_view

urlpatterns = [
    path('', home_view, name='home'),

    path('qualityeducation/<int:pk>/', qualityeducation_detail, name='qualityeducation_detail'),
    path("qualityeducation/create/", qualityeducation_add, name="qualityeducation_add"),
    path('qualityeducation/<int:pk>/edit/', qualityeducation_edit, name='qualityeducation_edit'),
    path('qualityeducation/<int:pk>/delete/', qualityeducation_delete, name='qualityeducation_delete'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]
