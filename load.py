# Cece Espadas
# 1-15-25
# ECE 2774: Project 1
# Load Class

class Load:
    # this is a class that represents the load in the simple DC circuit

    # the ATTRIBUTES of the class are defined below:
    # name (str): PROVIDED BY THE USER as an argument when defining the object.
    # bus1 (str): PROVIDED BY THE USER as an argument when defining the object.
    # p (float): PROVIDED BY THE USER as an argument when defining the object.
    # v (float): PROVIDED BY THE USER as an argument when defining the object.

    # r (float): It should be CALCULATED INTERNALLY using the calc_g method
    # g (float): It should be CALCULATED INTERNALLY using the calc_g method

    def __init__(self, name: str, bus1: str, p: float, v: float):
        self.name = name  # set the load name
        self.bus1 = bus1  # set the bus1 as the one that enters the load
        self.p = p  # set the real power value in watts
        self.v = v  #set the voltage for the load in volts
        self.g = self.calc_g() #set to zero, the method will calculate this
        self.r = self.calc_r() #set to zero, the method will calculate this

    # the METHOD of the class is defined below:
        # calc_g(): calculates the conductance value as a function of real power, reactive power, and voltage

    def calc_g(self):
        return self.p/(self.v ** 2) # calculate conductance based on the R

    def calc_r(self ):
        return (self.v ** 2)/self.p


    # this sets a string representation of the load object and returns it showing details

    def __str__(self):
        return f"Load (name={self.name}, bus1={self.bus1}, real power={self.p} W, voltage={self.v} V, resistance = {self.r} ohms, conductance={self.g} S)"
