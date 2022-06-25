# This file solves 5.1
# Solution for 5.2 and 5.3 can be found at ../modules/legb.py

import sys
import os

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(PROJECT_PATH)

from modules import legb

func = legb.enclosing_funcion()
func()