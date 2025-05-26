# librarias
import core.utils as ut

class AnalisisPromedioGeneroBajaAlimentacion:
    def __init__(self, df=None):
        self.df = df

    def analizar_promedio_baja_alimentacion(self):
        if self.df is None or 'gender' not in self.df.columns or 'lunch' not in self.df.columns or 'average_score' not in self.df.columns:
            print("DataFrame no válido o columnas faltantes.")
            return

        # Agrupar y calcular el promedio
        gender_lunch_scores = self.df.groupby(['gender', 'lunch'])['average_score'].mean().reset_index()

        # Mostrar tabla
        print("\nPromedio de calificaciones por género y tipo de almuerzo:")
        print(ut.tabulate(gender_lunch_scores, headers='keys', tablefmt='fancy_grid', showindex=False))

        # Gráfico
        ut.plt.figure(figsize=(12, 6))
        ut.sns.barplot(
            x='gender',
            y='average_score',
            hue='lunch',
            data=gender_lunch_scores,
            palette='Set2'
        )
        ut.plt.title('Promedio de Calificaciones por Género y Tipo de Almuerzo', fontsize=16)
        ut.plt.xlabel('Género')
        ut.plt.ylabel('Promedio de Calificaciones')
        ut.plt.legend(title='Tipo de Almuerzo', loc='center left', bbox_to_anchor=(1, 0.5))
        ut.plt.grid(True, axis='y')

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/calificaciones_genero_almuerzo.png')
        ut.plt.show()

        return gender_lunch_scores
