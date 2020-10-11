from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import uuid
from django.utils import timezone

# Create your models here.
class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(is_deleted=False)

class SignUpModel(models.Model):
    DEFAULT_EXPIRY_WINDOW = 5 * 60
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    photo = models.ImageField(max_length=None)
    expiry_window = models.IntegerField(default=DEFAULT_EXPIRY_WINDOW)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = UserManager()

    def set_password(self, password):
        self.password = make_password(password=password, hasher='default')

    def verify_password(self, password):
        return check_password(password=password, encoded=self.password, preferred='default')

    def is_authenticated(self):
        return True


def generate_id():
    """
    Generates unique id used as token in authentication
    """
    return uuid.uuid4().hex + str(timezone.now().microsecond)


class AuthTokens(models.Model):
    """
    Represents token object used for authorization in protected APIs to be used by third parties.
    """

    id = models.CharField(max_length=128, default=generate_id, primary_key=True)
    user = models.ForeignKey(to=SignUpModel, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

