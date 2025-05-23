import utils as ut

class LoadData():
    def __init__(self, df=None):
        self.df = df

    def load_data(self, file_path):
        """
        Load data from a CSV file.
        """
        self.df = ut.pd.read_csv(file_path)