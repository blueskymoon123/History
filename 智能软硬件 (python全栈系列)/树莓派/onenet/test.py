import requests

import json



url = "http://api.heclouds.com/devices/525114527/datapoints"
headers = { "api-key":'YKh3DYoChxVTrq6chbmubIhAJz0='}#,"Connection":"close"}

bb = {"datastreams":[{"id":"cmd","datapoints":[{"value":1}]}]}#可以多个
requests.post(url,headers = headers,data=json.dumps(bb))  #一定json转



###########################
url = "http://api.heclouds.com/devices/"+str(id)+"/datapoints"
headers = { "api-key":password}
data={'limit':limit_num} #可缺省
receive = requests.get(url,headers = headers,params = data).text
data = (json.loads(receive))['data']