# Generated by Django 2.0.1 on 2018-01-24 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField(default=5)),
                ('x_pos', models.FloatField()),
                ('y_pos', models.FloatField()),
                ('is_on_station', models.BooleanField(default=False)),
                ('last_update_time', models.TimeField(auto_now=True)),
                ('token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_final_station', models.BooleanField(default=False)),
                ('bus_wait_time', models.IntegerField(default=5)),
                ('x_pos', models.FloatField()),
                ('y_pos', models.FloatField()),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='bus.Line')),
                ('my_next_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_station', to='bus.Station')),
                ('my_prev_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_station', to='bus.Station')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='line',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buses', to='bus.Line'),
        ),
        migrations.AddField(
            model_name='bus',
            name='next_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prev_buses', to='bus.Station'),
        ),
        migrations.AddField(
            model_name='bus',
            name='prev_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_buses', to='bus.Station'),
        ),
    ]
