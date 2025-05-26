# librarias
import core.utils as ut

class AnalisisPromedioAcademicoAlimentacion:
    def __init__(self, df=None):
        self.df = df

    def mostrar_promedio_por_almuerzo(self):
        if self.df is None:
            print("DataFrame no cargado.")
            return

        if 'average_score' not in self.df.columns:
            self.df['average_score'] = self.df[['math score', 'reading score', 'writing score']].mean(axis=1)

        lunch_scores = self.df.groupby('lunch')[['math score', 'reading score', 'writing score', 'average_score']].mean()
        print("\nPromedio de calificaciones por tipo de almuerzo:")
        print(ut.tabulate(lunch_scores, headers='keys', tablefmt='fancy_grid', showindex=True))

        df_melted = ut.pd.melt(
            self.df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean().reset_index(),
            id_vars=['lunch'],
            value_vars=['math score', 'reading score', 'writing score']
        )

        ut.plt.figure(figsize=(12, 6))
        ut.sns.barplot(x='lunch', y='value', hue='variable', data=df_melted)
        ut.plt.title('Calificación Promedio por Tipo de Almuerzo', fontsize=16)
        ut.plt.xlabel('Tipo de Almuerzo')
        ut.plt.ylabel('Promedio de Calificación')
        ut.plt.legend(title='Asignatura', loc='center left', bbox_to_anchor=(1, 0.5))
        ut.plt.grid(True, axis='y')

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/calificaciones_tipo_almuerzo.png')
        ut.plt.show()
