from django import template

register = template.Library()

def right_ascension(ra, max):
    return float(ra) / 24.0 * max
    
def declination(dec, max):
    return (float(dec)-90.0) / -180.0 * max

def stellar_radius(radius):
    return (float(radius)*1000)

register.filter('right_ascension', right_ascension)
register.filter('declination', declination)
register.filter('stellar_radius', stellar_radius)