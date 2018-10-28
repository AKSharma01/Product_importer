from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from product_importer.config.app import app, db

class Product(db.Model):
	""" tablename """
	__tablename__ = 'product'

	""" Products atrributes """

	id = db.Column(db.String(255), primary_key=True)
	name = db.Column(db.String(255) , nullable=False)
	sku = db.Column(db.String(255) , nullable=False, unique=True)
	description = db.Column(db.String(255) , nullable=False)
	is_active = db.Column(db.Boolean , default=True)
	is_archived = db.Column(db.Boolean , default=False)
	created_at = db.Column(db.DateTime, server_default=db.func.now())
	updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
	archived_at = db.Column(db.DateTime, nullable=True)





