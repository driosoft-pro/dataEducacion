# librarias
import core.utils as ut

class AnalisisCalificacion:
    def __init__(self, df=None):
        self.df = df

    def analizar_rendimiento(self):
        if self.df is None:
            print("No se ha cargado un DataFrame.")
            return

        # Filtrar estudiantes con >90 en todas las asignaturas
        high_achievers = self.df[
            (self.df['math score'] > 90) &
            (self.df['reading score'] > 90) &
            (self.df['writing score'] > 90)
        ]
        percentage = (len(high_achievers) / len(self.df)) * 100

        print(f"\nPorcentaje de estudiantes con más de 90 puntos en las tres asignaturas: {percentage:.2f}%")

        # Gráfico de pastel
        ut.plt.figure(figsize=(10, 8))
        labels = ['>90 en las tres asignaturas', 'No cumple criterio']
        sizes = [percentage, 100 - percentage]
        colors = ['#66b3ff', '#ffcc99']
        explode = (0.1, 0)

        ut.plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            shadow=True
        )
        ut.plt.axis('equal')
        ut.plt.title('Porcentaje de Estudiantes con más de 90 puntos en las tres asignaturas', fontsize=16)
        ut.plt.tight_layout()

        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')

        ut.plt.savefig('img/estudiantes_alto_rendimiento.png')
        ut.plt.show()

        return percentage
