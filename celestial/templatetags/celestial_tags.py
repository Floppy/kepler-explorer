from django import template

register = template.Library()

def right_ascension(ra, max):
    return float(ra) / 24.0 * max
    
def declination(dec, max):
    return (float(dec)-90.0) / -180.0 * max

register.filter('right_ascension', right_ascension)
register.filter('declination', declination)