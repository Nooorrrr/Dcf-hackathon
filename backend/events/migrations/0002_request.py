# Generated by Django 5.1.7 on 2025-03-15 21:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(choices=[('volunteering', 'Volunteering'), ('borrowing', 'Borrowing')], max_length=20)),
                ('task', models.CharField(blank=True, max_length=255, null=True)),
                ('volunteers_needed', models.IntegerField(blank=True, null=True)),
                ('item_to_borrow', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity_needed', models.IntegerField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='events.event')),
            ],
        ),
    ]
