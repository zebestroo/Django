# Generated by Django 4.0.5 on 2022-07-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_app', '0003_customer_remove_human_mail_remove_human_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entry', models.DateField()),
            ],
        ),
    ]