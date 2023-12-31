# Generated by Django 4.2.2 on 2023-07-08 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurisdictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrgTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('org_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Substance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100)),
                ('laws_specifics', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('jurisdiction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jurisdictions')),
                ('organization_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.orgtypes')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('expiration_date', models.DateField()),
                ('is_generic', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('form', models.CharField(max_length=100)),
                ('organization', models.ManyToManyField(to='app.organization')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producer')),
                ('substance_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.substance')),
            ],
        ),
    ]
