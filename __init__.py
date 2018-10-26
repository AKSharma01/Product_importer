from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from product_importer.settings import *
from product_importer.routes.product.routes import product 

app = Flask(__name__)
CORS(app)

app.register_blueprint(product)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
	app.run(port=5001,debug=True)
