# Generated by Django 2.1.3 on 2018-11-22 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0005_dept_excellent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'hrs_blogspost',
            },
        ),
    ]
