# Generated by Django 5.0.6 on 2024-05-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='prix_panier',
        ),
        migrations.AddField(
            model_name='collecte',
            name='prix_panier',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
