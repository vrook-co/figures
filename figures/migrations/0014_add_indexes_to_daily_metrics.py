# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-08 09:30
"""
Hand edited to run separate database and state migrations to add indexes to
SiteDailyMetrics and CourseDailyMetrics
"""
from __future__ import unicode_literals

from django.db import migrations, models
from django.db import connection


def compat_drop_index(index, table):
    """Compatibility function to drop a database index

    Because MySQL requires the table name in the drop statement and SQLite
    fails if the `ON table_name` is provided
    """
    if connection.vendor == 'mysql':
        return 'DROP INDEX {index} ON {table}'.format(index=index, table=table)
    else:
        return 'DROP INDEX {index}'.format(index=index)


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('figures', '0013_add_indexes_to_lcgm_date_for_and_course_id'),
    ]

    operations = [

        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterField(
                    model_name='coursedailymetrics',
                    name='course_id',
                    field=models.CharField(db_index=True, max_length=255),
                ),
                migrations.AlterField(
                    model_name='coursedailymetrics',
                    name='date_for',
                    field=models.DateField(db_index=True),
                ),
                migrations.AlterField(
                    model_name='sitedailymetrics',
                    name='date_for',
                    field=models.DateField(db_index=True),
                ),
            ],
            database_operations=[
                migrations.RunSQL(sql="""
                    CREATE INDEX figures_coursedailymetrics_course_id_f7047b32
                    ON figures_coursedailymetrics (course_id);
                """, reverse_sql=compat_drop_index(
                        index='figures_coursedailymetrics_course_id_f7047b32',
                        table='figures_coursedailymetrics')),
                migrations.RunSQL(sql="""
                    CREATE INDEX figures_coursedailymetrics_date_for_481b5758
                    ON figures_coursedailymetrics (date_for);
                """, reverse_sql=compat_drop_index(
                        index='figures_coursedailymetrics_date_for_481b5758',
                        table='figures_coursedailymetrics')),
                migrations.RunSQL(sql="""
                    CREATE INDEX figures_sitedailymetrics_date_for_4d95be72
                    ON figures_sitedailymetrics (date_for);
                """, reverse_sql=compat_drop_index(
                        index='figures_sitedailymetrics_date_for_4d95be72',
                        table='figures_sitedailymetrics')
                    )
            ]
        )

    ]