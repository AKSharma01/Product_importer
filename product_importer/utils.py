from werkzeug.utils import secure_filename
import os
import csv

def get_file(request):
	return request.files['file']

def get_secure_filename(file):
	return secure_filename(file.name)

def get_csv_data(file):
	file = save_file(file)
	with open(file, 'r') as data:
		data = csv.reader(data)
		data = [row for row in data]
		del data[0]
		return data

def get_upload_folder():
	return os.getcwd()

def save_file(file):
	upload_folder = get_upload_folder()
	filename = get_secure_filename(file)
	path = os.path.join(upload_folder, filename + '.csv')
	file.save(path)
	return path





