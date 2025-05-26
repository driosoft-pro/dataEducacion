# librarias
import core.utils as ut

# clases
from core.LoadData import LoadData
from core.LimpiaValida import LimpiaValida
from core.operaciones import Operaciones
from core.DistribucionMultiple import DistribucionMultiple #1
from core.AnalisisMejoresPromedios import AnalisisMejoresPromedios #2
from core.AnalisisEducacionPadres import AnalisisEducacionPadres #3
from core.AnalisisPreparacionEstudiantil import AnalisisPreparacionEstudiantil #4
from core.AnalisisPromedioGeneroBajaAlimentacion import AnalisisPromedioGeneroBajaAlimentacion #5
from core.RendimientoGrupoEtnico import RendimientoGrupoEtnico #6
from core.AnalisisCorrelacionCalificaciones import AnalisisCorrelacionCalificaciones #7
from core.AnalisisPromedioAcademicoAlimentacion import AnalisisPromedioAcademicoAlimentacion #8
from core.AnalisisCalificacion import AnalisisCalificacion #9
from core.AnalisisDistribucionConjunta import AnalisisDistribucionConjunta #10
from core.ResumenHallazgosClave import ResumenHallazgosClave #Analisis

class DataAnalysis:
    def __init__(self):
        self.df = None
        self.loader = LoadData()
        self.valida = LimpiaValida()
        self.operar = Operaciones()
        self.multiple = DistribucionMultiple()
        self.mejor_promedio = AnalisisMejoresPromedios()
        self.edu_padres = AnalisisEducacionPadres()
        self.estudiantes_preparados = AnalisisPreparacionEstudiantil()
        self.estudiantes_baja_alimentacion = AnalisisPromedioGeneroBajaAlimentacion()
        self.rendimiento_grupo = RendimientoGrupoEtnico()
        self.analisis_correlacion = AnalisisCorrelacionCalificaciones()
        self.analisis_promedio_alimentacion = AnalisisPromedioAcademicoAlimentacion()
        self.analis_calificaciones = AnalisisCalificacion()
        self.dist_conjunta = AnalisisDistribucionConjunta()
        self.analisis_final = ResumenHallazgosClave()
        

    # Cargar datos
    def load_data(self, file_path):
        self.df = self.loader.load_data(file_path)
        self.valida.df = self.df
        self.operar.df = self.df
        self.multiple.df = self.df
        self.mejor_promedio.df = self.df
        self.edu_padres.df = self.df
        self.estudiantes_preparados.df = self.df
        self.estudiantes_baja_alimentacion.df = self.df
        self.rendimiento_grupo.df = self.df
        self.analisis_correlacion.df = self.df
        self.analisis_promedio_alimentacion.df = self.df
        self.analis_calificaciones.df = self.df
        self.dist_conjunta.df = self.df
        self.analisis_final.df = self.df

    # Cargar datos sin encabezado
    def load_data_not_head(self, file_path):
        self.df = self.loader.load_data_not_head(file_path)
    
    # Validar Datos    
    def validar_nombres(self):
        self.valida.validar_nombres()
        
    def validar_datos(self):
        self.valida.validar_datos()
        
    def validar_informacion(self):
        self.valida.validar_informacion()
            
    def validar_tipos(self):
        self.valida.validar_tipos()
                
    def validar_descriptivos(self):
        self.valida.validar_descriptivos()

    def validar_observaciones_atributos(self):        
        self.valida.validar_observaciones_atributos()

    def validar_nulos(self):        
        self.valida.validar_nulos()
        
    def validar_porcentaje_nulos(self):        
        self.valida.validar_porcentaje_nulos()
    
    def contar_duplicados(self):
        self.valida.contar_duplicados()
        
    def eliminar_duplicados(self):
        self.valida.eliminar_duplicados()    
            
    def limpiar(self):
        self.valida.limpiar()
        
    # Respuesta Primera pregunta
    def analizar_distribuciones_multiples(self, *columns):
        self.multiple.analizar(columns)
        
    # Respuesta Segunda pregunta
    def mejores_promedios(self):
        self.operar.calcular_promedio()
        self.mejor_promedio.analizar_mejores_promedios_por_genero()

    # Respuesta Tercera pregunta
    def influencia_padres_educacion(self):
        self.operar.calcular_promedio()
        self.edu_padres.educacion_padres()

    # Respuesta Cuarta pregunta
    def preparacion_estudiantil(self):
        self.estudiantes_preparados.graficar_resultados_preparacion()
        self.estudiantes_preparados.mostrar_estadisticas_preparacion()  

    # Respuesta Quinta pregunta
    def baja_alimentacion(self):
        self.estudiantes_baja_alimentacion.analizar_promedio_baja_alimentacion()
    
    # Respuesta Sexta pregunta
    def rendimiento_grupos(self):
        self.operar.calcular_promedio()
        self.rendimiento_grupo.graficar_rendimiento_etnico
        self.rendimiento_grupo.mostrar_estadisticas_etnicas()

    # Respuesta Septima pregunta
    def correlacion(self):
        self.analisis_correlacion.mostrar_matriz_correlacion()

    # Respuesta Octava pregunta
    def promedio_academico_alimentacion(self):
        self.analisis_promedio_alimentacion.mostrar_promedio_por_almuerzo()
        
    # Respuesta Novena pregunta
    def calificaciones(self):
        self.analis_calificaciones.analizar_rendimiento()

    # Respuesta Decima pregunta
    def distribucion_conjunta(self):
        self.dist_conjunta.generar_graficos()
    
    # Resumen de hallazgos del analisis    
    def resumen_hallazgos(self, gender_scores, prep_scores, education_scores, correlation_matrix):
        self.operar.calcular_promedio()
        self.analisis_final.mostrar_resumen(gender_scores, prep_scores, education_scores, correlation_matrix)