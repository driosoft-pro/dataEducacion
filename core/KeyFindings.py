# libraries
import core.utils as ut

class KeyFindings():
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df 

    # Resume los hallazgos clave de los datos de rendimiento estudiantil. Se asume que la puntuación promedio ya está diseñada.
    def summarize_findings(self):
        if self.df is None:
            print("No hay datos cargados. Por favor, cargue los datos primero.")
            return
        if 'average_score' not in self.df.columns:
            print("Por favor, ejecute la preparación de datos para crear 'average_score' primero.")
            return

        # 1. Puntuación media general
        overall_avg_score = self.df['average_score'].mean()

        # 2. énero con mejor promedio
        gender_scores = self.df.groupby('gender')['average_score'].mean().sort_values(ascending=False)
        best_gender = gender_scores.index[0]

        # 3. Nivel educativo de padres con mejor promedio
        education_scores = self.df.groupby('parental_level_of_education')['average_score'].mean().sort_values(ascending=False)
        best_education = education_scores.index[0]

        # 4. Diferencia en promedio entre estudiantes con y sin preparación para el examen
        prep_scores = self.df.groupby('test_preparation_course')['average_score'].mean()
        if 'completed' in prep_scores.index and 'none' in prep_scores.index:
            prep_course_diff = prep_scores.loc['completed'] - prep_scores.loc['none']
        else:
            prep_course_diff = "N/A (test_preparation_course categories not found)"

        # 5. Correlación más alta entre asignaturas
        numerical_scores = ['math_score', 'reading_score', 'writing_score']
        correlation_matrix = self.df[numerical_scores].corr()
        correlations = correlation_matrix.unstack()
        correlations = correlations[correlations.index.get_level_values(0) != correlations.index.get_level_values(1)]
        correlations_sorted = correlations.sort_values(ascending=False)
        highest_corr = correlations_sorted.iloc[0]
        highest_corr_vars = correlations_sorted.index[0]

        print("\n=== HALLAZGOS CLAVE ===")
        print(f"1. La calificación promedio global es: {overall_avg_score:.2f}")
        print(f"2. Género con mejor promedio: {best_gender} ({gender_scores.iloc[0]:.2f})")
        print(f"3. Nivel educativo de padres con mejor promedio: {best_education} ({education_scores.iloc[0]:.2f})")
        print(f"4. Diferencia en promedio entre estudiantes con curso de preparación y sin él: {prep_course_diff:.2f}" if isinstance(prep_course_diff, (int, float)) else f"4. {prep_course_diff}")
        print(f"5. Correlación más alta entre asignaturas: {highest_corr_vars[0]} y {highest_corr_vars[1]} (r={highest_corr:.2f})")