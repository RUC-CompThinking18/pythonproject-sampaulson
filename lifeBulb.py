import re
from datetime import date

#As reported by BBC on August 23, 2011 (https://www.bbc.com/news/science-environment-14616161),
#scientists estimate that the natural world contains about 8.7 mil species
date0 = date(2011, 8, 23)
num_of_species_at_date0 = 8700000.0

#This function calculates the number of days that have passed
#since it was determined that there are ~8.7 extant species
def days_since_date0():
    date_current = date.today()
    time_since_date0 = str(date_current - date0)
    #Since this datetime operation outputs a datetime object, we'll convert
    #it to a string and parse out the number of days that have passed
    #with regex
    days_since_date0_1stpass = str(re.findall(r'\w* days\b', time_since_date0))
    days_since_date0_2ndpass = re.findall(r'\d', days_since_date0_1stpass)

    days = ""
    for element in days_since_date0_2ndpass:
        days += element

    return float(days)

#This function calculates how many species we have lost since August 23, 2011
#and divides that number by 8.7 mil to determine the percentage remaining.
#Because, like percentages, the Lifebulb's incandescence must be a value
#between 0 and 1, the percentage value is used to set the incandescence.
def find_incandescence():
    #The World Wildlife Fund determined that we lose about
    #150 species every day (http://wwf.panda.org/our_work/biodiversity/biodiversity/)
    species_lost_per_day = 150
    species_lost_since_date0 = species_lost_per_day * days_since_date0()
    num_of_species_remaining = num_of_species_at_date0 - species_lost_since_date0
    if num_of_species_remaining <= 0:
        return 0

    incandescence = num_of_species_remaining/num_of_species_at_date0
    return incandescence

incand = find_incandescence()
print incand
#Finally, we'll set the new incandescence of the Lifebulb.
cmds.setAttr("bulbShade.incandescence",incand,incand,incand, type="double3")
#And lastly, we'll render an image of the bulb with its new incandescence.
cmds.render("renderCam")
