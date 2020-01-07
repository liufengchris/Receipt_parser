from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
from datetime import datetime
import json
import sys

def ocr_fun(image_file):

	# load the example image and convert it to grayscale
	image = cv2.imread(image_file)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# apply thresholding to preprocess the image
	gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	# make a check to see if median blurring should be done to remove
	# noise
	#elif args["preprocess"] == "blur":
	#    gray = cv2.medianBlur(gray, 3)

	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	ocr_text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)

	# set a dict object to return


	# use regex to find the date
	date_pattern_DDMMMYY = "[\d]{1,2} [ADFJMNOS]\w* [\d]{2}"
	date_pattern_DDMMMYYYY = "[\d]{1,2} [ADFJMNOS]\w* [\d]{4}"

	date_DDMMMYY = re.search(date_pattern_DDMMMYY, ocr_text)
	if date_DDMMMYY:
	# convert the string into standard datetime object
		date_formatted = datetime.strptime(date_DDMMMYY.group(0), '%d %b %y')
		print (date_formatted.date())
	else:
		print("no date!")


	# use regex to find the price
	price_pattern = "[\d]{1,2}\.[\d]{2}"

	prices = re.findall(price_pattern, ocr_text)
	if prices:
		print (max(prices))
	else:
		print("no price!")

	# store the value pair in json format file
	date_price_dict = {str(date_formatted.date()):max(prices)}
	with open('ocr_text_json.txt', 'a') as file_to_write:
			json.dump(date_price_dict, file_to_write)

	return date_price_dict

if __name__ == '__main__':
	receipt_dict = ocr_fun()



	# show the output images
	# cv2.imshow("Image", image)
	# cv2.imshow("Output", gray)
	# cv2.waitKey(0)
