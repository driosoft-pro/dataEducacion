# librarias
import core.utils as ut

class LimpiaValida:
    def __init__(self, df=None):
        self.df = df
        
    def validar_observaciones_atributos(self):
        if self.df is None:
            print("No hay datos para verificar las observaciones yatributos.")
            return

        print(f"El número de observaciones es: {self.df.shape[0]}")
        print(f"El número de atributos es: {self.df.shape[1]}")

    def validar_datos(self):
        if self.df is None:
            print("No hay datos para verificar los datos.")
            return

        print("Primeras filas:")
        print(self.df.head())
        print("\nUltimas filas:")
        print(self.df.tail())
        
    def validar_nombres(self):
        if self.df is None:
            print("No hay datos para verificar los nombres.")
            return

        print("Nombres de las columnas:")
        print(self.df.columns)

    def validar_tipos(self):
        if self.df is None:
            print("No hay datos para verificar los tipos.")
            return

        print("Tipos de datos:")
        print(self.df.dtypes)
        
    def validar_informacion(self):
        if self.df is None:
            print("No hay datos para verificar la información.")
            return

        print("Forma del DataFrame:", self.df.shape)
        print("\nPrimeras 5 filas:")
        print(self.df.head())
        print("\nInformación del DataFrame:")
        self.df.info()
        print("\nEstadísticas descriptivas:")
        print(self.df.describe())

    def validar_descriptivos(self):
        if self.df is None:
            print("No hay datos para verificar los descriptivos.")
            return

        print("Estadísticas descriptivas:")
        print(self.df.describe())
        
    def renombrar_columnas(self):
        if self.df is None:
            print("No hay datos para extraer nombres de columnas.")
            return
        
        self.headers = list(self.df.columns)
        print("Nombres de columnas actuales almacenados en 'self.headers':")
        print(self.headers)
        
    def validar_nulos(self):
        if self.df is None:
            print("No hay datos para contar nulos.")
            return

        print("Cantidad de valores nulos por columna:")
        print(self.df.isnull().sum())

    def validar_porcentaje_nulos(self):
        if self.df is None:
            print("No hay datos para calcular el porcentaje de nulos.")
            return

        print("Porcentaje de valores nulos por columna:")
        print(self.df.isnull().mean() * 100)

    def contar_duplicados(self):
        if self.df is None:
            print("No hay datos para contar duplicados.")
            return

        print("Cantidad de duplicados:")
        print(self.df.duplicated().sum())

    def eliminar_duplicados(self):
        if self.df is None:
            print("No hay datos para eliminar duplicados.")
            return

        self.df.drop_duplicates(inplace=True)
        
    def valor_atipico(self):
        if self.df is None:
            print("No hay datos para encontrar el valor atípico.")
            return

        print("Valores atípicos:")
        print(self.df.describe(percentiles=[0.01, 0.99]))
        
    def copiar_df(self):
        if self.df is None:
            print("No hay datos para crear una nueva copia.")
            return

        return self.df.copy()

    def actualizar_col_objeto(self, col, nuevo_valor):
        if self.df is None:
            print("No hay datos para actualizar la columna.")
            return

        self.df[col] = nuevo_valor

    def datos_df(self):
        if self.df is None:
            print("No hay datos para obtener.")
            return

        ## ¿De qué tamaño es el nuevo dataframe?
        print(self.df.shape)
        ## ¿Cuántas filas se eliminaron?
        print(f"Se eliminaron {self.df.shape[0] - self.df.shape[0]} filas")
        ## Porcentaje de filas eliminadas
        porcentaje = 100*(self.df.shape[0] - self.df.shape[0])/self.df.shape[0]
        print(f"El porcentaje de filas eliminadas es: {porcentaje:.2f}%")
            
    def limpiar(self):
        if self.df is None:
            print("No hay datos para limpiar.")
            return

        # Eliminar columnas con más del 50% de nulos
        threshold = 0.5 * len(self.df)
        cols_antes = self.df.shape[1]
        self.df = self.df.dropna(thresh=threshold, axis=1)
        cols_despues = self.df.shape[1]
        print(f"Columnas eliminadas por nulos: {cols_antes - cols_despues}")

        # Imputar valores nulos en numéricas con la mediana
        num_cols = self.df.select_dtypes(include=['float64', 'int64']).columns
        for col in num_cols:
            if self.df[col].isnull().any():
                mediana = self.df[col].median()
                self.df[col].fillna(mediana, inplace=True)
                print(f"Valores nulos en '{col}' imputados con la mediana ({mediana})")

        print("Datos limpios (primeras filas):")
        print(self.df.head())