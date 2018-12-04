# Generated by Django 2.1.4 on 2018-12-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Principle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('age', models.IntegerField(max_length=64)),
                ('qualification', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='principleName',
            field=models.OneToOneField(on_delete='CASCADE', to='onetoone.Principle'),
        ),
    ]