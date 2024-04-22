# Generated by Django 5.0.4 on 2024-04-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_remove_company_user_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footprintreport',
            old_name='transaction_id',
            new_name='transaction_hash',
        ),
        migrations.AlterField(
            model_name='footprintreport',
            name='reporting_period',
            field=models.CharField(choices=[('MONTH', 'Month'), ('YEAR', 'Year')], default='Month', max_length=10),
        ),
    ]