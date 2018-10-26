from se.Repositories.Repository import Repository
from se.Exceptions.SeException import SeException
from se.Repositories.Mailer.Config import *
from flask import Flask , request, abort
from flask_mail import Mail, Message
from se.connect import connect
import requests
import uuid

class LeadRepository:
	
	def __init__(self, mailerUrl):

		self.mailerUrl = mailerUrl

	def store(self , wrappedObj):
		data = Repository().fetchDetailsWithoutJoin('lead_management', {'email':wrappedObj['sender']})
		id = str(uuid.uuid4()).strip()
		if not data:	
			leadId = Repository().store('lead_management', {'id':id,'first_name':wrappedObj['firstName'],'last_name':wrappedObj['lastName'],'email':wrappedObj['sender'],'company':wrappedObj['company'],'phone':wrappedObj['phone'],'country':wrappedObj['country'],'state':wrappedObj['state'],'about_project':wrappedObj['aboutProject'],'project_type':wrappedObj['projectType'],'sign_up_news_letter':wrappedObj['signUpNewsLetter']})
			data = Repository().fetchDetailsWithoutJoin('lead_management', leadId)
			r = requests.post(self.mailerUrl, wrappedObj)
			return data
		else:
			abort(404)	
	

	def get_lead_by_id(self, leadId):
		data = Repository().fetchDetailsWithoutJoin('lead_management', {'id':leadId})
		if data:
			return data
		else:
			abort(404)	
	def delete_lead_by_id(self, leadId):
		data = Repository().fetchDetailsWithoutJoin('lead_management', {'id':leadId})
		if data:
			Repository().delete('lead_attachment', {'lead_id':leadId})
			Repository().delete('lead_management', {'id':leadId})
			return True
		else:
			abort(404)