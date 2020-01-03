# Generated by Django 2.2.5 on 2020-01-01 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_centerwarehouse_center'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='meterage_name',
        ),
        migrations.AddField(
            model_name='material',
            name='meterage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='meterage_material', to='base.Meterage', verbose_name='计量单位'),
            preserve_default=False,
        ),
    ]