from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="ไม่ระบุชื่อ")
    rank = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs["created"]:
        profile = UserProfile.objects.create(user=kwargs["instance"])


post_save.connect(create_profile, sender=User)
