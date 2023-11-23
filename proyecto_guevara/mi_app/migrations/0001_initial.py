# Generated by Django 4.2.7 on 2023-11-23 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Catedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('profesor', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('catedras', models.ManyToManyField(to='mi_app.catedra')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.curso')),
            ],
        ),
    ]
