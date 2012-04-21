from math import pi, atan2

def weight_on_planet(weight_on_earth, planet_gravity):
    """
    Calculates how much something would weigh on a planet with a given gravity
    
    weight_on_earth - the weight of the object on earth (in unspecified units)
    planet_gravity - acceleration due to gravity on the planet
    
    returns the weight of the object on the planet, in the same units it was given in
    """
    
    return weight_on_earth * (planet_gravity / 9.80665)

def time_to_go_circumnavigate_by_airbus_a380(planet_radius):
    """
    Calculates the time taken to circumnavigate a planet using an Airbus A380
    (travelling at 900km/h)
    
    planet_radius - radius of the planet in m
    
    returns the time in seconds to circumnavigate the planet
    """ 
    
    # 900 km/h = 250 m/s
    circ = 2*pi * planet_radius
    return circ/250.0

def time_to_boil_tea(planet_temperature):
    """
    Calculates the time taken to boil a cup of tea
    
    planet_temperature - the temperature of the planet in K
    
    returns:
        the time in seconds to boil a cup of tea
        OR None if it's too cold
    """
    pass

def time_to_freeze_lolly(planet_temperature):
    """
    Calculates the time taken to freeze an ice lolly
    
    planet_temperature - the temperature of the planet in K
    
    returns:
        the time in seconds to freeze an ice lolly
        OR None if it's too warm
    """
    pass

def age_in_planet_years(age_in_years, planetary_orbit_period):
    """
    Calculates how old you would be if you lived on an exo-planet
    
    age_in_years - the age on Earth, in years
    planetary_orbit_period - the planetary orbital period, in days
    
    returns the age in planet years, i.e. how many times the planet has
    orbitted its star in the time given
    """
    return age_in_years * planetary_orbit_period / 365.256363

def time_to_planet_by_spacecraft(planet_distance):
    """
    Calculates the time to travel to the planet by spacecraft
    This assumes a travelling speed of 62,120km/h (17255.5 m/s), which is the solar
    system espace velocity of Voyager 1
    
    planet_distance - the distance to the planet in parsecs
    
    returns the time in seconds taken to get to the planet
    """
    m_per_parsec = 3.08568025e16
    speed_of_craft = 17255.56
    return planet_distance * m_per_parsec / speed_of_craft

def time_to_planet_by_car(planet_distance):
    """
    Calculates the time to travel to the planet by car
    This assumes a travelling speed of 31.2928m/s (70mph), which is the
    speed limit in the UK
    
    planet_distance - the distance to the planet in parsecs
    
    returns the time in seconds taken to get to the planet
    """
    m_per_parsec = 3.08568025e16
    speed_of_craft = 31.2928
    return planet_distance * m_per_parsec / speed_of_craft

def size_of_star_in_sky(star_radius, star_distance):
    """
    Calculates the size of the star in the sky from the surface of the planet
    
    star_radius - radius of the star
    star_distance - distance to the star
    
    units of radius and distance are unimportant, but must be the same
    
    returns the size of the star in the sky in degrees
    """
    # 2* because we only give radius (not diameter), 180/pi to convert to degrees
    return 2*atan2(star_radius, star_distance)*180/pi

def colour_of_star(temperature):
    """
    Calculates the colour of the star based on its temperature
    
    tmperature - the temperature of the star in K
    
    returns a string representing the HTML colour of the star
    """
    # Colours based on data here:
    # http://outreach.atnf.csiro.au/education/senior/astrophysics/photometry_colour.html
    
    if (temperature > 28000):
        return "#9bb0ff"
    elif (temperature > 10000):
        return "#aabfff"
    elif (temperature > 7500):
        return "#cad7ff"
    elif (temperature > 6000):
        return "#f8f7ff"
    elif (temperature > 4900):
        return "#fff4ea"
    elif (temperature > 3500):
        return "#ffd2a1"
    else:
        return "#ffccdf"

    