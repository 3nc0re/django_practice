# Generated by Django 4.2.2 on 2023-07-08 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='organization',
        ),
        migrations.CreateModel(
            name='MedicineOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicine')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.organization')),
            ],
        ),
    ]
