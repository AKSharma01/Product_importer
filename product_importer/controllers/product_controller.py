from flask import Flask, make_response, render_template
from sqlalchemy import or_ 
import flask
import os
from ..utils import *
from ..settings import * 
from ..models.product import Product
import uuid

""" Product Controller """
class ProductController():
	
	""" upload products through csv file or url
	@param request file or url
	@response bool, response mg
	 """
	def upload_products(self, request):
		try:
			session = Session()	
			if request.form.get('url') is not None:
				status, data = get_csv_data_from_url(request.form.get('url'))
			elif len(request.files):
				file = get_file(request)
				if isinstance(file, bool):
					status, data = False, 'Size should be between 1 KB to 100 MB'
				else:
					status, data = get_csv_data(file)
			else:
				status, data = False, 'Select a csv file or a valid url to upload'
			if status:
				for row in data:
					name = row[0]
					sku = row[1]
					description = row[2]
					is_exist = session.query(Product).filter_by(sku=sku).first()
					if is_exist is None:
						_id = str(uuid.uuid4()).strip()
						product = Product(id=_id, name=name, sku=sku, description=description)
						session.add(product)
						session.commit()
					status, data = True, ''
		except Exception as e:
			return False, ''
		finally:
			session.close()
		return status, data

	""" Product filter
	@param name sku
	@return data
	 """
	def product_filter(self, request):
		try:
			result = []
			
			""" creating session for querying """
			session = Session()
			dataset = session.query(Product)

			if request.args.get('name') is not None:
				dataset = dataset.filter(Product.name.ilike('%{}%'.format(request.args.get('name')))) 
			if request.args.get('sku') is not None:
				dataset = dataset.filter(Product.sku.ilike('%{}%'.format(request.args.get('sku'))))
			if request.args.get('is_active') is not None:
				dataset = dataset.filter_by(is_active=request.args.get('is_active'))
			if request.args.get('is_archived') is not None:
				dataset = dataset.filter_by(is_archived=request.args.get('is_archived'))

			if request.args.get("search") is not None:
				dataset = dataset.filter(or_ (Product.name.ilike("%{}%".format(request.args.get("search"))),Product.sku.ilike("%{}%".format(request.args.get("search")))) )
			
			""" get data """
			dataset = dataset.all()
			
			""" response """
			for data in dataset:
				response = {}
				response['name'] = data.name
				response['sku'] = data.sku
				response['description'] = data.description
				response['is_active'] = data.is_active
				response['is_archived'] = data.is_archived
				response['created_at'] = data.created_at
				result.append(response)
		except Exception as e:
			result = []
		finally:
			""" closing the session """
			session.close()
		return result



