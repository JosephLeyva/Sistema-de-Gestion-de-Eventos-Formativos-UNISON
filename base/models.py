from django.db import models


# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    TIPO_EVENTOS = (
            ('Diplomado','Diplomado'),
            ('Curso','Curso'),
            ('Taller','Taller'),
            ('Programa Especial','Programa Especial')
        )
    TipoEventos =  models.CharField(max_length=30,null=True,choices=TIPO_EVENTOS)
    TIPO_MODALIDAD = (
            ('En Lineal', 'En Lineal'),
            ('Presencial','Presencial'),
            ('Mixta','Mixta')
        )
    modalidad = models.CharField(max_length=30,null=True,choices=TIPO_MODALIDAD)
    objetivos = models.TextField(null=True)
    experiencias = models.TextField(null=True)
    contenido = models.TextField(null=True)
    recursos_y_materiales = models.TextField(null=True,blank=True)
    Estrategias_de_Evaluacion = models.TextField(null=True)
    Fecha_de_Inicio = models.DateField()
    Fecha_de_Fin = models.DateField()
    Referencias_y_bibliografia = models.TextField(null=True,blank=True)
    Utilidad_y_Oportunidad_del_programa = models.TextField(null=True)
    Cupo_Maximo = models.CharField(max_length=3)
    Requisistos_de_Acreditacion = models.TextField(null=True)
    Experiencia_y_pericia_de_Instructores = models.TextField(null=True)
    Dirigido_a = models.TextField(null=True)
    Requisitos_de_Participacion = models.TextField(null=True)
    Curriculum_de_los_Instructores = models.TextField(null=True)
    Capacidad_de_utofinanciamiento = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.nombre
    


