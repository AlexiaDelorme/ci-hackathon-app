# Generated by Django 3.1.1 on 2020-10-18 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0007_auto_20201017_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackprojectscorecategory',
            name='highest_score',
            field=models.IntegerField(default=10),
        ),
    ]