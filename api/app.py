from flask import Flask
from flask_restplus import Api, Resource, fields, abort
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='sendIT MVC api',
)

base_url= '/api/v1'

app.config['RESTPLUS_VALIDATE'] = True
app.config['DEBUG'] = True

@api.route(base_url + '/hello')
class HelloWorld(Resource):
	def get(self):
		
		"sanity check"

		return {'hello': 'world'}

