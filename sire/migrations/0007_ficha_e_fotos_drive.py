"""Extensão opcional da ficha — não substitui a baseline ER-SIRE 2.1."""
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [("sire", "0006_excursao_tipo_pacote")]

    operations = [
        migrations.AddField(
            model_name="excursao", name="descricao",
            field=models.TextField(blank=True, default="", verbose_name="Descrição do pacote"),
        ),
        migrations.AddField(
            model_name="excursao", name="roteiro",
            field=models.TextField(blank=True, default="", verbose_name="Roteiro da viagem"),
        ),
        migrations.AddField(
            model_name="excursao", name="inclusos",
            field=models.TextField(blank=True, default="", verbose_name="Itens inclusos (um por linha)"),
        ),
        migrations.CreateModel(
            name="FotoExcursao",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("drive_id", models.CharField(max_length=128, unique=True, verbose_name="ID no Google Drive")),
                ("criada_em", models.DateTimeField(auto_now_add=True)),
                ("excursao", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="fotos", to="sire.excursao")),
            ],
            options={"db_table": "sire_foto_excursao", "ordering": ("id",)},
        ),
    ]
