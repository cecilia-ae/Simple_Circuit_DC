# Cece Espadas
# 1-15-25
# ECE 2774: Project 1
# Bus Class

class Bus:
    # this is a class that represents a bus in the simple DC circuit

    # the ATTRIBUTES of the class are defined below:
    # name (str): the name of the bus, PROVIDED BY THE USER during object creation.
    # v (float): voltage at the bus, INITIALIZED TO 0.0 BY DEFAULT.  for voltage
    # source-connected buses, the voltage is updated when the source is created.
    # for other buses, it updates during the power flow calculation.

    def __init__(self, name: str, v: float = 0.0):
        self.name = name  # set the bus name
        self.v = v  # set the initial voltage (defaults to 0.0 if not provided)

    # the METHOD of the class is defined below:
    # set_bus_v(bus_v: float): sets the voltage at the bus.

    def set_bus_v(self, bus_v: float):
        self.v = bus_v  # set the voltage value for the bus

    # this sets a string representation of the bus object
    # it returns a string representation of the bus object showing its name and voltage

    def __repr__(self):
        return f"Bus (name={self.name}, v={self.v})"  # return the information about the bus
