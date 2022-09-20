# Generated by Django 4.1.1 on 2022-09-06 17:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(auto_created=True, editable=False, help_text='Identity of a object', primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='Activity of the object', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='when item is created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='when item is updated')),
                ('username', models.CharField(blank=True, help_text='username of a user', max_length=20, null=True)),
                ('email', models.EmailField(help_text='User personal email address', max_length=254, unique=True)),
                ('last_pass_change', models.DateTimeField(blank=True, help_text='Last password changed date', null=True)),
                ('auth_token', models.CharField(help_text='authentication code', max_length=6, null=True)),
                ('two_factor', models.BooleanField(default=False, help_text='Activates two factor auth')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
