import sys

if __name__ == '__main__':
	
	survey_key =  "MSISDN"
	file_name = r"E:\my_work\data\nei_data\2020\CEI_O_INDEX_DAY_11_perc_kpi.csv"
	feature_selection = FeatureSelection(data,survey_key)
	data = feature_selection.transform()
	data_impute = DataImpute(data, survey_key)
	data = data_impute.fill_na('mean')
