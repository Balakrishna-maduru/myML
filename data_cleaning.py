import sys
from pre_processing.read_data import ReadData
from pre_processing.scaler import Scaler
from pre_processing.data_impute import DataImpute
from pre_processing.feature_selection import FeatureSelection

if __name__ == '__main__':

	survey_key =  "MSISDN"
	file_name = r"E:\my_work\data\nei_data\2020\CEI_O_INDEX_DAY_11_perc_kpi.csv"

	read_data = ReadData()
	data = read_data.read(file_name)

	print(data)

	feature_selection = FeatureSelection(data,survey_key)
	data = feature_selection.transform()

	data_impute = DataImpute(data, survey_key)
	data = data_impute.fill_na('mean')

	scaler = Scaler("min_max_scaler")
	df = scaler.scale(data)
	print(data[1])