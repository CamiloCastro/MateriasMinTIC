import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb://usuario-grupo40:usuario-grupo40@ac-yrfo6pa-shard-00-00.tholq2k.mongodb.net:27017,ac-yrfo6pa-shard-00-01.tholq2k.mongodb.net:27017,ac-yrfo6pa-shard-00-02.tholq2k.mongodb.net:27017/?ssl=true&replicaSet=atlas-8rr3k3-shard-0&authSource=admin&retryWrites=true&w=majority", tlsCAFile=ca)

ra_db = client["bd-registro-academico"]
coll_estudiantes = ra_db["estudiantes"]
estudiante = {
  "nombre" : "Pedro",
  "apellido" : "Perez",
  "Edad" : 27,
  "telefonos" : ["369214578"],
  "materias" : [
    {
      "nombre" : "Fisica",
      "creditos" : 5
    },
    {
      "nombre" : "Calculo",
      "creditos" : 3
    }
  ]
}
coll_estudiantes.insert_one(estudiante)





