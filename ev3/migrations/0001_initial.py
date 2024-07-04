from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('producto', models.CharField(max_length=1000)),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
