# libraries
import utils as ut

class RelationshipAnalysis:
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df

    # Analyzes the relationship between a categorical and a numerical column by plotting boxplots and calculating group means.
    def analyze_categorical_numerical_relationship(self, categorical_col, numerical_col, title_prefix=""):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        if categorical_col not in self.df.columns or numerical_col not in self.df.columns:
            print(f"Las columnas '{categorical_col}' o '{numerical_col}' no se encontraron.")
            return
        if self.df[numerical_col].dtype not in ['int64', 'float64']:
            print(f"La columna '{numerical_col}' no es numérica.")
            return

        print(f"\n--- Análisis de {categorical_col} vs {numerical_col} ---")
        group_scores = self.df.groupby(categorical_col)[numerical_col].mean().sort_values(ascending=False)
        print(f"Promedio de {numerical_col} por {categorical_col}:\n{group_scores}")

        ut.plt.figure(figsize=(10, 6))
        ut.sns.boxplot(x=categorical_col, y=numerical_col, data=self.df)
        ut.plt.title(f"{title_prefix} Distribución de {numerical_col} por {categorical_col}")
        ut.plt.xlabel(categorical_col)
        ut.plt.ylabel(numerical_col)
        ut.plt.xticks(rotation=45)
        ut.plt.show()

    # Calculates and visualizes the correlation matrix for given numerical columns.
    def analyze_correlations(self, numerical_cols):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        for col in numerical_cols:
            if col not in self.df.columns or self.df[col].dtype not in ['int64', 'float64']:
                print(f"La columna '{col}' no es numérica o no existe.")
                return

        print("\n--- Matriz de Correlación ---")
        correlation_matrix = self.df[numerical_cols].corr()
        print(correlation_matrix)

        ut.plt.figure(figsize=(8, 6))
        ut.sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        ut.plt.title('Matriz de Correlación de Puntajes')
        ut.plt.show()
        return correlation_matrix