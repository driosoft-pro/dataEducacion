# librerías
import core.utils as ut

# clases
from .LoadData import LoadData
from .DataPreparation import DataPreparation
from .ExploratoryAnalysis import ExploratoryAnalysis
from .AnalisisDistribucion import AnalisisDistribucion # Importación corregida basada en el nombre del archivo
from .RelationshipAnalysis import RelationshipAnalysis
from .KeyFindings import KeyFindings

class DataAnalysis():
    # El DataFrame principal que se utilizará en todas las operaciones
    def __init__(self):
        # Inicializar el DataFrame principal como Ninguno
        self.df = None

        # Inicializar las clases auxiliares, pasando None para df inicialmente.
        # El df se actualizará en _update_all_dfs después de cargar los datos.
        self.loader = LoadData(df=self.df)
        self.preparer = DataPreparation(df=self.df)
        self.explorer = ExploratoryAnalysis(df=self.df)
        self.dist_analyzer = AnalisisDistribucion(df=self.df)
        self.rel_analyzer = RelationshipAnalysis(df=self.df)
        self.findings_reporter = KeyFindings(df=self.df)

    # Cargar datos utilizando la instancia LoadData y actualizar el DataFrame interno.
    def load_data(self, file_path):
        self.loader.load_data(file_path)
        self.df = self.loader.df # Actualizar el DataFrame principal
        # Pasar el DataFrame actualizado a todas las demás clases auxiliares
        self._update_all_dfs()
        print(f"Datos cargados desde {file_path}")

    # Método auxiliar para actualizar el DataFrame en todas las clases instanciadas.
    def _update_all_dfs(self):    
        self.preparer.df = self.df
        self.explorer.df = self.df
        self.dist_analyzer.df = self.df
        self.rel_analyzer.df = self.df
        self.findings_reporter.df = self.df

    # Realiza la limpieza de datos y la ingeniería de características.
    def prepare_data(self):    
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        self.df = self.preparer.clean_and_engineer_features()
        # Actualiza el DataFrame en todas las clases después de la preparación
        self._update_all_dfs() 
        print("Preparación de datos completa.")

    # Realiza un análisis exploratorio de datos.
    def explore_data(self, include_object_descriptive=False):    
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        self.explorer.check_info()
        self.explorer.check_missing_values()
        self.explorer.display_descriptive_statistics(include_object=include_object_descriptive)
        self.explorer.check_unique_values()
        print("Análisis exploratorio de datos completo.")

    # Analiza y visualiza la distribución de una columna específica.
    def analyze_distribution(self, column):    
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        self.dist_analyzer.analizar_distribucion(column)
        print(f"Análisis de distribución para '{column}' completo.")

    # Analiza la relación entre una columna categórica y una columna numérica.
    def analyze_relationships(self, categorical_col, numerical_col):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        self.rel_analyzer.analyze_categorical_numerical_relationship(categorical_col, numerical_col)
        print(f"Análisis de relación entre '{categorical_col}' y '{numerical_col}' completo.")

    # Analiza y visualiza las correlaciones entre las columnas de puntuación numéricas.
    def analyze_scores_correlations(self, numerical_cols=['math_score', 'reading_score', 'writing_score']):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        return self.rel_analyzer.analyze_correlations(numerical_cols)

    # Resume los hallazgos clave del análisis.
    def summarize_key_findings(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero usando load_data().")
            return
        self.findings_reporter.summarize_findings()
        print("Hallazgos clave resumidos.")