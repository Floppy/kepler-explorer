from django import template
from math import pi, sin, cos
from decimal import Decimal

register = template.Library()

def right_ascension(ra, max):
    return float(ra) / 24.0 * max

@register.simple_tag
def xpos(ra, dec, max):
    r, theta = get_r_theta(ra, dec)
    if(dec >= 0):
        offset = 0.25
    else:
        offset = 0.75
    return Decimal(max)*(Decimal(offset) + Decimal(0.25)*r*Decimal(sin(theta)))


@register.simple_tag
def ypos(ra, dec, max):
    r, theta = get_r_theta(ra, dec)
    offset = 0.5
    return Decimal(max)*(Decimal(offset) + Decimal(0.5)*r*Decimal(cos(theta)))

def get_r_theta(ra, dec):
    if(dec > 0):
        theta = Decimal(pi) - ra * Decimal(2*pi / 24.0)
    else:
        theta = Decimal(pi) + ra * Decimal(2*pi / 24.0)
    r = (Decimal(90) - abs(dec)) / Decimal(90.0)
    return [r, theta]

def declination(dec, max):
    return (float(dec)-90.0) / -180.0 * max

def stellar_radius(radius):
    return (float(radius)*1000)

register.filter('right_ascension', right_ascension)
register.filter('declination', declination)
register.filter('stellar_radius', stellar_radius)