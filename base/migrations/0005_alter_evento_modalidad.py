# Generated by Django 3.2.8 on 2021-12-02 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211201_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='modalidad',
            field=models.CharField(choices=[('En Lineal', 'En Lineal'), ('Presencial', 'Presencial'), ('Mixta', 'Mixta')], max_length=30, null=True),
        ),
    ]