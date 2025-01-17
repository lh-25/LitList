# Generated by Django 5.1.3 on 2024-12-04 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('read_status', models.CharField(choices=[('P', 'Planned to read'), ('R', 'Reading'), ('F', 'Finished')], default='P', max_length=1)),
                ('publish_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
