import sys, os
import re
import pycountry_convert as pc

passes = ["North A",	"South A",	"Europe",	"Asia", 	"Afria",	"Australia"]
counts = [0,0,0,0,0,0]

with open("data.csv", "r") as a_file:
    next(a_file)
    for line in a_file:

        split = line.split(",")
        # print(split)
        country = split[1].split("\"")[1]
        # print(country)
        if(split[5] != ''):
            totalNumberOfDeaths = int(split[5])
        else: 
            totalNumberOfDeaths = 0
        # print(totalNumberOfDeaths)
        if(country != "United States"):
            country_code = pc.country_name_to_country_alpha2(country, cn_name_format="default")
            continent_name = pc.country_alpha2_to_continent_code(country_code)
            if(continent_name == "NA"):
                counts[0]+= totalNumberOfDeaths
            if(continent_name == "SA"):
                counts[1]+= totalNumberOfDeaths
            if(continent_name == "EU"):
                counts[2]+= totalNumberOfDeaths
            if(continent_name == "AS"):
                counts[3]+= totalNumberOfDeaths
            if(continent_name == "AF"):
                counts[4]+= totalNumberOfDeaths
            if(continent_name == "OC"):
                counts[5]+= totalNumberOfDeaths
        else:
            print("United States:" + str(totalNumberOfDeaths))
    print(passes)
    print(counts)
            # print(continent_name)
            # print(totalNumberOfDeaths)
        
        