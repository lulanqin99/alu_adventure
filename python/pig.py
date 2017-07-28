city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomás Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }

#city = raw_input('City':)


for city in city_info:
    for item in city_info[city]:
    print 'The' + item + 'of'+ city 'is' + str(city_info[city][item])
