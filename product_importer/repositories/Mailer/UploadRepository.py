from se.Repositories.Repository import Repository 
from flask import Flask , request, jsonify
from werkzeug.utils import secure_filename
from se.connect import *
import requests
import uuid
import json
import os


class UploadRepository:

        def __init__(self, uploadUrl):

                self.uploadUrl = uploadUrl

        def upload_attachment(self, request):                
                list = []
                nameList = []
                totalList = []
                # folder for uploading file locally
                UPLOAD_FOLDER = os.getcwd()+'/AwsUpload/'
                if 'attachment-count' in request.form:
                        count = int(request.form['attachment-count'])+1
                        for i in range(1,count):
                                key =  'attachment'+'-'+str(i)
                                file = request.files[str(key)]
                                filename = secure_filename(file.filename)
                                nameList.append(filename)
                                if not os.path.isdir(UPLOAD_FOLDER):
                                        os.mkdir(UPLOAD_FOLDER)
                                fileToBeUploaded = os.path.join(UPLOAD_FOLDER , filename)
                                totalList.append(fileToBeUploaded)
                                file.save(fileToBeUploaded)   
                                list.append(('files[]',open(fileToBeUploaded, 'rb')))
                        #upload request to uploadServer
                        r = requests.post(self.uploadUrl, files=list)
                        print r.text 
                        self.save_attachment_in_db(request.form['sender'], totalList)
                        # deleting the file locally 
                        for name in nameList:
                                os.remove(os.path.join(UPLOAD_FOLDER ,  name)) 
                        return 'attachment successfully uploaded'  
                
                return 'something went wrong'              

        def save_attachment_in_db(self, sender, attachments):
                data = Repository().fetchDetailsWithoutJoin('lead_management',{'email':sender})
                cursor = connect.cursor() 
                cursor.execute("select * from information_schema.tables where table_name='lead_attachment'")
                is_exists =  cursor.fetchone()
                if is_exists is None:
                        cursor.execute("CREATE TABLE lead_attachment (id varchar(100), lead_id varchar(100) REFERENCES lead_management(id), attachment BYTEA)")
                        connect.commit()        
                for attachment in attachments:
                        print attachment
                        query = "INSERT INTO lead_attachment (id,lead_id,attachment) VALUES(%s,%s,%s)"
                        queryData = (str(uuid.uuid4()).strip(), data['id'], psycopg2.Binary(open(attachment,'rb').read()))
                        cursor.execute(query, queryData)
                        connect.commit()


