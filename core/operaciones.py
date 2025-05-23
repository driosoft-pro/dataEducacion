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