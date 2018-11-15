import requests
import re
import maya.cmds as cmds

#This program takes a float from a live data set and scales it to the range
#0 to 1, which is the range of the incandescence attibrute on the "lightbulb" object
#in Maya. It then sets the incandescence attribute to the value of the scaled
#float

#here: imports data from an api and uses regex to parse out a single value
headers = {
  'Accept': 'application/json'
}

whole_data = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)
data_text = str(whole_data.json())

data_text_1stpass = str(re.findall(r'\'actual\': \w\w\w\b', data_text))
data_text_2ndpass = re.findall(r'\d\d\d', data_text_1stpass)
population = int(data_text_2ndpass[0])

#here: takes the value parsed through regex and uses it to set the
#      relative incandescence of the LifeBulb
max = 500
incand = population/max

cmds.setAttr("bulbShade.incandescence",incand,incand,incand, type="double3")
cmds.render("renderCam")
