# Generated by Django 4.1.3 on 2023-01-05 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ui", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="employee_data",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ui.employeedata",
            ),
        ),
    ]
