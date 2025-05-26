# librarias
import core.utils as ut

class Operaciones:
    def __init__(self, df=None):
        self.df = df    

    def calcular_promedio(self):
        if self.df is None:
            print("DataFrame no ha sido inicializado.")
            return
        self.df['average_score'] = (
            self.df['math score'] +
            self.df['reading score'] +
            self.df['writing score']
        ) / 3
        return self.df

    def obtener_gender_scores(self):
        if self.df is None:
            print("DataFrame no ha sido inicializado.")
            return
        return self.df.groupby('gender')[
            ['math score', 'reading score', 'writing score', 'average_score']
        ].mean().reset_index()

    def obtener_prep_scores(self):
        if self.df is None:
            print("DataFrame no ha sido inicializado.")
            return
        return self.df.groupby('test preparation course')[
            ['math score', 'reading score', 'writing score', 'average_score']
        ].mean()

    def obtener_education_scores(self):
        if self.df is None:
            print("DataFrame no ha sido inicializado.")
            return
        return self.df.groupby('parental level of education')[
            'average_score'
        ].agg(['mean', 'median', 'std']).sort_values('mean', ascending=False)

    def obtener_matriz_correlacion(self):
        if self.df is None:
            print("DataFrame no ha sido inicializado.")
            return
        return self.df[['math score', 'reading score', 'writing score']].corr()
