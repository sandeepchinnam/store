# Generated by Django 4.2 on 2024-08-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_cartitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(),
        ),
    ]
