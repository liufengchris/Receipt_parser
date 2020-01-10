import csv
import glob
import sys
import ocr

if __name__ == '__main__':

# list down all png image files in the current working directory
	image_file_list = []
	for image in glob.glob("*.png"):
		image_file_list.append(image)

# run ocr function to parse date_price value pair in dict
	ocr_dict = dict()
	for image_file in image_file_list:
		ocr_dict.update(ocr.ocr_fun(image_file))
		
	print(ocr_dict)

	with open('ocr_csv.csv', 'w') as file_to_write:
		dict_writer = csv.DictWriter(file_to_write, ocr_dict.keys())
		dict_writer.writeheader()
		#dict_writer.writerows(ocr_dict)