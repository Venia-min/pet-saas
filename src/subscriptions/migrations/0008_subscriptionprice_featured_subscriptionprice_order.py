# Generated by Django 5.0.8 on 2024-09-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_subscriptionprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionprice',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscriptionprice',
            name='order',
            field=models.IntegerField(default=-1),
        ),
    ]
