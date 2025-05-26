# librarias
import core.utils as ut

class RendimientoGrupoEtnico:
    def __init__(self, df=None):
        self.df = df

    def graficar_rendimiento_etnico(self):
        if self.df is None:
            print("No se ha cargado un DataFrame.")
            return

        df_melted = ut.pd.melt(
            self.df,
            id_vars=['race/ethnicity'],
            value_vars=['math score', 'reading score', 'writing score']
        )

        ut.plt.figure(figsize=(14, 8))
        ut.sns.violinplot(
            x='race/ethnicity',
            y='value',
            hue='variable',
            data=df_melted,
            inner='quartile',
            palette='Set3'
        )
        ut.plt.title('Rendimiento por Grupo Étnico', fontsize=16)
        ut.plt.xlabel('Grupo Étnico')
        ut.plt.ylabel('Calificación')
        ut.plt.legend(title='Asignatura', loc='center left', bbox_to_anchor=(1, 0.5))
        ut.plt.grid(True, axis='y')
        ut.plt.tight_layout()

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/rendimiento_grupo_etnico.png')
        ut.plt.show()

    def mostrar_estadisticas_etnicas(self):
        if self.df is None or 'race/ethnicity' not in self.df.columns:
            print("DataFrame no válido o columna 'race/ethnicity' no encontrada.")
            return

        if 'average_score' not in self.df.columns:
            self.df['average_score'] = self.df[['math score', 'reading score', 'writing score']].mean(axis=1)

        ethnicity_scores = self.df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score', 'average_score']].mean()
        ethnicity_scores = ethnicity_scores.sort_values('average_score', ascending=False)

        print("\nPromedio de calificaciones por grupo étnico:")
        print(ut.tabulate(ethnicity_scores, headers='keys', tablefmt='fancy_grid', showindex=True))

        return ethnicity_scores
