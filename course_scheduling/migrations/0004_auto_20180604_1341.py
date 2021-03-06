# Generated by Django 2.0.3 on 2018-06-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheduling', '0003_auto_20180604_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_scheduling.classroom'),
        ),
        migrations.AddField(
            model_name='time',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_scheduling.teacher'),
        ),
    ]
