# Generated by Django 4.2 on 2023-05-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0002_alter_product_options_product_account_product_name_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]