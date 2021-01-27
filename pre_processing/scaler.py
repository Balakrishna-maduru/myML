import pandas as pd
from sklearn import preprocessing
class Scaler:

    def __init__(self, type_of_scaler = "min_max_scaler", quantile_range = (0.1,0.9)):
        if type_of_scaler == "min_max_scaler":
            self.scaler = preprocessing.MinMaxScaler()
        elif type_of_scaler == "standard_scaler":
            self.scaler = preprocessing.StandardScaler()
        elif type_of_scaler == "max_abs_scaler":
            self.scaler = preprocessing.MaxAbsScaler()
        elif type_of_scaler == "robust_scaler":
            self.scaler = preprocessing.RobustScaler()
        elif type_of_scaler == "robust_scaler":
            self.scaler = preprocessing.RobustScaler()

    def scale(self, df, key):
        key_id = df[key]
        column_names = df.columns
        df.drop(key, axis=1, inplace=True)
        df = self.do_scaling_df(df)
        df = pd.concat([key_id, df], axis=1)
        df.columns = column_names
        return df

    def do_scaling_df(self, dataDf):
        x_scaled = self.do_scaling_series(dataDf)
        return pd.DataFrame(x_scaled)

    def do_scaling_series(self, dataDf):
        x = dataDf.values
        return self.scaler.fit_transform(x)

if __name__ == "__main__":
    df1 = scale(df, "MSISDN")
    df1.describe()
