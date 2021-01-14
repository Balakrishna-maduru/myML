class FeatureSelection:
    def __init__(self, df, key):
        self.df = df
        self.key = key

    def transform(self):
        self._remove_non_varying_columns(1)
        self._remove_all_nan_rows()
        self._remove_non_varying_rows()
        self.df.reset_index(drop=True)
        return self.df

    def _remove_non_varying_columns(self, distinct_values_threshold):
        columns = [c for c in list(self.df) if len(self.df[c].unique()) > distinct_values_threshold]
        self.df = self.df[columns]
    
    def _remove_all_nan_rows(self):
        columns = list(self.df.columns)
        columns.remove(self.key)
        self.df = self.df.dropna(subset=columns, how='all')

    def _remove_non_varying_rows(self,condition_value = 0,):
        condition, and_flag = "", ""
        columns = list(self.df.columns)
        columns.remove(self.key)
        for column in columns:
            condition =  f'{condition}{and_flag}(self.df.{column} > {condition_value})'
            and_flag = " | "
        self.df = eval(f'self.df[{condition}]')
