# Generated by Django 3.1 on 2021-03-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auctionlist_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlist',
            name='comentario',
        ),
    ]
