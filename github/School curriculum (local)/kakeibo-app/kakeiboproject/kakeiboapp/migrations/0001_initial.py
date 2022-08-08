# Generated by Django 3.2 on 2022-08-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('memo', models.TextField(blank=True, null=True)),
                ('type', models.IntegerField(choices=[(0, '収入'), (1, '支出')])),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]