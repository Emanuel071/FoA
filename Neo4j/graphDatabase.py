import sys
import boto3
# from awsglue.transforms import *
# from awsglue.utils import getResolvedOptions
# from pyspark.context import SparkContext
# from awsglue.context import GlueContext
from pyspark.sql import SparkSession
# from awsglue.job import Job
from datetime import datetime
# from awsglue.dynamicframe import DynamicFrame
import pyspark.sql.functions as pyspsf
import os                               #for fetchin txt
import pandas
#SPECIAL IMPORT DEPENDENCIES
import neo4j
from neo4j import __version__ as neo4j_version
import json
from neo4j.exceptions import ServiceUnavailable
import logging

print(neo4j_version)
print('')


uri = "neo4j+s://a649506b.databases.neo4j.io"
user = "neo4j"
password = "ZeGgBo-uY4Xz-oF50cMg9kjh_0qZoACCoFW-EVXSUnk"

try:
    driver = neo4j.GraphDatabase \
        .driver(uri, auth=(user, password))
    
    print("connected: {}".format(driver.verify_connectivity()))
    print(' ')

except Exception as e:
    print("Failed to create the driver:", e)

def get_people(tx):
    persons = []
    result = tx.run("MATCH (n:Message) RETURN n LIMIT 25")
    for record in result:
        persons.append(record["a"])
    return persons

try:
    # other examples 
    # https://neo4j.com/docs/api/python-driver/current/

    # setting session to defualt database which is only one
    # https://neo4j.com/docs/api/java-driver/current/org/neo4j/driver/SessionConfig.Builder.html
    # ctrl find withDatabase
    
    with driver.session(database="neo4j", 
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
# job.commit()
