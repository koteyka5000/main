# Generated by Django 4.1.5 on 2023-01-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.IntegerField(choices=[(1, 'One Star'), (2, 'Two Star'), (3, 'Three Star'), (4, 'Four Star'), (5, 'Five Star')])),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
