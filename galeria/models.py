from django.db import models
from datetime import datetime

# Create your models here.

class fotografia(models.Model):
    OPTIONS_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALAXIA","galáxia"),
        ("PLANETA","Planeta")]
    
    nome = models.CharField(max_length= 100, null= False, blank= False)
    legenda = models.CharField(max_length= 150, null= False, blank= False)
    categoria = models.CharField(max_length=100,choices= OPTIONS_CATEGORIA, default= '')
    descricao = models.TextField( blank= False)
    foto = models.ImageField(upload_to= "fotos/%Y/%m/%d/", blank= True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default= datetime.now, blank= False)

    def __str__(self):

        return self.nome
