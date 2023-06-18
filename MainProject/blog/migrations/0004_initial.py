# Generated by Django 4.2.1 on 2023-06-09 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0003_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('theme', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=35)),
            ],
        ),
    ]