# Generated by Django 4.0.3 on 2022-05-09 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
        ('user', '0002_profile_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
                ('track_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_like', to='audio.track')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('user_id', 'track_id'), name='unique_like'),
        ),
    ]
