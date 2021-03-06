# Generated by Django 2.0.3 on 2018-06-04 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheduling', '0002_lesson_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(null=True)),
                ('time', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='time',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='week',
        ),
        migrations.AddField(
            model_name='time',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_scheduling.lesson'),
        ),
    ]
