from flask import Flask, jsonify

def transform(result):
      
      data  = {
            'id' : result['id'],
            'firstName' : result['first_name'],
            'lastName' : result['last_name'],
            'email': result['email'],
            'company': result['company'],
            'phone': result['phone'],
            'country': result['country'],
            'state': result['state'],
            'aboutProject': result['about_project'],
            'projectType': result['project_type'],
            'signUpNewsLetter': result['sign_up_news_letter'],
            'createdAt': result['created_at'],
            'updatedAt': result['updated_at'],
            'deleted_at': result['deleted_at']
	}
      return jsonify(data)