from django.db import models

# Create your models here.
class equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='titulo')
    escudo = models.ImageField(upload_to='imagenes/',verbose_name='escudo', null=True)
    descripcion = models.TextField(verbose_name='descripcion', null=True)
    
    def __str__(self):
        fila = "nombre: " + self.nombre + " - " + "descripcion: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parent=False):
        self.escudo.storage.delete(self.escudo.name)
        super().delete()