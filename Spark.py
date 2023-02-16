#Linking with spark

from pyspark import SparkConf
from pyspark.context import SparkContext

conf = SparkConf()
conf.setMaster("local").setAppName("My app")

conf.get("Spark.app.name")

sc = SparkContext(conf=conf)
sc.master
sc.appName
sc.sparkHome is None