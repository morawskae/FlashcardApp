from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Lower
from django.core.validators import RegexValidator

class TagManager(models.Manager):
    def create_tag(self, title,color, user):
        tag = self.create(user=user, color=color,title=title)
        return tag

class Tag(models.Model):
    class Meta:
        constraints=[
            models.UniqueConstraint(
                Lower("title"),"user",
                name="unique-user-title-tag"
            )
        ]
    title = models.CharField(max_length=50) #enforce it at serializer to be uppercase
    color = models.CharField(max_length=7,     validators=[
        RegexValidator(regex=r"^#[0-9A-Fa-f]{6}$", message="Color must be a valid HEX value, e.g. #FFFFFF.",)],) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags", blank=True, null=True)

    objects = TagManager()