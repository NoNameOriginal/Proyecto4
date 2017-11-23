import sys

from pyspark import SparkContext                                                                                                                                                                  
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.clustering import KMeans                                                                                                                                                                   

if __name__ == "__main__":
    dirs = "hdfs:///user/clondo46/datasets/gutenberg"  
    k = 5    
    maxIters = 20
    sc = SparkContext(appName="Proyecto04") 
    #Leemos tfidf
    documentos = sc.wholeTextFiles(dirs) 
    nombreDocumentos = documentos.keys().collect() 
    docs = documentos.values().map(lambda doc: doc.split(" "))
    #Usamos TFIDF
    hashingTF = HashingTF() 
    tf = hashingTF.transform(docs)
    idf = IDF().fit(tf)    
    tfidf = idf.transform(tf) 
    #Crea el modelo de k-mean y crea los clusters
    clusters = KMeans.train(tfidf,k,maxIterations=maxIters) 
    clustersid = clusters.predict(tfidf).collect()  
    diccionario = dict(zip(nombreDocumentos, clustersid)) 
    d = sc.parallelize(diccionario.items()) 
    d.coalesce(1).saveAsTextFile("hdfs:///user/clondo46/gut5")     
    sc.stop() #SparkContext detenido:
