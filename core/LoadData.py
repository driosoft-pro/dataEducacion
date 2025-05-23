# librarias
import core.utils as ut

class LoadData:
    def __init__(self):
        self.df = None

    def load_data(self, file_path):
        self.df = ut.pd.read_csv(file_path)
        return self.df
    
    def load_data_not_head(self, file_path):
        self.dfnh = ut.pd.read_csv(file_path, header=None)
        return self.dfnh