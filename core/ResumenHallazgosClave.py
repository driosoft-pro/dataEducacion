from core.operaciones import Operaciones
        
class ResumenHallazgosClave:
    def __init__(self, df=None):
        self.df = df

    def mostrar_resumen(self, gender_scores, prep_scores, education_scores, correlation_matrix):
        if self.df is None:
            print("No data loaded.")
            return

        # Asegurar columna de promedio
        if 'average_score' not in self.df.columns:
            operar = Operaciones(self.df)
            self.df = operar.calcular_promedio()

        # Calcular correlaciones
        if correlation_matrix is not None:
            correlations = correlation_matrix.unstack()
            correlations = correlations[correlations.index.get_level_values(0) != correlations.index.get_level_values(1)]
            correlations_sorted = correlations.sort_values(ascending=False)
            highest_corr = correlations_sorted.iloc[0]
            highest_corr_vars = correlations_sorted.index[0]
        else:
            print("La matriz de correlación no está disponible.")
            highest_corr = None
            highest_corr_vars = (None, None)

        # Mostrar hallazgos
        print("\n=== HALLAZGOS CLAVE ===")
        if self.df is not None and 'average_score' in self.df.columns:
            promedio_global = self.df['average_score'].mean()
            print(f"1. La calificación promedio global es: {promedio_global:.2f}")
        else:
            print("1. No se pudo calcular la calificación promedio global (datos insuficientes).")

        if gender_scores is not None and not gender_scores.empty:
            # Asegura que 'gender' sea columna, no índice
            if 'gender' not in gender_scores.columns:
                gender_scores = gender_scores.reset_index()
            mejor_genero = gender_scores.loc[gender_scores['average_score'].idxmax(), 'gender']
            print(f"2. Género con mejor promedio: {mejor_genero}")
        else:
            print("2. No se pudo determinar el género con mejor promedio (datos insuficientes).")

        if education_scores is not None and not education_scores.empty:
            mejor_nivel = education_scores.index[0]
            print(f"3. Nivel educativo de padres con mejor promedio: {mejor_nivel}")
        else:
            print("3. No se pudo determinar el nivel educativo de padres con mejor promedio (datos insuficientes).")

        if prep_scores is not None and not prep_scores.empty:
            if 'completed' in prep_scores.index and 'none' in prep_scores.index:
                diferencia = prep_scores.loc['completed']['average_score'] - prep_scores.loc['none']['average_score']
                print(f"4. Diferencia en promedio entre estudiantes con curso de preparación y sin él: {diferencia:.2f}")
            else:
                print("4. No se encontraron ambos grupos ('completed' y 'none') para comparar.")
        else:
            print("4. No se pudo calcular la diferencia en promedio entre estudiantes con y sin curso de preparación (datos insuficientes).")

        if highest_corr_vars[0] and highest_corr_vars[1]:
            print(f"5. Correlación más alta entre asignaturas: {highest_corr_vars[0]} y {highest_corr_vars[1]} (r={highest_corr:.2f})")
