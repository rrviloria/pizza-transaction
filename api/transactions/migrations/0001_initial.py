# Generated by Django 2.2.4 on 2019-08-30 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product name', max_length=150)),
                ('city', models.CharField(help_text='Product manufacturing city', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Transaction amount', max_digits=11)),
                ('date_time', models.DateTimeField(help_text='Transaction date time')),
                ('product', models.ForeignKey(help_text='Transaction product', on_delete=django.db.models.deletion.CASCADE, to='transactions.Product')),
            ],
        ),
    ]
