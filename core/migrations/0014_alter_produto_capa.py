# Generated by Django 5.0.6 on 2024-10-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_produto_quantidade"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="capa",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
    ]