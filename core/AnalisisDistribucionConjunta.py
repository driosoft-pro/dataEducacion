# librarias
import core.utils as ut

class AnalisisDistribucionConjunta:
    def __init__(self, df=None):
        self.df = df

    def generar_graficos(self):
        if self.df is None:
            print("No data loaded.")
            return

        # Gráfico hexbin: Matemáticas vs Escritura
        g1 = ut.sns.jointplot(
            x='math score',
            y='writing score',
            data=self.df,
            kind='hex',
            height=10,
            cmap='viridis'
        )
        g1.fig.suptitle('Distribución Conjunta entre Matemáticas y Escritura', y=1.02, fontsize=16)
        ut.plt.tight_layout()
        if not ut.os.path.exists('img'):
            ut.os.makedirs('img')
        ut.plt.savefig('img/distribucion_conjunta_matematicas_escritura.png')
        ut.plt.show()

        # Gráfico scatter: Matemáticas vs Lectura
        g2 = ut.sns.jointplot(
            x='math score',
            y='reading score',
            data=self.df,
            kind='scatter',
            height=10,
            color='purple',
            alpha=0.6
        )
        g2.fig.suptitle('Distribución Conjunta entre Matemáticas y Lectura', y=1.02, fontsize=16)
        ut.plt.tight_layout()
        ut.plt.savefig('img/distribucion_conjunta_matematicas_lectura.png')
        ut.plt.show()