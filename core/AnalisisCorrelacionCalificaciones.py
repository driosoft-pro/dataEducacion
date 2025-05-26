# librarias
import core.utils as ut

class AnalisisCorrelacionCalificaciones:
    def __init__(self, df=None):
        self.df = df

    def mostrar_matriz_correlacion(self):
        if self.df is None:
            print("No se ha proporcionado un DataFrame.")
            return

        correlation = self.df[['math score', 'reading score', 'writing score']].corr()

        ut.plt.figure(figsize=(10, 6))
        ut.sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=0.5, vmax=1)
        ut.plt.title('Matriz de Correlación entre Calificaciones', fontsize=16)
        ut.plt.tight_layout()

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/matriz_correlacion_calificaciones.png')
        ut.plt.show()

        print("\nMatriz de correlación:")
        print(correlation)
        return correlation
