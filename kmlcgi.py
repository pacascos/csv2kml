from flask import Flask
from flask import request
from flask import Response
import pandas as pd

app = Flask(__name__)

tabla = pd.read_csv("./data/zonacoma.csv",sep=';', decimal=',')

@app.route('/q', methods=['GET', 'POST'])
def cgikml():

    bbox = request.args.get('BBOX')
    bbox = bbox.split(',')
    west = float(bbox[0])
    south = float(bbox[1])
    east = float(bbox[2])
    north = float(bbox[3])

    center_lng = ((east - west) / 2) + west
    center_lat = ((north - south) / 2) + south
    p = printPoints(west,south,east,north)

    kml = (
       '<?xml version="1.0" encoding="UTF-8"?>\n'
       '<kml xmlns="http://www.opengis.net/kml/2.2">\n %s'
       '</kml>'
       ) %(p)
    return Response(kml, mimetype = 'Content-Type: application/vnd.google-earth.kml')



def printPoints(w,s,e,n):
    print (w,s,e,n)
    resultados  = tabla [(tabla.LATITUDE > s) & \
                            (tabla.LATITUDE < n) & \
                            (tabla.LONGITUDE < e) & \
                            (tabla.LONGITUDE > w)].values.tolist()
    print len(resultados)
    placemarks = ''
    for item in resultados:
       placemarks = placemarks + \
       '<Placemark>\n' \
       '<name>View-centered placemark</name>\n' \
       '<Point><coordinates>%.6f,%.6f</coordinates></Point>\n' \
       '</Placemark>\n'%(item[16],item[15])
    return placemarks
