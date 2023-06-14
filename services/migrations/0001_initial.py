# Generated by Django 4.2 on 2023-06-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=1000, unique=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=1000)),
                ('Role', models.CharField(default='', max_length=500)),
                ('Typeofinst', models.CharField(blank=True, default='', max_length=500)),
                ('Institute', models.CharField(blank=True, default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('Linkedin', models.CharField(blank=True, default='', max_length=500)),
                ('Aboutclient', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, null=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(default='', max_length=30)),
                ('mobile', models.CharField(default='', max_length=30)),
                ('Refered', models.CharField(default='NA', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobsupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=1000)),
                ('Company', models.CharField(default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('Concern', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Mobileno', models.CharField(default='', max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('Profession', models.CharField(blank=True, default='', max_length=200)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=1000)),
                ('Institute', models.CharField(default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('yearofpassout', models.DateField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=300, null=True)),
                ('Email', models.CharField(default='', max_length=30, null=True)),
                ('Mobile', models.CharField(default='', max_length=30, null=True)),
                ('Role', models.CharField(default='', max_length=500)),
                ('Typeofinst', models.CharField(blank=True, default='', max_length=500)),
                ('Institute', models.CharField(blank=True, default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('Aboutapp', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SessionRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=1000)),
                ('Role', models.CharField(default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('Typeofinst', models.CharField(default='', max_length=500)),
                ('Institute', models.CharField(default='', max_length=500)),
                ('Linkedin', models.CharField(blank=True, default='', max_length=500)),
                ('Aboutclient', models.TextField(blank=True, default='', max_length=500)),
                ('PaymentGateway', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=300, null=True)),
                ('Email', models.CharField(default='', max_length=30, null=True)),
                ('Mobile', models.CharField(default='', max_length=30, null=True)),
                ('Role', models.CharField(default='', max_length=500)),
                ('Typeofinst', models.CharField(blank=True, default='', max_length=500)),
                ('Institute', models.CharField(blank=True, default='', max_length=500)),
                ('Qualification', models.CharField(blank=True, default='', max_length=500)),
                ('Aboutapp', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Made_on', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(default='', max_length=1000)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile', models.CharField(default='', max_length=1000)),
                ('Role', models.CharField(default='', max_length=500)),
                ('Typeofinst', models.CharField(blank=True, default='', max_length=500)),
                ('Institute', models.CharField(blank=True, default='', max_length=500)),
                ('AboutTicket', models.TextField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_by', models.CharField(max_length=100)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=100)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transcatid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('transcation_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]