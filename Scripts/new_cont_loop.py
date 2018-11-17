import u12
from time import sleep
from time import time
from scipy.integrate import simps
import datetime
import csv
import numpy as np
import sys
sys.path.insert(0, '/home/albert/Documents/Albert Work/Scripts')
from funcs import PID
from thermocouple import temperature_read
from pressure import pressure_read
