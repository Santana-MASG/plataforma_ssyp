from django.db import models
from django.contrib.auth.models import User

class Alumno(User):
    id_alumno = models.BigAutoField(primary_key=True)
    id_programa_academico = models.ForeignKey("instituciones.ProgramaAcademico", verbose_name="Programa académico", on_delete=models.DO_NOTHING)
    id_intitucion_ss = models.ForeignKey(
        "instituciones.Intitucion", verbose_name="Institución de servicio social", on_delete=models.DO_NOTHING, blank=True, null=True)
    id_intitucion_pp = models.ForeignKey(
        "instituciones.Intitucion", verbose_name="Institución de prácticas profesionales", on_delete=models.DO_NOTHING, blank=True, null=True)
    estatus = models.CharField("Estado", max_length=30)
    matricula = models.IntegerField("Matrícula", max_length=8)
    numero_creditos = models.IntegerField("Número de créditos", max_length=3)
    semestre = models.IntegerField(max_length=2)
    grupo = models.CharField(max_length=1)
    celular = models.PhoneNumberField(max_length=10)
    telefono_fijo = models.PhoneNumberField("Teléfono fijo", max_length=10)
    calle = models.CharField(max_length=50)
    numero_casa = models.IntegerField("Número de casa",max_length=4)
    colonia = models.CharField("Colonia", max_length=50)
    localidad = models.CharField("Localidad", max_length=50)
    codigo_postal = models.IntegerField("Código postal",max_length=5)
    ciudad_origen = models.CharField("Ciudad de origen",max_length=100)
    foto = models.ImageField("Foto de perfil", upload_to='perfiles', blank=True, null=True)
    kardex_ss = models.models.FileField("", upload_to='uploads', max_length=100, blank=True, null=True)
    kardex_pp = models.models.FileField("Kardes para prácticas profesionales", upload_to=None, max_length=100, blank=True, null=True)
    contancia_estudios_ss = models.models.FileField("Constancia de estudios para servivio social", upload_to=None, max_length=100, blank=True, null=True)
    contancia_estudios_pp = models.models.FileField("Constancia de estudios para pácticas profesionales", upload_to=None, max_length=100, blank=True, null=True)
    carta_aceptacion = models.models.FileField("Carta de aceptación", upload_to=None, max_length=100, blank=True, null=True)
    carta_liberacion = models.models.FileField("Carta de libreración", upload_to=None, max_length=100, blank=True, null=True)#Esta nunca la llevan y se podría decir que no es obligatoria
    nombre_proyecto_ss = models.CharField("Nombre del proyecto del servicio social", max_length=100, blank=True, null=True)
    nombre_proyecto_pp = models.CharField("Nombre del proyecto del la prácticas profesionales", max_length=100, blank=True, null=True)
    red_social = models.CharField("Red social", max_length=70)
    numero_serie = models.models.CharField("Número de serie", max_length=100, blank=True, null=True)
    certificado = models.CharField(max_length=3000, blank=True, null=True)
    constrsena_certificado = models.CharField("Contraseña de certificado", max_length=100, blank=True, null=True)

    def __str__(self):
        return "Alumno" + self.matricula


class Notificaciones(models.Model):
    """
    Modelo para almacenar las notificaciones de todos los usuario del sistema
    """
    id_notificacion = models.AutoField(max_length=8, primary_key=True)
    id_alumno = models.ForeignKey("Alumno", verbose_name="ID alumno", on_delete=models.DO_NOTHING)
    mensaje = models.CharField(max_length=500)
    estatus = models.BooleanField(default=True)

    def __str__(self):
        return "Notifiación"

class ReporteMensual(models.Model):
    """
    Este modelo almacena reportes mansuales del servico social
    """
    id_alumno = models.ForeignKey("Alumno", verbose_name="ID alumno", on_delete=models.DO_NOTHING)
    fecha_inicio = models.DateField("Fecha inicio", auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField("Fecha fin", auto_now=False, auto_now_add=False)
    fecha = models.models.DateTimeField("Fecha en que se creó el reporte", auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Reporte mensual"


class ReporteInicial(models.Model):
    """
    - Modelo para que almacena la información de reportes iniciales de Servicio Social y Prácticas Profesionales
    - El servicio puede durar un hasta un año
    """
    id_reporte_inicial = models.AutoField(max_length=8, primary_key=True)
    id_alumno = models.ForeignKey(
        "alumnos.Alumno", verbose_name="Id alumno", on_delete=models.DO_NOTHING)
    mes_1 = models.CharField(max_length="750", blank=True, null=True) 
    mes_2 = models.CharField(max_length="750", blank=True, null=True) 
    mes_3 = models.CharField(max_length="750", blank=True, null=True) 
    mes_4 = models.CharField(max_length="750", blank=True, null=True) 
    mes_5 = models.CharField(max_length="750", blank=True, null=True) 
    mes_6 = models.CharField(max_length="750", blank=True, null=True) 
    mes_7 = models.CharField(max_length="750", blank=True, null=True) 
    mes_8 = models.CharField(max_length="750", blank=True, null=True) 
    mes_9 = models.CharField(max_length="750", blank=True, null=True) 
    mes_10 = models.CharField(max_length="750", blank=True, null=True) 
    mes_11 = models.CharField(max_length="750", blank=True, null=True) 
    mes_12 = models.CharField(max_length="750", blank=True, null=True) 
    fecha = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "Reporte inicial"

class ReporteFinal(models.Model):
    """
    Modelo para que almacena la información de reportes finales de Servicio Social y Prácticas Profesionales
    """
    id_reporte_final = models.AutoField(max_length=8, primary_key=True)
    id_alumno = models.ForeignKey("alumnos.Alumno", verbose_name="ID alumno", on_delete=models.DO_NOTHING)
    horas_acumuladas = models.IntegerField(max_length=3)
    fecha_inicio_ss = models.models.DateField("Fecha de inicio", auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_fin_ss = models.models.DateField("Fecha en que terminó", auto_now=False, auto_now_add=False, blank=True, null=True)
    descripcion = models.CharField("Descripción", max_length=5000)
    fecha = models.DateField("Fecha", auto_now=False, auto_now_add=False)

    def __str__(self):
        return "Reporte final"
