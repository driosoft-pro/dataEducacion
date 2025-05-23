# libraries
import utils as ut

class ExploratoryAnalysis:
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df

    # Imprime la información del DataFrame.
    def check_info(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        print("\n--- DataFrame Info ---")
        self.df.info()

    # Verifica e imprime el conteo y porcentaje de valores faltantes.
    def check_missing_values(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        print("\n--- Valores Faltantes ---")
        missing_values = self.df.isnull().sum()
        missing_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        missing_table = ut.pd.DataFrame({
            'Conteo de Faltantes': missing_values,
            'Porcentaje de Faltantes': missing_percentage
        })
        print(missing_table[missing_table['Conteo de Faltantes'] > 0])

    # Muestra estadísticas descriptivas para columnas numéricas y opcionalmente categóricas.
    def display_descriptive_statistics(self, include_object=False):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        print("\n--- Estadísticas Descriptivas (Numéricas) ---")
        print(self.df.describe())

        if include_object:
            print("\n--- Estadísticas Descriptivas (Categóricas) ---")
            print(self.df.describe(include='object'))

    # Imprime los valores únicos y sus conteos para todas las columnas.
    def check_unique_values(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        print("\n--- Valores Únicos ---")
        for column in self.df.columns:
            unique_count = self.df[column].nunique()
            print(f"Columna '{column}': {unique_count} valores únicos")
            if unique_count < 20 and self.df[column].dtype == 'object':  # Mostrar conteos de valores para categóricas con pocos valores únicos
                print(self.df[column].value_counts())
            print("-" * 30)