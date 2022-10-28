# Generated by Django 4.1.1 on 2022-10-27 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loveapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(max_length=225)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loveapp.usuario')),
            ],
        ),
    ]
