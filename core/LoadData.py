# libraries
import core.utils as ut

class LoadData():
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df 

    # Cargar datos desde un archivo CSV.
    def load_data(self, file_path):
        self.df = ut.pd.read_csv(file_path)