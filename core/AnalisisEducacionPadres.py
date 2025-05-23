# librarias
import core.utils as ut

from core.operaciones import Operaciones

class AnalisisEducacionPadres:
    def __init__(self, df=None):
        self.df = df
        self.operar = Operaciones()

    def educacion_padres(self):
        if self.df is None:
            print("No data loaded.")
            return
        self.operar.calcular_promedio()
 
        # Estadísticas por nivel educativo de los padres
        ut.plt.figure(figsize=(14, 8))
        ut.sns.boxplot(
            x='parental level of education',
            y='average_score',
            hue='parental level of education',
            data=self.df,
            palette='viridis',
            legend=False
        )
        ut.plt.title('Influencia del Nivel Educativo de los Padres en el Promedio de Calificaciones', fontsize=16)
        ut.plt.xlabel('Nivel Educativo de los Padres')
        ut.plt.ylabel('Promedio de Calificaciones')
        ut.plt.xticks(rotation=45)
        ut.plt.grid(True, axis='y')
        ut.plt.tight_layout()
        
        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/inivel_educativo_padres.png')
        ut.plt.show()

        education_scores = self.df.groupby('parental level of education')['average_score'].agg(['mean', 'median', 'std']).sort_values('mean', ascending=False)
        print("\nEstadísticas por nivel educativo de los padres:")
        print(ut.tabulate(education_scores, headers='keys', tablefmt='fancy_grid', showindex=True))
