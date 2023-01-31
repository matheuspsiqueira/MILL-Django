from datetime import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('codigo_produto', models.IntegerField()),
                ('quantidade_produto', models.IntegerField()),
                ('nome_fornecedor', models.CharField(max_length=100)),
                ('valor_unitario', models.FloatField()),
                ('date_produto', models.DateTimeField(blank=True, default=datetime.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]