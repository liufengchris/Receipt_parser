import csv
import glob
import sys
import ocr
import pandas as pd

if __name__ == '__main__':

# list down all png image files in the current working directory
	image_file_list = []
	for image in glob.glob("*.png"):
		image_file_list.append(image)

# run ocr function to parse date_price value pair in dict
	ocr_dict = dict()
	for image_file in image_file_list:
		ocr_dict.update(ocr.ocr_fun(image_file))

# convert the ocr_dict into pandas dataframe with index as orientation
	ocr_df = pd.DataFrame.from_dict(ocr_dict, orient='index')

# convert datafram into csv file
	ocr_df.to_csv('ocr.csv')