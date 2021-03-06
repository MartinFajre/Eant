from flask import Flask
from flask import json


app = Flask(__name__)   


@app.route('/users')
def twitter_Users():
    users = [
        {'name':'tincchofajre'},
        {'name':'eantech'},
        {'name':'TinchoLutter'},
        {'name':'bitcoinArg'}
        ]
    
    response = app.response_class( response = json.dumps(users), status = 200, mimetype = 'application/json' )
    
    return response

   

@app.route('/users/<path>')
def searchUsers(path):
    if path == 'people':
        return 'ACA VA UN JSON DE PERSONAS'
    elif path == 'company':
        return 'ACA VA UN JSON DE EMPRESAS'
    else:
        return 'UPPS.. NO PUEDO BUSCAR LO QUE ESTAS PIDIENDO'
    
app.run( port = 3030, host = '0.0.0.0' )     
    
