# Generated by Django 2.0.3 on 2018-05-31 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SRTP', '0003_auto_20180530_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_owner', to='SRTP.student'),
        ),
    ]