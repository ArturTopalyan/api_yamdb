from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, username, email, role="user", **extra_fields):
        if username is None:
            raise ValueError("Поле username обязательное!")
        if email is None:
            raise ValueError("Поле email обязательное!")
        return super().create_user(username, email, role, **extra_fields)
        if username == "me":
            raise ValueError("нельзя создать с таким именем!")
        return super().create_user(
            username, email=email, password=password, **extra_fields)

    def create_superuser(self, username, email, password, role="admin", **extra_fields):
        if password is None:
            raise TypeError("Поле password обязательное!")
        return super().create_superuser(username, email, password, role, **extra_fields)

class CustomUser(AbstractUser):

    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

    ROLE = ((ADMIN, "admin"), (MODERATOR, "moderator"), (USER, "user"))

    bio = models.TextField(blank=True)
    role = models.CharField(max_length=200, choices=ROLE, default='user')
    username = models.CharField(max_length=150, unique=True, db_index=True)
    object = CustomUserManager()

    REQUIRED_FIELDS = ('email', 'password')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    @property
    def is_user(self):
        return self.role == self.ROLE[2][0]

    @property
    def is_admin(self):
        return self.role == self.ROLE[0][0]

    @property
    def is_moderator(self):
        return self.role == self.ROLE[1][0]
