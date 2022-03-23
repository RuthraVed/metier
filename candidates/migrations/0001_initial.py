# Generated by Django 3.2 on 2022-03-23 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(help_text='Enter your first-name', max_length=30)),
                ('middle_name', models.CharField(blank=True, help_text='Enter your middle-name (optional)', max_length=30, null=True)),
                ('last_name', models.CharField(help_text='Enter your last-name', max_length=30)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('NA', 'Prefer Not To Say'), ('M', 'Male'), ('FM', 'Female'), ('O', 'Others')], default='NA', max_length=2)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('details', models.TextField(blank=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EducationDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('education_type', models.CharField(choices=[('10th', '10th Board'), ('12th', '12th Board'), ('College', 'Graduation'), ('PG', 'Post Graduation')], max_length=10)),
                ('course_type', models.CharField(choices=[('PT', 'Part-time Course'), ('FT', 'Full-time Course')], max_length=10)),
                ('degree', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('completion_date', models.DateField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('IN', 'India'), ('JP', 'Japan'), ('RU', 'Russia'), ('O', 'Others')], default='IN', max_length=2)),
                ('state', models.CharField(choices=[('MH', 'Maharashtra'), ('GU', 'Gujarat'), ('OD', 'Odisha'), ('UP', 'Uttar Pradesh')], default='MH', max_length=2)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('address_line', models.TextField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
