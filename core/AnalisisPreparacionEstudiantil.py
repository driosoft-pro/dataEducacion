# librarias
import core.utils as ut

class AnalisisPreparacionEstudiantil:
    def __init__(self, df=None):
        self.df = df

    def graficar_resultados_preparacion(self):
        if self.df is None:
            print("No data loaded.")
            return

        df_melted = ut.pd.melt(
            self.df,
            id_vars=['test preparation course'],
            value_vars=['math score', 'reading score', 'writing score']
        )

        ut.plt.figure(figsize=(14, 8))
        ut.sns.boxplot(x='test preparation course', y='value', hue='variable', data=df_melted)
        ut.plt.title('Resultados por Curso de Preparación', fontsize=16)
        ut.plt.xlabel('Curso de Preparación')
        ut.plt.ylabel('Calificación')
        ut.plt.legend(title='Asignatura', loc='center left', bbox_to_anchor=(1, 0.5))
        ut.plt.grid(True, axis='y')
        ut.plt.tight_layout()
        
        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/inivel_educativo_padres.png')
        ut.plt.show()

    def mostrar_estadisticas_preparacion(self):
        if self.df is None or 'test preparation course' not in self.df.columns:
            print("DataFrame no válido o columna 'test preparation course' no encontrada.")
            return

        if 'average_score' not in self.df.columns:
            self.df['average_score'] = self.df[['math score', 'reading score', 'writing score']].mean(axis=1)

        prep_scores = self.df.groupby('test preparation course')[['math score', 'reading score', 'writing score', 'average_score']].mean()
        print("\nPromedio de calificaciones por curso de preparación:")
        print(ut.tabulate(prep_scores, headers='keys', tablefmt='fancy_grid', showindex=True))
        return prep_scores