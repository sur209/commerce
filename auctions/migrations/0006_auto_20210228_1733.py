# Generated by Django 3.1 on 2021-02-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210228_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlist',
            name='montoinicial',
        ),
        migrations.AddField(
            model_name='auctionlist',
            name='monto',
            field=models.ManyToManyField(default=0, related_name='Amount', to='auctions.Bid'),
        ),
    ]