# librarias
import core.utils as ut

# clases
from core.LoadData import LoadData
from core.DistribucionMultiple import DistribucionMultiple
from core.LimpiaValida import LimpiaValida
from core.operaciones import Operaciones
from core.AnalisisEducacionPadres import AnalisisEducacionPadres

class DataAnalysis:
    def __init__(self):
        self.df = None
        self.loader = LoadData()
        self.multiple = DistribucionMultiple()
        self.valida = LimpiaValida()
        self.operar = Operaciones()
        self.edu_padres = AnalisisEducacionPadres()

    # Cargar datos
    def load_data(self, file_path):
        self.df = self.loader.load_data(file_path)
        self.multiple.df = self.df
        self.valida.df = self.df
        self.operar.df = self.df
        self.edu_padres.df = self.df

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

        
    # Respuesta Tercera pregunta
    def influencia_padres_educacion(self):
        self.operar.calcular_promedio()
        self.edu_padres.educacion_padres()


    # Respuesta Cuarta pregunta
    
    # Respuesta Quinta pregunta
    
    # Respuesta Sexta pregunta
    
    # Respuesta Septima pregunta
    
    # Respuesta Octava pregunta
    
    # Respuesta Novena pregunta
    
    # Respuesta Decima pregunta