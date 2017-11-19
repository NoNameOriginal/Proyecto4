# Unidad 3: Big Data - HDFS
## ST0263 - Tópicos Especiales en Telemática
## Ingeniería de Sistemas
## Universidad EAFIT
### Profesor: Edwin Montoya M. – emontoya@eafit.edu.co
## 2017-2


# Proyecto 4


    Geralin Stefania Fernandez Bedoya      codigo: 201510033010
    Christian Londoño Cañas                codigo: 201510112010



# Instalacion:

 
 ## Python 
 Se Ejecuta el siguiente comando:
 ```
    pip install pyspark
 ```
 Asegurarse de tener la variable JAVA_HOME configurada
    
 ## Otra opcion
 Descargar e instalar desde la pagina de descarga de apache spark 
 [Spark]https://spark.apache.org/downloads.html


# Definiciones necesarias

 TF-IDF:
 tf idf es  una medida de frecuencia en un texto o coleccion de palabras en la que se puede determinar la frecuencia de una palabra en este, determinando asi que palabras son mas frecuentes 
 y que tan relevante es una palabra en un texto.

 K means:
 Este es un metodo de agrupamiento de datos en el que se utiliza centroides para agrupar k grupos cercanos y asi tener el agrupamiento por cercania de datos.


 ## Explicacion algoritmo
 1. Primero tenemos la verificacion de parametros , la cual solo se asegura que el usuario entregue la carpeta de salida y el K(numero de conjuntos en el que quiere que se separen los archivos)

 2. Luego de esto observamos la obtension de los archivos o documentos 
        documentos = sc.wholeTextFiles(dirs)
    sus nombres en nombredocumentos  
        nombresDocumentos=documentos.Keys().collect()
    para asi luego obtener el vector docs que es un vector con el contenido de los archivos
        docs=documetos.values().map(lambda doc: doc.split(" "))


 3. esta parte es el manejo de TF-IDF  en el que el tf esta hayara la frecuencia de los terminos en el documento
        tf=hashingTF.transform(docs)
    luego el idf encontrara la relevancia de una palabra en los documentos
        idf=IDF().fit(tf)
    para terminar con esta parte esta el tfidf que es un RDD el cual es como una especie de vector con el resultado de lo anterios, que utilizaremos para luego hayar las "distancias" entre archivos
        tfidf=idf.transform(tf)

 4. por ultimo en esta parte se hace la implementacion del k means 
        clusters=KMeans.train(tfidf,k,maxIterations=20)
    tenemos luego la ubicacion de los archivos en el cluster con el clousterid
        clousterid=clusters.predict(tfidf).collect()
    
    luego de esto tenemos el diccionario que relaciona el nombre del archivo con el cluster correspondiente
        diccionario=dict(zip(nombreDocumentos , clusterid))

    la paralelizacion que se observa a el final es para obtener los itms del diccionario y meterlos en un vectos(RDD)


# Comando ejecucion
    spark-submit --master yarn --deploy-mode cluster proyectoSpark.py 2 salidaArgv9
 
    proyectoSpark.py es el archivo en el que esta el algoritmo 
    2 es el numero de k que quiero manejar
    salidaArgv9 es la carpeta que se generara al ejecutarse
