# Generated manually for the product status and category management changes.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nombre', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
    ]
