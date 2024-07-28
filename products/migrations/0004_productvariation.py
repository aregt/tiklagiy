# Generated by Django 4.2.14 on 2024-07-28 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_productsize"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductVariation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("color", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="product_images/"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="variations",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
