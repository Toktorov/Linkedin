# Generated by Django 4.1.5 on 2023-02-02 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_usercontact'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usercontact',
            unique_together={('from_user', 'to_user')},
        ),
    ]
