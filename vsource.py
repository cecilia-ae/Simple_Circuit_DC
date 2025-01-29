# Cece Espadas
# 1-15-25
# ECE 2774: Project 1
# VSource Class

class VSource:
    # this is a class that represents the voltage source in the simple DC circuit

    # the ATTRIBUTES of the class are defined below:
    # name (str): PROVIDED BY THE USER as an argument when defining the object
    # bus1 (str): PROVIDED BY THE USER as an argument when defining the object
    # v (float): PROVIDED BY THE USER as an argument when defining the object

    def __init__(self, name: str, bus1: str, v: float):
        self.name = name  # set the Vsource name
        self.bus1 = bus1  # set the first bus as the one that enters the resistor
        self.v = v  # set the source voltage

    # the METHOD of the class is defined below:
    # there is no method for this!


    # this sets a string representation of the VSource object
    # it returns a string representation of the VSource object showing its name, bus, and voltage

    def __repr__(self):
        return f"VSource (name={self.name}, bus1={self.bus1}, v={self.v})"  # return the information about the voltage source