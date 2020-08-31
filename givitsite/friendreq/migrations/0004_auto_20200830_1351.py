# Generated by Django 3.1 on 2020-08-30 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendreq', '0003_auto_20200830_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemrequest',
            name='friend_id',
            field=models.IntegerField(default=305355356),
        ),
        migrations.AlterField(
            model_name='itemrequest',
            name='special_req',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='itemrequest',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('closed', 'closed')], default='open', max_length=40),
        ),
    ]
