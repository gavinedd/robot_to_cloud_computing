from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.password_validation import validate_password
from django_cryptography.fields import encrypt

import uuid


class FrontendUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff=False, is_superuser=False, **other_fields):
        if 'id' not in other_fields:
            other_fields['id'] = uuid.uuid4()

        if not email:
            raise ValueError('Email address must be specified')

        if not password:
            raise ValueError('Password must be specified')

        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_superuser=is_superuser,
            **other_fields
        )
        validate_password(password)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **other_fields):
        return self._create_user(email, password, False, False, **other_fields)

    def create_superuser(self, email, password, **other_fields):
        return self._create_user(email, password, True, True, **other_fields)


class FrontendUser(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, editable=False,
                          default=uuid.uuid4, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40, null=True, blank=True)

    date_of_birth = models.DateField()

    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'

    objects = FrontendUserManager()

    def get_full_name(self):
        return ("%s %s" % (self.first_name, self.last_name))

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name() + ', ' + self.email

    def asdict(self):
        return {'id': self.id, 'is_superuser': self.is_superuser, 'is_staff': self.is_staff, 'is_active':
                self.is_active, 'email': self.email, 'first_name': self.first_name, 'last_name': self.last_name,
                'date_of_birth': self.date_of_birth, 'last_login': self.last_login, 'date_joined':self.date_joined,
                'date_modified': self.date_modified}


class Robot(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,
                          default=uuid.uuid4, unique=True)

    name = models.CharField(max_length=255)
    auth_string = encrypt(models.CharField(max_length=255))
    
    
class CsvFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,
                          default=uuid.uuid4, unique=True)

    robot = models.ForeignKey(Robot, editable=False, on_delete=models.CASCADE)
    
    received_timestamp = models.DateTimeField(auto_now_add=True)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()

    file_path = models.TextField()

    
class RobotImageFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,
                          default=uuid.uuid4, unique=True)

    received_timestamp = models.DateTimeField(auto_now_add=True)
    image_timestamp = models.DateTimeField()

    image_type = models.CharField(max_length=255)

    csv_file = models.ForeignKey(CsvFile, editable=False, on_delete=models.CASCADE)

    file_path = models.TextField()
