# Generated by Django 5.0.8 on 2024-09-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_subscription_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]