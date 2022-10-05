# Generated by Django 4.1.1 on 2022-10-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ver_familia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subfamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=30)),
                ('asignacion', models.CharField(max_length=50)),
                ('invitados', models.IntegerField()),
                ('fecha_pago', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
    ]