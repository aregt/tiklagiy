# Generated by Django 4.2.14 on 2024-07-28 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_category_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSize",
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
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("XS", "Extra Small"),
                            ("S", "Small"),
                            ("M", "Medium"),
                            ("L", "Large"),
                            ("XL", "Extra Large"),
                            ("XXL", "Double Extra Large"),
                        ],
                        max_length=3,
                    ),
                ),
                ("chest", models.FloatField(blank=True, null=True)),
                ("waist", models.FloatField(blank=True, null=True)),
                ("hips", models.FloatField(blank=True, null=True)),
                ("length", models.FloatField(blank=True, null=True)),
                ("stock", models.PositiveIntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sizes",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "unique_together": {("product", "size")},
            },
        ),
    ]