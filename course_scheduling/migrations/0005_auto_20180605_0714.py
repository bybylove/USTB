# Generated by Django 2.0.3 on 2018-06-05 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheduling', '0004_auto_20180604_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_scheduling.classroom'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_scheduling.teacher'),
        ),
    ]