import sys
import logging
import pymysql
import json
import requests
import time
from datetime import datetime

hostname = 'ejercicio2-instancia.cryssnu9ajdn.us-east-2.rds.amazonaws.com'
username = 'ejercicio2admin'
password = '8XLY3NHHU6WH6ODZMCDj'
dbname = 'ejercicio2db'

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=dbname, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: No es posible conectarse a instancia MySQL.")
    logger.error(e)
    sys.exit()

logger.info("CORRECTO: Acceso Exitoso a instancia MySQL.")

url = "https://dweet.io:443/get/latest/dweet/for/thecore"
webhook = "https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9"

for i in range(15): 
    response = requests.request("GET", url)
    print("Respuesta : " + str(response.status_code))
    if response.status_code == 200:
            response_json = response.json()
            if(response_json["with"]):
                temperatura = response_json["with"][0]['content']['temperature']
                humedad = response_json["with"][0]['content']['humidity']
                fecha = datetime.today().strftime('%Y-%m-%d %H:%M')
                with conn.cursor() as cur:
                    sql = 'insert into ejercicio2_table (fecha, temperatura, humedad) values(%s, %s, %s)'
                    val = (fecha, temperatura, humedad)
                    cur.execute(sql, val)
                    conn.commit()
                    print('Agregado registro ' + str(i + 1) + ' satisfactoriamente.')
                
    time.sleep(59)
    
cur = conn.cursor()
sql = "select json_object('fecha',`fecha`,'temperatura',`temperatura`,'humedad',`humedad`) from `ejercicio2_table`"
cur.execute(sql)
data = cur.fetchall()

response = requests.request("POST", webhook, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print("Respuesta Webhook : " + str(response.status_code))
print("Proceso Finalizado.")