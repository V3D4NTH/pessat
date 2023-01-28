import mysql.connector as mycon
cn=mycon.connect(host='localhost',user='root',passwd='root',database='pessatui')
cur=cn.cursor()
query="""CREATE TABLE ST_DATA (
    SRN INT NOT NULL,
    ATTITUDE INT,
    MOTIVATION INT,
    CONFIDENCE INT,
    RESILIENCE INT,
    TOTAL INT);"""
cur.execute(query)
