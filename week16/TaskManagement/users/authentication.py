from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class MyAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, email=None, password=None, **kwargs):

        if username is None:
            try:
                user = CustomUser.objects.get(email=email)
                return user
            except CustomUser.DoesNotExist:
                return

        elif email is None:
            try:
                user = CustomUser.objects.get(username=username)
                return user
            except CustomUser.DoesNotExist:
                return


    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return
