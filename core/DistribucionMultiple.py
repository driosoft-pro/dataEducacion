# librarias
import core.utils as ut

class DistribucionMultiple:
    def __init__(self, df=None):
        self.df = df

    def analizar(self, columns):
        if self.df is None:
            print("No data loaded.")
            return

        # Validaciones:
        valid_columns = []
        for col in columns:
            if col not in self.df.columns:
                print(f"Columna '{col}' no encontrada en el DataFrame. Se omitirá.")
            elif self.df[col].dtype not in ['int64', 'float64']:
                print(f"Columna '{col}' no es numérica. Se omitirá.")
            elif self.df[col].isnull().sum() > 0:
                print(f"Columna '{col}' contiene valores nulos. Se omitirá.")
            else:
                valid_columns.append(col)

        if not valid_columns:
            print("No hay columnas válidas para graficar.")
            return

        n = len(valid_columns)
        fig, axes = ut.plt.subplots(1, n, figsize=(6*n, 6))
        if n == 1:
            axes = [axes]

        fig.suptitle('Distribución de Calificaciones', fontsize=16)
        colors = ['blue', 'green', 'red', 'orange', 'purple']

        for i, col in enumerate(valid_columns):
            ut.sns.histplot(x=self.df[col], kde=True, color=colors[i % len(colors)], ax=axes[i])
            axes[i].set_title(f'Distribución de {col}')
            axes[i].set_xlabel('Calificación')
            axes[i].set_ylabel('Frecuencia')

        ut.plt.tight_layout()
        ut.plt.subplots_adjust(top=0.9)

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/distribucion_calificaciones.png')
        ut.plt.show()
 
        print("\nEstadísticas descriptivas:")
        stats = self.df[valid_columns].describe()
        print(ut.tabulate(stats.values, headers=list(stats.columns), showindex=list(stats.index), tablefmt='fancy_grid'))