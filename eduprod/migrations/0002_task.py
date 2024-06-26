# Generated by Django 5.0.2 on 2024-03-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=15)),
                ('task_type', models.CharField(choices=[('homework', 'Homework'), ('assessment', 'Assessment')], max_length=10)),
                ('subject', models.CharField(max_length=15)),
                ('due_date', models.DateField()),
                ('task_requirements', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
        ),
    ]
