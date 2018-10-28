from flask import Flask, make_response, render_template
from sqlalchemy import or_ 
import flask
import os
from ..utils import *
from ..settings import * 
from ..models.product import Product
import uuid
# from sqlalchemy.ext.declarative import declarative_base

class ProductController():
	
	UPLOAD_FOLDER = os.getcwd()
	
	def upload_products(self, request):
		if request.form.get('url') is not None:
			data = get_csv_data_from_url(request.form.get('url'))
		elif request.files is not None:
			file = get_file(request)
			data = get_csv_data(file)
		session = Session()
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
		session.close()
		return True

	def product_filter(self, request):
		try:
			result = []
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
			dataset = dataset.all()
			for data in dataset:
				response = {}
				response['name'] = data.name
				response['sku'] = data.sku
				response['description'] = data.description
				response['is_active'] = data.is_active
				response['is_archived'] = data.is_archived
				response['created_at'] = data.created_at
				result.append(response)
		except:
			result = []
		finally:
			session.close()
			return result




