import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tabulate
from LoadData import LoadData
from AnalizarDistribucion import AnalisisDistribucion

sns.set_theme(style="whitegrid")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

class DataAnalysis():
    def __init__(self, df=None):
        self.df = df

    LoadData()
    #def load_data(self, file_path):
        #"""
        #Load data from a CSV file.
        #"""
        #self.df = pd.read_csv(file_path)

    AnalisisDistribucion()
            


