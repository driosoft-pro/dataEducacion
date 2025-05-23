# libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tabulate
from tabulate import tabulate

# Configuraciones iniciales
sns.set_theme(style="whitegrid")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class Utils:
    # Inicializar df como Ninguno o con un DataFrame proporcionado
    def __init__(self, df=None):
        self.df = df