# Generated by Django 5.1.6 on 2025-02-27 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the book title', max_length=255)),
                ('author', models.CharField(help_text='Enter the book author', max_length=255)),
                ('genre', models.CharField(help_text='Enter the book genre', max_length=100)),
                ('isbn', models.CharField(help_text='Enter the 13-character ISBN number', max_length=13, unique=True)),
                ('available_copies', models.PositiveIntegerField(default=1, help_text='Number of copies available')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(help_text="Enter the librarian's employee ID", max_length=20, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('member', 'Member')], default='member', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowRecore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, help_text='Expected retuen date', null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='library.member')),
            ],
        ),
    ]
