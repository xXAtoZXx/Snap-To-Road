# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json
app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))
scalar = pickle.load(open('scalar.pkl','rb'))

Radius = 6371e3
def distanceBetween(point1, point2):
    phi1 = point1[0] * np.pi / 180
    phi2 = point2[0] * np.pi / 180
    deltaPhi = (point2[0] - point1[0]) * np.pi / 180
    deltaLambda = (point2[1] - point1[1]) * np.pi / 180
    a = np.sin(deltaPhi/2) * np.sin(deltaPhi/2) + np.cos(phi1) * np.cos(phi2) * np.sin(deltaLambda/2) * np.sin(deltaLambda/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return Radius * c

def findMatchedPoint(point, segment):
    file = open('route.json', 'r')
    FileData = json.load(file)
    coordinates = []
    for feature in FileData['features']:
        if feature['properties']['segment'] == segment:
            coordinates.extend(feature['geometry']['coordinates'])
            break
    min = distanceBetween(coordinates[0], point)
    minIndex = 0
    for idx in range(1,len(coordinates)):
        dist = distanceBetween(coordinates[idx], point)
        if(dist < min):
            min = dist
            minIndex = idx
    return coordinates[minIndex]

@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json(force=True)
    print(data)
    returnList=[]

    for coords in data['coordinates']:
        predictVal = pd.DataFrame([coords], columns=['Latitude','Longitude'])
        predictVal = scalar.transform(predictVal)
        value = model.predict(predictVal)[0]
        returnList.append(int(value))

    listOfPoints = []
    for index, gpoint in enumerate(data['coordinates']):
        listOfPoints.append(findMatchedPoint(gpoint,returnList[index])) 

    return jsonify({"data":listOfPoints})
if __name__ == '__main__':
    app.run(port=5000, debug=True)