# Generated by Django 3.2.9 on 2022-12-26 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qs1', models.CharField(blank=True, max_length=500, null=True)),
                ('qs2', models.CharField(blank=True, max_length=500, null=True)),
                ('qs3', models.CharField(blank=True, max_length=500, null=True)),
                ('qs4', models.CharField(blank=True, max_length=500, null=True)),
                ('qs5', models.CharField(blank=True, max_length=500, null=True)),
                ('ans1', models.CharField(blank=True, max_length=500, null=True)),
                ('ans2', models.CharField(blank=True, max_length=500, null=True)),
                ('ans3', models.CharField(blank=True, max_length=500, null=True)),
                ('ans4', models.CharField(blank=True, max_length=500, null=True)),
                ('ans5', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
