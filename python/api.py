import json
import requests

r = requests.get('http://127.0.0.1:3000/')

data = r.json()
#widget1=str(data[0]['name'])
#widget2=str(data[1]['name'])
#widget3=str(data[2]['name'])
#widgetx=str(data[3]['name'])
#widget1color=str(data[0]['color'])
#widget2color=str(data[1]['color'])
#widget3color=str(data[2]['color'])
#print(widget1+" is color: "+widget1color)
#print(widget2)
#print(widget3)
#print(widgetx)
#^ That was dumb, I'll do it a different way now below


for item in data:
    color = item['color']
    name = item['name']
    print("This widget is named: {} it is colored: {}.".format(name,color))