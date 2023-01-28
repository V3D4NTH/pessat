import mysql.connector as mycon
cn=mycon.connect(host='localhost',user='root',passwd='password',database='pessatui')
cur=cn.cursor()
query="""CREATE TABLE ST_DATA (
    PESSATID VARCHAR(255)     NOT NULL ,
    ATTITUDE INT,
    MOTIVATION INT,
    CONFIDENCE INT,
    RESILIENCE INT,
    TOTAL INT,
    PRIMARY KEY (PESSATID));"""
cur.execute(query)
