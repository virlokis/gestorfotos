from django.db import models


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_imagen = models.ImageField(null=True, blank=True, upload_to='eventos')
    fecha = models.DateField()

    def __str__(self):
        return self.nombre


class Competidor(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    archivo_imagen = models.ImageField(null=True, blank=True, upload_to='competidores')
    fecha = models.DateField()

    def __str__(self):
        return self.nombre


class Dorsal(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    competidor = models.ForeignKey(Competidor,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True,
                                   )
    numero_dorsal = models.IntegerField()
    archivo_imagen = models.ImageField(null=True, blank=True, upload_to='dorsales')

    def __str__(self):
        return str(self.numero_dorsal)


class Foto(models.Model):
    dorsal = models.ForeignKey(Dorsal,
                            on_delete=models.CASCADE,
                            blank=True,
                            null=True,
                            )
    nombre = models.CharField(max_length=100)
    archivo_imagen = models.ImageField(null=True, blank=True, upload_to='fotos')

    def __unicode__(self, ):
        return str(self.archivo_imagen)
