from flask import Flask
from configuration import configure_all

# inicializando o flask

app = Flask(__name__)


configure_all(app)

# executa o servidor web
app.run(debug=True)

