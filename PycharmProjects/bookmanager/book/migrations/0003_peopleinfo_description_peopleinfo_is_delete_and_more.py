# Generated by Django 5.0.2 on 2024-02-28 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookinfo_options_bookinfo_comment_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], default=1),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]