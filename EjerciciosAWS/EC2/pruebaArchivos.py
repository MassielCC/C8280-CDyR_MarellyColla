import os

ruta = './buckets'

# verificamos si el directorio ya existe
if not os.path.exists(ruta):
  os.mkdir(ruta)
  print("Directorio %s creado!" % ruta)
else:
  print("Directorio %s ya existe" % ruta)
  
def crear_file(ruta, nombre, contenido):
    ruta= "./buckets/" + ruta + "/"+ nombre 
    with open(ruta, "w") as archivoI:
        archivoI.write(contenido)
    archivoI.close()

crear_file("mybucket","file1.txt", "Hola esta es la versión 1")
