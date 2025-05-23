# libraries
import core.utils as ut

# classes
# classes
from .LoadData import LoadData
from .DataPreparation import DataPreparation
from .ExploratoryAnalysis import ExploratoryAnalysis
from .AnalisisDistribucion import AnalisisDistribucion
from .RelationshipAnalysis import RelationshipAnalysis
from .KeyFindings import KeyFindings
class DataAnalysis():
    # Initialize LoadData and AnalisisDistribucion objects
    def __init__(self, df=None):
        # El DataFrame principal que se utilizará en todas las operaciones
        self.df = df

        # Inicializar clases
        self.loader = LoadData(self.df)
        self.preparer = DataPreparation(self.df)
        self.explorer = ExploratoryAnalysis(self.df)
        self.dist_analyzer = AnalisisDistribucion(self.df)
        self.rel_analyzer = RelationshipAnalysis(self.df)
        self.findings_reporter = KeyFindings(self.df)

    # Cargue datos utilizando la instancia LoadData y actualice el DataFrame interno.
    def load_data(self, file_path):
        self.loader.load_data(file_path)
        self.df = self.loader.df # Update the main DataFrame
        # Pass the updated DataFrame to all other helper classes
        self._update_all_dfs()
        print(f"Data loaded from {file_path}")

    # Método auxiliar para actualizar el DataFrame en todas las clases instanciadas.
    def _update_all_dfs(self):    
        self.preparer.df = self.df
        self.explorer.df = self.df
        self.dist_analyzer.df = self.df
        self.rel_analyzer.df = self.df
        self.findings_reporter.df = self.df

    # Realiza la limpieza de datos y la ingeniería de características.
    def prepare_data(self):    
        self.df = self.preparer.clean_and_engineer_features()
        self._update_all_dfs() # Update after data preparation

    # Realiza un análisis exploratorio de datos.
    def explore_data(self, include_object_descriptive=False):    
        self.explorer.check_info()
        self.explorer.check_missing_values()
        self.explorer.display_descriptive_statistics(include_object=include_object_descriptive)
        self.explorer.check_unique_values()

    # Analiza y visualiza la distribución de una columna específica.
    def analyze_distribution(self, column):    
        self.dist_analyzer.analizar_distribucion(column)

    # Analiza la relación entre una columna categórica y una columna numérica.
    def analyze_relationships(self, categorical_col, numerical_col):
        self.rel_analyzer.analyze_categorical_numerical_relationship(categorical_col, numerical_col)

    # Analiza y visualiza las correlaciones entre las columnas de puntuación numéricas.
    def analyze_scores_correlations(self, numerical_cols=['math_score', 'reading_score', 'writing_score']):
        return self.rel_analyzer.analyze_correlations(numerical_cols)

    # Resume los hallazgos clave del análisis.
    def summarize_key_findings(self):
        self.findings_reporter.summarize_findings()