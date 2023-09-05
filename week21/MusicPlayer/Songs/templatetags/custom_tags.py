from django import template
from Interactions.models import Like

register = template.Library()


def is_liked(value, arg):
    qs = Like.objects.filter(song=value, user=arg)
    if qs.exists():
        return True
    else:
        return False


register.filter('is_liked', is_liked)
