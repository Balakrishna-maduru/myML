from sklearn import preprocessing
class Scaler:

    def __init__(self, type_of_scaler = "min_max_scaler"):
        if type_of_scaler == "min_max_scaler":
            self.scaler = preprocessing.MinMaxScaler()

    def scale(self, df, key):
        key_id = df[key]
        column_names = df.columns
        df.drop(key, axis=1, inplace=True)
        df = do_scaling_df(df)
        df = pd.concat([key_id, df], axis=1)
        df.columns = column_names
        return df

    def do_scaling_df(self, dataDf):
        x_scaled = do_scaling_series(dataDf)
        return pd.DataFrame(x_scaled)

    def do_scaling_series(self, dataDf):
        x = dataDf.values
        return self.scaler.fit_transform(x)

if __name__ == "__main__":
    df1 = scale(df, "MSISDN")
    df1.describe()
