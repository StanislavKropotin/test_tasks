# Generated by Django 5.0.6 on 2024-10-03 07:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='points',
            new_name='daily_points',
        ),
        migrations.AddField(
            model_name='boost',
            name='expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='player',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boost',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='boosts', to='player_management.player'),
        ),
        migrations.AlterField(
            model_name='boost',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='PlayerDailyActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('points_earned', models.IntegerField(default=0)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='daily_activities', to='player_management.player')),
            ],
        ),
    ]
