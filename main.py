# -*- coding: utf-8 -*-

import numpy as np

print("Hugues")

class Ride:
    def __init__(self,ride):
        self.start = [int(ride[0]), int(ride[1])]
        self.end = [int(ride[2]), int(ride[3])]
        self.step_start = int(ride[4])
        self.step_end = int(ride[5])
        self.to_do = True
        
