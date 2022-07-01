# Generated by Django 4.0.4 on 2022-07-01 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_episode_episode_alter_episode_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.character'),
            preserve_default=False,
        ),
    ]
