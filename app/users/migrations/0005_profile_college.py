# Generated by Django 3.1 on 2020-08-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_grad_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(choices=[('CALS', 'Agriculture and Life Sciences'), ('AAP', 'Architecture, Art, and Planning'), ('AS', 'Arts and Sciences'), ('COE', 'Engineering'), ('HUMEC', 'Human Ecology'), ('ILR', 'Industrial and Labor Relations'), ('SCJCB', 'SC Johnson College of Business')], default='AS', max_length=5),
        ),
    ]
