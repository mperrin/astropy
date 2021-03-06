# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
This package defines colloquially used Imperial units.  They are also
available in the `astropy.units` namespace.

"""
from __future__ import absolute_import, division, print_function, unicode_literals

from .core import UnitBase, def_unit
from . import si

UnitBase._set_namespace(globals())

###########################################################################
# LENGTH

def_unit(['inch'], 2.54 * si.cm, register=True,
         doc="International inch")
def_unit(['ft', 'foot'], 12 * inch, register=True,
         doc="International foot")
def_unit(['yd', 'yard'], 3 * ft, register=True,
         doc="International yard")
def_unit(['mi', 'mile'], 5280 * ft, register=True,
         doc="International mile")


###########################################################################
# AREAS

def_unit(['ac', 'acre'], 43560 * ft ** 2, register=True,
         doc="International acre")


###########################################################################
# VOLUMES

def_unit(['gallon'], si.liter / 0.264172052, register=True,
         doc="U.S. liquid gallon")
def_unit(['quart'], gallon / 4, register=True,
         doc="U.S. liquid quart")
def_unit(['pint'], quart / 2, register=True,
         doc="U.S. liquid pint")
def_unit(['cup'], pint / 2, register=True,
         doc="U.S. customary cup")
def_unit(['foz', 'fluid_oz', 'fluid_ounce'], cup / 8, register=True,
         doc="U.S. fluid ounce")
def_unit(['tbsp', 'tablespoon'], foz / 2, register=True,
         doc="U.S. customary tablespoon")
def_unit(['tsp', 'teaspoon'], tbsp / 3, register=True,
         doc="U.S. customary teaspoon")


###########################################################################
# MASS

# Imperial measurements
# well, force actually, but who uses it that way?
def_unit(['oz', 'ounce'], 28.349523125 * si.g, register=True,
         doc="International avoirdupois ounce")
def_unit(['lb', 'pound'], 16 * oz, register=True,
         doc="International avoirdupois pound")
def_unit(['ton'], 2000 * lb, register=True,
         doc="International avoirdupois ton")


##########################################################################
# ENERGY

def_unit(['BTU', 'btu'], 1.05505585 * si.kJ, register=True,
         doc="British thermal unit")
def_unit(['cal', 'calorie'], 4.184 * si.J, register=True,
         doc="Thermochemical calorie: pre-SI metric unit of energy")
def_unit(['kcal', 'Cal', 'Calorie', 'kilocal', 'kilocalorie'],
         1000 * cal, register=True,
         doc="Calorie: colloquial definition of Calorie")


###########################################################################
# POWER

# Imperial units
def_unit(['hp', 'horsepower'], si.W / 0.00134102209, register=True,
         doc="Electrical horsepower")


###########################################################################
# CLEANUP

del UnitBase
del def_unit


###########################################################################
# DOCSTRING

# This generates a docstring for this module that describes all of the
# standard units defined here.
from .utils import generate_unit_summary as _generate_unit_summary
__doc__ += _generate_unit_summary(globals())
