# Generated by Django 4.0.2 on 2022-05-03 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0012_recipe_helloworld'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='helloworld',
        ),
    ]
