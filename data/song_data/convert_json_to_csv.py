import json
import pandas as pd
import os

def convert_json_to_csv(files_path, output_file_name):
	data_rows_dic = []
	for file_path in files_path:	
		with open(file_path, 'r', encoding='utf-8') as file:
			j_file = json.load(file)
			data_rows_dic.append(j_file)
			
	df = pd.DataFrame()
	for row in data_rows_dic:
		df = df.append(row, ignore_index=True)
	
	df.to_csv(output_file_name, index= False, encoding='utf-8')
	print("Success")
	
def get_all_file_paths(root):
	file_names = []
	for root, dirs, files in os.walk("."):
		for name in files:
			abs_path = os.path.join(root, name)
			if ".json" in abs_path:
				file_names.append(abs_path)
	
	return file_names
			
		
if __name__ == "__main__":
	root_dir = os.getcwd()
	all_files_list = get_all_file_paths(root_dir)
	convert_json_to_csv(all_files_list, "Songs_Data.csv")


