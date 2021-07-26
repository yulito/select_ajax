from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(null=False, primary_key=True)
    nomCategoria = models.CharField(max_length=60, null=False, blank=False)
    class Meta:
        db_table = "categoria"

class Producto(models.Model):
    idProducto = models.IntegerField(null=False, primary_key=True)
    nomProducto = models.CharField(max_length=60, null=False, blank=False)
    categoriaa = models.ForeignKey(Categoria, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = "producto"

class Compra(models.Model):
    idCompra = models.AutoField( primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    productoo = models.ForeignKey(Producto, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        db_table = "compra"

