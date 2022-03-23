from enum import unique

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Gender(models.TextChoices):
    PREFER_NOT_TO_SAY = "NA", "Prefer Not To Say"
    MALE = "M", "Male"
    FEMALE = "FM", "Female"
    OTHERS = "O", "Others"


class Country(models.TextChoices):
    INDIA = "IN", "India"
    JAPAN = "JP", "Japan"
    RUSSIA = "RU", "Russia"
    OTHERS = "O", "Others"


class IndianState(models.TextChoices):
    MAHARASHTRA = "MH", "Maharashtra"
    GUJARAT = "GU", "Gujarat"
    ODISHA = "OD", "Odisha"
    UTTARPRADESH = "UP", "Uttar Pradesh"


class JapaneseState(models.TextChoices):
    KYOTO = "KY", "Kyoto"
    TOKYO = "TK", "Tokyo"


class EducationType(models.TextChoices):
    BOARD10TH = "10th", "10th Board"
    BOARD12TH = "12th", "12th Board"
    GRADUATION = "College", "Graduation"
    POSTGRAD = "PG", "Post Graduation"


class CourseType(models.TextChoices):
    PARTTIME = "PT", "Part-time Course"
    FULLTIME = "FT", "Full-time Course"


class Candidate(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, help_text="Enter your first-name", null=False, blank=False)
    middle_name = models.CharField(max_length=30, help_text="Enter your middle-name (optional)", null=True, blank=True)
    last_name = models.CharField(max_length=30, help_text="Enter your last-name", null=False, blank=False)
    date_of_birth = models.DateField(null=False)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.PREFER_NOT_TO_SAY)
    email = models.EmailField(_("email address"), unique=True)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "date_of_birth", "gender"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Address(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    country = models.CharField(max_length=2, choices=Country.choices, default=Country.INDIA)
    state = models.CharField(max_length=2, choices=IndianState.choices, default=IndianState.MAHARASHTRA)
    pincode = models.IntegerField(null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    address_line = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")


class EducationDetail(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100, blank=False)
    university = models.CharField(max_length=100, blank=False)
    education_type = models.CharField(max_length=10, choices=EducationType.choices)
    course_type = models.CharField(max_length=10, choices=CourseType.choices)
    degree = models.CharField(max_length=50, blank=False)
    start_date = models.DateField(null=False)
    completion_date = models.DateField(null=False)

    class Meta:
        verbose_name_plural = _("Education Details")


class WorkExperience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    job_title = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, blank=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    details = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = _("Work Experiences")
