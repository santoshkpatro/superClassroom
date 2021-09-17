import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from classrooms.models import Classroom


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_url = models.URLField(blank=True, null=True)

    classrooms = models.ManyToManyField(Classroom, through='UserClassroom')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    password_reset_required = models.BooleanField(default=False)
    v_counter = models.PositiveSmallIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    login_ip_address = models.GenericIPAddressField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def has_permission(self, classroom, role='student'):
        user_classroom = UserClassroom.objects.get(user=self, classroom=classroom)
        return user_classroom.role == role


class UserClassroom(models.Model):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher'),
        ('assistant', 'assistant'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_classrooms')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='classroom_users')
    role = models.CharField(max_length=20, default='student', choices=ROLE_CHOICES)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_classrooms'

    def __str__(self) -> str:
        return self.user.email + ' is a member of classroom ' + self.classroom.name


class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organizations')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'organizations'

    def __str__(self) -> str:
        return self.name
