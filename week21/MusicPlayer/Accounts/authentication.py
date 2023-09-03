from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import Base


class AuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Base.objects.get(Q(username=username) | Q(email=username))
        except Base.DoesNotExist:
            return None

        return user if user.check_password(password) else None

    def get_user(self, user_id):
        try:
            return Base.objects.get(pk=user_id)
        except Base.DoesNotExist:
            return
