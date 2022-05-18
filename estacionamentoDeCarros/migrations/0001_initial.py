# Generated by Django 4.0.4 on 2022-05-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('anoFabricacao', models.CharField(max_length=30)),
                ('anoModelo', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=30)),
                ('nomePai', models.CharField(max_length=100)),
                ('nomeMae', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CNPJ', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('salario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=30)),
                ('endereco', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('carro', models.CharField(max_length=30)),
                ('funcionario', models.CharField(max_length=100)),
                ('dataLocacao', models.CharField(max_length=30)),
                ('valor', models.CharField(max_length=100)),
                ('dataDevolucao', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Seguranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vagas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
    ]
