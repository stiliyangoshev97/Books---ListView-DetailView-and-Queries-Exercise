# Generated by Django 3.2.4 on 2021-06-12 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beats_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('owner', models.CharField(max_length=64)),
                ('beat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beats_app.beat')),
            ],
        ),
    ]