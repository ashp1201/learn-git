# Generated by Django 4.1.6 on 2023-03-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('cemail', models.CharField(max_length=200)),
                ('pass1', models.CharField(max_length=200, null=True)),
                ('pass2', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('femail', models.CharField(max_length=200)),
                ('pass1', models.CharField(max_length=200, null=True)),
                ('pass2', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=200)),
                ('pprice', models.IntegerField()),
                ('pquality', models.CharField(max_length=10)),
                ('pquantity', models.IntegerField()),
                ('pimage', models.ImageField(default='', upload_to='static/meadia/pimage')),
            ],
        ),
    ]
