import utils as ut

class AnalisisDistribucion():
    def __init__(self, df=None):
        self.df = df

    def analizar_distribucion(self, column):
            """
            Analyze the distribution of a given column.
            """
            if self.df is None:
                # Verificar si la columna existe en el DataFrame
                print("No data loaded.")
                return
            elif column not in self.df.columns:
                print(f"La columna '{column}' no existe en el DataFrame.")
                return
            elif self.df[column].dtype not in ['int64', 'float64']:
                print(f"La columna '{column}' no es numérica.")
                return
            elif self.df[column].isnull().sum() > 0:
                # Verificar si la columna tiene valores nulos
                print(f"La columna '{column}' contiene valores nulos.")
                return
            else:
                ut.plt.figure(figsize=(15,6))
                atribute = column
                num_bins = 20
                ut.sns.histplot(data     = self.df,
                            x        = atribute,
                            bins     = num_bins,
                            color    = 'red',
                            fill     = True,
                            stat     = 'count')    #'count' muestra el número de observaciones.
                                                    #'frequency' muestra el número de observaciones dividida por el ancho del bin.
                                                    #'density' normaliza las cuentas tal que el área del histograma es 1.
                                                    #'probability' normaliza las cuentas tal que la suma de la altura de las barras es 1.

                ut.plt.xlabel(atribute) #Texto en el eje x.
                ut.plt.ylabel('Cuentas')              #Texto en el eje y.
                ut.plt.title(f'Distribución de la variable {column}')             #Título del gráfico.
                ut.plt.xticks(rotation=45, fontsize=8)
                ut.plt.show()