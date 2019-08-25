import sqlite3
import sys
sys.path.append("..")

def create_connection(db_file):
    connection = None
    connection = sqlite3.connect(db_file)
    c = connection.cursor()
    return c, connection

def sql_insert_company(name, c, connection):
    try:
        sql = "INSERT INTO `company` (name) VALUES ({});".format(name)
        try:
            c.execute(sql)
        except:
            pass
        connection.commit()
    except Exception as e:
        print("Insertion: ", str(e))

def sql_insert_data(date, price, open_price, high, low, vol, name, c, connection):
    sql_select = "SELECT id FROM 'company' WHERE name=={};".format(name)
    c.execute(sql_select)
    company_id = c.fetchall()
    try:
        sql = "INSERT INTO `data` (date, price, open_price, high, low, vol, company_id) VALUES ({}, {}, {}, {}, {}, {}, {});".format(date, price, open_price, high, low, vol, company_id)
        try:
            c.execute(sql)
        except:
            pass
        connection.commit()
    except Exception as e:
        print("Insertion: ", str(e))