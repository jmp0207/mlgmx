import urllib.request, urllib.parse, urllib.error
import json


sist_conexion = 'SIN/' 
tipo_mercado = 'MTR/'
nodos = '01PLO-115,01AGU-230,01AGV-85,01AIN-115,01ALR-85,01AMO-85,01ANL-85,01ANM-115,01ANS-85,01ANU-115,01ANU-69,01ARA-85,01ARX-230,01ASK-230,01ATE-230,01ATE-85,01ATG-69,01ATI-230,01ATK-230,01ATM-115'
fecha_inicial = '/2018/05/22'
fecha_final = '/2018/05/28'
formato = '/JSON'

url = 'https://ws01.cenace.gob.mx:8082/SWPML/SIM/'+ sist_conexion + tipo_mercado + nodos + fecha_inicial + fecha_final + formato

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

print(json.dumps(js, indent=4))

