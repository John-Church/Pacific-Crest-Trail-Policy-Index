# Generated by Django 2.2.7 on 2019-11-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='park',
            options={'verbose_name': 'Park'},
        ),
        migrations.AlterModelOptions(
            name='policy',
            options={'verbose_name': 'Policy', 'verbose_name_plural': 'Policies'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'State'},
        ),
        migrations.AddField(
            model_name='policy',
            name='category',
            field=models.CharField(choices=[('CLI', 'climate'), ('CST', 'construction'), ('INF', 'infastructure'), ('TSR', 'trail services'), ('COM', 'commercial use'), ('CON', 'conservation'), ('ENF', 'enforcement'), ('TMT', 'trail maintenance'), ('OVR', 'oversight'), ('FIN', 'finance'), ('WIL', 'wildlife'), ('PLT', 'plantlife'), ('HIK', 'hiking'), ('BIK', 'biking'), ('HRS', 'horseback riding'), ('UNC', 'unconventional use'), ('MOT', 'motorized vehicles'), ('HEA', 'health'), ('WAT', 'water'), ('FIR', 'fire'), ('VUM', 'visitor use management'), ('PER', 'permits'), ('VOL', 'volunteers'), ('OTH', 'other')], default='CON', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policy',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
