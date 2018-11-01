""" LIVE DATA (INCLUDES CURRENT POPULATION OF SPECIES)
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('https://api.carbonintensity.org.uk/intensity', params={}, headers = headers)

print r.json()
"""
import maya.cmds as cmds

species_population = 0 #will retrieve number from regex parsing of live data

#This function takes a float from a live data set and scales it to the range
#0 to 1, which is the range of the intensity attibrute on the light object
#in Maya. It then sets the intensity attribute to the value of the scaled
#argument

def bulb_intensity(population): #takes a float
    """ *FILLER*
    if population > 5:
        mc.polySphere(r=1.5, sx=25, sy=25, ax=[0,1,0], ch=1)
    """
    return #returns nothing

bulb_intensity(species_population)
