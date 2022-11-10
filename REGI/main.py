from flask import Flask
from flask_cors import CORS
import json
from waitress import serve
from Routes.Candidatos import candidato
from Routes.Mesas import mesas
from Routes.Partidos import partidos
from Routes.Resultados import resultados
import pymongo
import certifi

# @app.route("http://127.0.0.1:9999",methods=['GET'])

#database shit
ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://ad123:ad123@cluster0.r1uuskn.mongodb.net/REGISTRADURIA?retryWrites=true&w=majority",tlsCAFile=ca)
db = client["test"]
print(db)

baseDatos = client["REGISTRADURIA"]
print(baseDatos.list_collection_names())
###############


app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(candidato)
app.register_blueprint(mesas)
app.register_blueprint(partidos)
app.register_blueprint(resultados)

app.debug = True




def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


