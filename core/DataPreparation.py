# libraries
import utils as ut

class DataPreparation:
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df

    # Limpia los nombres de las columnas y crea nuevas características como 'average_score'.
    def clean_and_engineer_features(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return

        # Cambiar el nombre de las columnas para facilitar el acceso
        self.df.columns = self.df.columns.str.replace(' ', '_').str.lower()

        # Crear la columna 'average_score'
        self.df['average_score'] = self.df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)
        print("Datos limpios y característica 'average_score' creada.")
        return self.df