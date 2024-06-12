import uuid
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Nome', max_length=400)
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    values = models.FloatField(verbose_name='Valor', default=0.0)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Opções"
        verbose_name_plural = "Cardápio"

    def __str__(self):
        return self.name


class Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.CharField(verbose_name='Númeração', max_length=2)
    availability = models.BooleanField(verbose_name='Disponibilidade', default=True)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mesa"
        verbose_name_plural = "Mesas"

    def __str__(self):
        return self.number
    

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.CharField(verbose_name='Cliente', max_length=400, null=True, blank=True)
    created_by = models.ForeignKey(User, verbose_name='Criado por', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id.__str__()
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class ItemOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, verbose_name='Item', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.PositiveBigIntegerField(verbose_name='Quantidade', default=1)
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"