"""Extensão de catálogo: categoria opcional sem alterar dados anteriores."""
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("sire", "0007_ficha_e_fotos_drive")]
    operations = [migrations.AddField(
        model_name="excursao", name="categoria",
        field=models.CharField("categoria da viagem", max_length=20,
            choices=[("PRAIA", "Praias"), ("CACHOEIRA", "Cachoeiras"), ("MONTANHA", "Montanhas e serra"), ("TRILHA", "Trilhas e aventura"), ("GRUTA", "Cavernas e grutas"), ("PARQUE", "Parques e diversão"), ("CULTURA", "Cultura e gastronomia"), ("RELAXAR", "Relaxamento e natureza"), ("RELIGIOSO", "Turismo religioso"), ("EVENTO", "Eventos e shows")], blank=True, default=""),
    )]
