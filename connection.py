# coding=utf-8
import pandas as pd
import sqlalchemy
import settings

def GetEngineFS():
    USER = settings.ZEUS_USER
    PW = settings.ZEUS_PW
    URL = '172.21.130.152:35432/ZEUS_BR-FS'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    #print url
    return sqlalchemy.create_engine(url)

def run_queryFS(qry):
    #print qry
    return pd.read_sql(sql=qry, con=GetEngineFS())

def GetEngineCM():
    USER = settings.ZEUS_USER
    PW = settings.ZEUS_PW
    URL = '172.21.9.153:35432/ZEUS_BR-CM'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    #print url
    return sqlalchemy.create_engine(url)

def run_queryCM(qry):
    #print qry
    return pd.read_sql(sql=qry, con=GetEngineCM())

def GetEngineAR():
    USER = settings.ZEUS_USER
    PW = settings.ZEUS_PW
    URL = '151.10.190.48:35432/ZEUS_AR'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    #print url
    return sqlalchemy.create_engine(url)

def run_queryAR(qry):
    #print qry
    return pd.read_sql(sql=qry, con=GetEngineAR())

