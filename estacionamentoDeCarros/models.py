from django.db import models

# Create your models here.
class Carro(models.Model):
    placa = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anoFabricacao = models.CharField(max_length=30)
    anoModelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    def __str__(self):
        return self.codigo

class Cliente(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=30)
    nomePai = models.CharField(max_length=100)
    nomeMae = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.codigo

class Funcionario(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    salario = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    def __str__(self):
        return self.codigo

class Fornecedor(models.Model):
    CNPJ = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    def __str__(self):
        return self.codigo

class Seguranca(models.Model):
    CPF = models.CharField(max_length=100)
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=30)
    def __str__(self):
        return self.codigo

class Vagas(models.Model):
    ID = models.CharField(max_length=100)
    descricao = models.CharField(max_length=30)
    def __str__(self):
        return self.codigo
