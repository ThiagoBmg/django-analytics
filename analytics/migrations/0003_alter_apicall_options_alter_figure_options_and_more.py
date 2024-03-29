# Generated by Django 4.0.5 on 2022-08-11 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("analytics", "0002_query"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apicall",
            options={
                "ordering": ["position"],
                "verbose_name": "Consulta HTTP",
                "verbose_name_plural": "Consultas HTTP",
            },
        ),
        migrations.AlterModelOptions(
            name="figure",
            options={
                "ordering": ["position"],
                "verbose_name": "Visual",
                "verbose_name_plural": "Visuais",
            },
        ),
        migrations.AlterModelOptions(
            name="query",
            options={
                "ordering": ["position"],
                "verbose_name": "Consulta Sql",
                "verbose_name_plural": "Consultas Sql",
            },
        ),
        migrations.AddField(
            model_name="query",
            name="database",
            field=models.CharField(
                default=12, help_text="Nome do banco de dados", max_length=100
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="query",
            name="query",
            field=models.TextField(
                blank=True,
                default="\n-- Configuração de filtros dinamicos\n\n-- Para consultas sem condições where {{filters}} \n-- Em consultas com where  {{and_filters}}\n\nSELECT * FROM dashboard_whatsapp {{filters}} LIMIT 1000\n",
                null=True,
            ),
        ),
    ]
