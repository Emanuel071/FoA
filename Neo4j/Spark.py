from email import header
import sys
from urllib import request
import boto3
# from awsglue.transforms import *
# from awsglue.utils import getResolvedOptions
from pyspark import SparkContext, HiveContext, SQLContext
# from awsglue.context import GlueContext
from pyspark.sql import SparkSession
# from awsglue.job import Job
from datetime import datetime
# from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as pyspsf
import os                               #for fetchin txt
import pandas as pd
#SPECIAL IMPORT DEPENDENCIES
import neo4j
from neo4j import __version__ as neo4j_version
from pyspark import __version__ as spark_version
import json
import requests

print("Neo4j Version: " + str(neo4j_version))
print(' ')
print("Spark Version: " + str(spark_version))
print(' ')

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, 
[
    'JOB_NAME',
    'catalog_id',
    'dl_glue_db_nm',
    'dl_glue_tbl_prefix',
    'username',
    'pw'    
])

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get

sc = SparkContext()
hc = HiveContext(sc)
sqlContext = SQLContext(sc)
gc = GlueContext(sc)

sparkSession = SparkSession \
                    .builder \
                    .config("fs.s3.canned.acl", "BucketOwnerFullControl") \
                    .enableHiveSupport() \
                    .getOrCreate()

spark = gc.sparkSession 

# Logger
#logger = glueContext.get_logger()

# Allows Glue to Interact with ENTRPR S3
gc._jsc.hadoopConfiguration() \
                .set("fs.s3.canned.acl", "BucketOwnerFullControl")

job = Job(gc)
job.init(args['JOB_NAME'], args)

s3 = boto3.resource('s3')
glue_client = boto3.client('glue')

try:
    df = spark.read \
        .load("s3://trv-common-css-ppl-analytics-dc3-dev-us-east-1-umtotr/ppl-analytics/utilities/test/HelloWorld.csv",
        format="csv", header="true")

        

except Exception as e:
    print("Failed to Spark:", e)

df.show(5)

try:
    example = spark.read.format("org.neo4j.spark.DataSource") \
        .option("url", "neo4j+s://eda-neo4j-dev.thc.travp.net:7687") \
        .option("labels", "Message:Hello World!") \
        .load()

except Exception as e:
    print("Failed to 4j read:", e)

try:
    (df.write \
            .format("org.neo4j.spark.DataSource") \
            .mode("overwrite") \
            .option("url", "neo4j+s://eda-neo4j-dev.thc.travp.net:7687") \
            .option("database", "css-ppl-bia-db-dev") \
            .option("authentication.type", "basic") \
            .option("authentication.basic.username", str(args['username'])) \
            .option("authentication.basic.password", str(args['pw'])) \
            .option("node.keys", "name,surname") \
            .option("labels", ":Person:Customer") \
            .save())

except Exception as e:
    print("Failed to 4j write:", e)

current_dt = datetime.utcnow().strftime('%Y-%m-%d') 

print('DONE')
job.commit()


From: Calderon, Emanuel A 
Sent: Wednesday, February 23, 2022 7:42 AM
To: 'ecalde11@jh.edu' <ecalde11@jh.edu>
Subject: neo4j

import sys
import boto3
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession
from awsglue.job import Job
from datetime import datetime
from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as pyspsf
import os                               #for fetchin txt
import pandas
#SPECIAL IMPORT DEPENDENCIES
import neo4j
from neo4j import __version__ as neo4j_version
import json

print(neo4j_version)
print('')
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, 
[
    'JOB_NAME',
    'catalog_id',
    'dl_glue_db_nm',
    'dl_glue_tbl_prefix',
    'username',
    'pw'    
])

sc = SparkContext()
sparkSession = SparkSession.builder \
    .config("fs.s3.canned.acl", "BucketOwnerFullControl") \
    .enableHiveSupport() \
    .getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Logger
#logger = glueContext.get_logger()

# Allows Glue to Interact with ENTRPR S3
glueContext._jsc.hadoopConfiguration() \
    .set("fs.s3.canned.acl", "BucketOwnerFullControl")

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3 = boto3.resource('s3')
glue_client = boto3.client('glue')

try:
    uri = "bolt://eda-neo4j-dev.thc.travp.net:7687/db/css-ppl-bia-db-dev/"
    driver = neo4j.GraphDatabase \
        .driver(uri, auth=(str(args['username']), str(args['pw'])))
    
    print(json.dumps(driver.verify_connectivity()))
    print('VC')
    print(' ')
    print("connected: {}".format(driver.verify_connectivity()))
    print(' ')

except Exception as e:
    print("Failed to create the driver:", e)

def get_people(tx):
    persons = []
    result = tx.run("MATCH (a:Person) RETURN a LIMIT 25")
    for record in result:
        persons.append(record["a"])
    return persons

try:
    # other examples 
    # https://neo4j.com/docs/api/python-driver/current/

    # setting session to defualt database which is only one
    # https://neo4j.com/docs/api/java-driver/current/org/neo4j/driver/SessionConfig.Builder.html
    # ctrl find withDatabase
    
    with driver.session(database="css-ppl-bia-db-dev", 
    default_access_mode=neo4j.READ_ACCESS) as session:
        people = session.read_transaction(get_people)
        for p in people:
            print(p)

except Exception as e:
    print("Query failed:", e)
finally:
    if session is not None:
        session.close()

if driver is not None:
    driver.close()

current_dt = datetime.utcnow().strftime('%Y-%m-%d') 

print('DONE')
job.commit()


Thank You,
 
Emanuel Calderon | Data Engineer in Corporate & Shared Systems | Travelers
Tower Square, One| Hartford, CT 06183
: 860.594.9824 |: ecalder@travelers.com
  

________________________________________
This message (including any attachments) may contain confidential, proprietary, privileged and/or private information. The information is intended to be for the use of the individual or entity designated above. If you are not the intended recipient of this message, please notify the sender immediately, and delete the message and any attachments. Any disclosure, reproduction, distribution or other use of this message or any attachments by an individual or entity other than the intended recipient is prohibited.

TRVDiscDefault::1201 
