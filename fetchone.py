import json
import psycopg2
from config import config

 
 
def get_vendors():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # cur.execute("SELECT vendor_id, vendor_name FROM vendors WHERE vendor_id=%s ORDER BY vendor_name", (id, ))
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")
        print("The number of parts: ", cur.rowcount)
        returned_data = cur.fetchall()
        columns = ('vendor_id', 'vendor_name')
        results = []
        for row in returned_data:
            results.append(dict(zip(columns, row)))

        print json.dumps(results, indent=2)
 
        # while row is not None:
        #     print(row)
        #     row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_vendors()
