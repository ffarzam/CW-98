from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class MyAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, email=None, password=None, **kwargs):

        if email is None:
            try:
                user = CustomUser.objects.get(username=username)
                if user.check_password(password):
                    return user
            except CustomUser.DoesNotExist:
                try:
                    user = CustomUser.objects.get(email=username)
                    if user.check_password(password):
                        return user
                except CustomUser.DoesNotExist:
                    return


    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return
