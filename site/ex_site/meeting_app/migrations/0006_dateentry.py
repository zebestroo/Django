# Generated by Django 4.0.5 on 2022-07-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0005_delete_dateentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entry', models.DateField()),
                ('surname', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
