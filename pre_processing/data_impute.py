'''
Created on 10-Dec-2020

@author: Maduru Balakrishna
'''
import sys
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from impyute.imputation.cs import mice


class DataImpute:

    def __init__(self, data, key=[]):
        self.data = data
        self.key = key

    def fill_na(self, impute_type="mean", k_samples=30):
        if impute_type == 'mean':
            imputer=SimpleImputer(missing_values=np.nan , strategy='mean')
        elif impute_type == 'most_frequent':
            imputer=SimpleImputer(missing_values=np.nan , strategy='most_frequent')
        elif impute_type == 'median':
            imputer=SimpleImputer(missing_values=np.nan , strategy='median')
        elif impute_type == 'knn':
            return self.KNN(self.data, k_samples)
        elif impute_type == 'multi_variate':
            return self.Multivariate(self.data)
        
        imputer.fit(self.data.iloc[:, 1:])
        self.data.iloc[:,1:]=imputer.transform(self.data.iloc[:,1:])        
        return self.data
        
    def KNN(self, data, k_samples=30):
        imputer = KNNImputer(n_neighbors=3, weights="uniform")
        return imputer.fit_transform(data)
    
    def Multivariate(self, data):
        return mice(data.values)
