# Generated by Django 5.0.8 on 2024-09-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_usersubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]