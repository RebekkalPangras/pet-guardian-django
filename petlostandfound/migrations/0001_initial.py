# Generated by Django 4.2.4 on 2023-08-07 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('age', models.PositiveIntegerField(null=True)),
                ('pet_type', models.CharField(max_length=50)),
                ('breed', models.CharField(blank=True, max_length=50)),
                ('sex', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('color', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='petlostandfound.user')),
            ],
        ),
        migrations.CreateModel(
            name='LostPetReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_date', models.DateField()),
                ('last_seen_location', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('is_found', models.BooleanField(default=False)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petlostandfound.pet')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petlostandfound.user')),
            ],
        ),
    ]