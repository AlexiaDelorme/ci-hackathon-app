from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from allauth.account.views import PasswordChangeView
from . import views

urlpatterns = [
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    # Override django allauth default success url
    path('password/change/',
         login_required(
             PasswordChangeView.as_view(
                 success_url=reverse_lazy('profile')
             )
         ),
         name='account_change_password'
         ),
]
