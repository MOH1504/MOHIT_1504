# Generated by Django 4.2.1 on 2023-05-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='costomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30, unique=True)),
                ('Password', models.IntegerField(max_length=30)),
                ('Confirm_Password', models.CharField(max_length=30)),
                ('Frish_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Phome_Number', models.IntegerField(max_length=30)),
            ],
        ),
    ]
