# Generated by Django 4.2 on 2023-05-08 17:03

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("carts", "0003_alter_cart_account"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="account",
            new_name="user",
        ),
    ]