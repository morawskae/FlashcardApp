from ..models import Tag
from django.db.models import Q
def user_tags(user):
    if user.is_staff:
        return Tag.objects.all()
    return Tag.objects.filter(user=user)

def accessible_tags(user):
    if user.is_staff:
        return Tag.objects.all()
    return Tag.objects.filter(Q(user=user)|Q(user=None))