import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tabulate

sns.set_theme(style="whitegrid")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class DataAnalysis():
    def __init__(self, df=None):
        self.df = df

    def load_data(self, file_path):
        """
        Load data from a CSV file.
        """
        self.df = pd.read_csv(file_path)

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
            plt.figure(figsize=(15,6))
            atribute = column
            num_bins = 20
            sns.histplot(data     = self.df,
                        x        = atribute,
                        bins     = num_bins,
                        color    = 'red',
                        fill     = True,
                        stat     = 'count')    #'count' muestra el número de observaciones.
                                                #'frequency' muestra el número de observaciones dividida por el ancho del bin.
                                                #'density' normaliza las cuentas tal que el área del histograma es 1.
                                                #'probability' normaliza las cuentas tal que la suma de la altura de las barras es 1.

            plt.xlabel(atribute) #Texto en el eje x.
            plt.ylabel('Cuentas')              #Texto en el eje y.
            plt.title(f'Distribución de la variable {column}')             #Título del gráfico.
            plt.xticks(rotation=45, fontsize=8)
            plt.show()
            

    
               

