from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CandidateChangeForm, CandidateCreationForm
from .models import Address, Candidate, EducationDetail, WorkExperience


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class EducationDetailInline(admin.StackedInline):
    model = EducationDetail
    extra = 0


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 0


class CandidateAdmin(UserAdmin):
    add_form = CandidateCreationForm
    form = CandidateChangeForm
    model = Candidate
    # To display all fields
    list_display = [
        "id",
        "avatar",
        "first_name",
        "middle_name",
        "last_name",
        "date_of_birth",
        "gender",
        "email",
        "date_joined",
        "is_staff",
        "is_active",
    ]
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "avatar",
                    "first_name",
                    "middle_name",
                    "last_name",
                    "date_of_birth",
                    "gender",
                    "email",
                )
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "avatar",
                    "first_name",
                    "middle_name",
                    "last_name",
                    "date_of_birth",
                    "gender",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    inlines = [
        AddressInline,
        EducationDetailInline,
        WorkExperienceInline,
    ]
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Address)
admin.site.register(EducationDetail)
admin.site.register(WorkExperience)
