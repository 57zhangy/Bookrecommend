import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.mllib.recommendation import ALS,MatrixFactorizationModel
from pyspark.sql import SparkSession
# Create a local StreamingContext with two working thread and batch interval of 1 second

import redis

pool = redis.ConnectionPool(host='192.168.43.50', port=6379)
redis_client = redis.Redis(connection_pool=pool)

sc = SparkContext("local", "recommend")
sc.setLogLevel("WARN")
def redisOp():
    redis_client.set(1,'b')
    print(redis_client.get(1))
def getRecommendByUserId(userid,rec_num):
    try:
        model=MatrixFactorizationModel.load(sc,'recommendModel')
        result=model.recommendProducts(userid,rec_num)
        temp=''
        for r in result:
            temp+=str(r[0])+','+str(r[1])+','+str(r[2])+'|'
        redis_client.set(userid,temp)
        print('load model success !')
    except Exception as e:
        print('load model failed!'+str(e))
    sc.stop()

if __name__ == '__main__':
    getRecommendByUserId(20,5)
    print(redis_client.get(5))
#redisOp()
