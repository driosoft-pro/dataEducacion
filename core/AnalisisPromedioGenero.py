# librarias
import core.utils as ut

class AnalisisPromedioGenero:
    def __init__(self, df=None):
        self.df = df

    def mostrar_promedio_genero(self):
        if self.df is None:
            print("DataFrame no cargado.")
            return

        gender_scores = self.df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().reset_index()
        print("\nPromedio de calificaciones por género:")
        print(ut.tabulate(gender_scores.values, headers=list(gender_scores.columns), tablefmt='fancy_grid', showindex=False))

        df_melted = ut.pd.melt(gender_scores, id_vars=['gender'], value_vars=['math score', 'reading score', 'writing score'])

        ut.plt.figure(figsize=(12, 6))
        ut.sns.barplot(x='gender', y='value', hue='variable', data=df_melted)
        ut.plt.title('Promedio de Calificaciones por Género', fontsize=16)
        ut.plt.xlabel('Género')
        ut.plt.ylabel('Promedio de Calificación')
        ut.plt.legend(title='Asignatura', loc='center left', bbox_to_anchor=(1, 0.5))
        ut.plt.grid(True, axis='y')

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/calificaciones_por_genero.png')
        ut.plt.show()
