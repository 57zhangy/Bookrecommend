import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel
from pyspark.sql import SparkSession

# Create a local StreamingContext with two working thread and batch interval of 1 second
# sc = SparkContext("spark://192.168.192.130:7077", "recommend")
sc = SparkContext("local", "recommend")
sc.setLogLevel("WARN")
txt = sc.textFile('hit.txt')
ratingsRDD = txt.flatMap(lambda x: x.split()).map(lambda x: x.split(','))
sqlContext = SparkSession.builder.getOrCreate()
from pyspark.sql import Row

user_row = ratingsRDD.map(lambda x: Row(
    userid=int(x[0]), bookid=int(x[1]), hitnum=int(x[2])
))
# print user_row.take(5)
user_df = sqlContext.createDataFrame(user_row)
# user_df.printSchema()
# user_df.show()
user_df.registerTempTable('test')
# sqlContext.sql("select * from test").show()
datatable = sqlContext.sql("select userid,bookid,sum(hitnum) as hitnum  from test group by userid,bookid")
# datatable.show()
# print type(datatable)
bookrdd = datatable.rdd.map(lambda x: (x.userid, x.bookid, x.hitnum))
# print bookrdd.collect()
model = ALS.trainImplicit(bookrdd, 10, 10, 0.01)
# print model
# print model.recommendProducts(5,5)

# sqlContext.sql("").show()
import os
import shutil

if os.path.exists('recommendModel'):
    shutil.rmtree('recommendModel')
model.save(sc, 'recommendModel')
