import httplib2
import urllib
import requests
import json
import sys

def Main():

    OH2_Host = "openhabianpi.home"
    OH2_Port = 8080

    Kodi_Host = "osmc.home"
    Kodi_Port = 8088

    Kodi_user = "kodi"
    Kodi_pass = "password"

    #Check if user/pass defined
    try:
        Kodi_user
    except NameError:
        Kodi_user = None

    if Kodi_user is None:
        Kodi_URL = 'http://' + Kodi_Host + ":" + str(Kodi_Port)   
    else:
        Kodi_URL = 'http://' + Kodi_user + ":" + Kodi_pass + "@" + Kodi_Host + ":" + str(Kodi_Port) 

    OH2_URL = "http://" + OH2_Host + ":" + str(OH2_Port) + "/rest/items/"

    episodes_api = '{ "jsonrpc": "2.0", "method": "VideoLibrary.GetRecentlyAddedEpisodes", "params": { "properties": [ "showtitle" ]}, "id": 1}'

    enc_api = urllib.quote(episodes_api)

    try:
        response = urllib.urlopen(Kodi_URL + "/jsonrpc?request="+enc_api).read()
    except:
        print "Error connecting to " + Kodi_URL
        sys.exit()

    data = json.loads(response)

    id = 1

    Number_Episodes = len(data['result']["episodes"])

    if Number_Episodes > 5:
        count = 5
    else:
        count = Number_Episodes

    for x in range(0, count):
    
        title = data["result"]["episodes"][x]["showtitle"]
        label = data["result"]["episodes"][x]["label"]

        try:
            OpenHABResponse = requests.post(url=OH2_URL + 'Kodi_title' + str(id), data = title, allow_redirects = True) 
            OpenHABResponse = requests.post(url=OH2_URL + 'Kodi_episode' + str(id), data = label, allow_redirects = True)
            id += 1
        except:
            print "Error connecting to " + OH2_URL
            sys.exit()

if __name__ == '__main__':
    Main()
