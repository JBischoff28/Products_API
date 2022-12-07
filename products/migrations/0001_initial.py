# Generated by Django 4.1.4 on 2022-12-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=510)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('inventory_quantity', models.IntegerField()),
            ],
        ),
    ]