from werkzeug.utils import secure_filename
import os
import csv
import requests

""" get file from request """
def get_file(request):
	return request.files['file']

""" secure name """
def get_secure_filename(file):
	return secure_filename(file.name)

""" get csv data """
def get_csv_data(file):
	file = save_file(file)
	size = os.path.getsize(file)
	if size < 1:
		return False, 'File size should be in between 1KB to 100MB'
	if size / 1024 > 100:
		return False , 'File size should be in between 1KB to 100MB'
	with open(file, 'r') as data:
		data = csv.reader(data)
		data = [row for row in data]
		del data[0]
	os.remove(file)
	return True, data

""" get the directory to upload a file """
def get_upload_folder():
	return os.getcwd()

""" save the file """
def save_file(file):
	upload_folder = get_upload_folder()
	filename = get_secure_filename(file)
	path = os.path.join(upload_folder, filename + '.csv')
	file.save(path)
	return path

""" get csv data from url """
def get_csv_data_from_url(url):
	upload_folder = get_upload_folder()
	try:
		response = requests.get(url)
	except Exception as e:
		return False, 'Enter a valid csv url'
	path = os.path.join(upload_folder, 'file' + '.csv')
	with open(path, 'wb') as f:
		f.write(response.content)
	with open(path, 'r') as data:
		data = csv.reader(data)
		data = [row for row in data]
		del data[0]
	size = os.path.getsize(path)
	if size < 1:
		return False
	if size / 1024 > 100:
		return False 
	os.remove(path)
	return True, data

##
# Get Allowed Extension
##
def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'doc', 'xls', 'csv']
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





