import csv
import json
import glob
import sys
import ocr

if __name__ == '__main__':

# list down all png image files in the current working directory
	image_file_list = []
	for image in glob.glob("*.png"):
		image_file_list.append(image)

# run ocr function to parse date_price value pair in json txt
	for image_file in image_file_list:
		ocr.ocr_fun(image_file)
