from flask import Flask
from routes.home import home_route
from routes.cliente import cliente_route

# inicializando o flask

app = Flask(__name__)

# registrando a variavel do blueprint
app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')

# executa o servidor web
app.run(debug=True)

