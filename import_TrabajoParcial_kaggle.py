

import json
import zipfile
import os

api_token = {"username":"elsitovar","key":"7bed8d274916385f7590e17f06e4cd34"} #contenido kaggle,json
# conectar a kaggle
with open("C:/Users/Joset/.Kaggle/kaggle.json","w") as file:
    json.dump(api_token,file)


location= "C:/TrabajoParcial/dataset"


    ## validar que la carpeta exista
if not os.path.exists(location):
    ## sino existe la carpeta dataset se crea 
    os.mkdir(location)

else:
            ## si si existe borro su contenido 
    for root,dirs,files in os.walk(location,topdown=False): 
        for name in files: os.remove(os.path.join(root,name))##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name))##elimino todas las carpetas

## descargar dataset de kaggle
                    
os.system("kaggle datasets download -d nelgiriyewithana/new-york-housing-market -p C:/TrabajoParcial/dataset")
                    
## decomprimir el archivo de kaggle
                    
os.chdir(location)## para ver el contendo del directorio
for file in os.listdir():
    zip_ref=zipfile.ZipFile(file,"r")##lee archivo.zip
    zip_ref.extractall()##extrae contenido de archivo.zip
    zip_ref.close()## cierre archivo