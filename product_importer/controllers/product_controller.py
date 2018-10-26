from flask import Flask, make_response
import flask
import os
from ..utils import *

class ProductController():
	
	UPLOAD_FOLDER = os.getcwd()
	
	def upload_products(self, request):
		file = get_file(request)
		data = get_csv_data(file)
		for row in data:
			print row
			break		

