# Generated by Django 2.2 on 2020-05-17 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('data_type', models.CharField(choices=[('character', 'character'), ('text', 'text'), ('integer', 'integer'), ('float', 'float'), ('boolean', 'boolean'), ('date', 'date')], editable=False, max_length=16)),
                ('null', models.BooleanField(default=False)),
                ('unique', models.BooleanField(default=False)),
                ('max_length', models.PositiveIntegerField(null=True)),
                ('model_schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='dynamic_models.ModelSchema')),
            ],
            options={
                'unique_together': {('name', 'model_schema')},
            },
        ),
    ]