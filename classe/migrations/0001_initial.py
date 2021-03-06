# Generated by Django 2.1.3 on 2019-01-25 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sala_aula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('max_alunos', models.CharField(blank=True, max_length=20, null=True)),
                ('unidade', models.CharField(blank=True, max_length=200, null=True)),
                ('obs', models.CharField(blank=True, max_length=400, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
