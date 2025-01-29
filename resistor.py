# Cece Espadas
# 1-15-25
# ECE 2774: Project 1
# Resistor Class


class Resistor:

    # this is a class that represents a resistor in the simple DC circuit

    # the ATTRIBUTES of the class are defined below:
    # name (str): PROVIDED BY THE USER as an argument when defining the object.
    # bus1 (str): PROVIDED BY THE USER as an argument when defining the object.
    # bus2 (str): PROVIDED BY THE USER as an argument when defining the object.
    # r (float): PROVIDED BY THE USER as an argument when defining the object.
    # g (float): It should be CALCULATED INTERNALLY using the calc_g method

    def __init__(self, name: str, bus1: str, bus2: str, r: float):
        self.name = name  # set the resistor name
        self.bus1 = bus1  # set the first bus as the one that enters the resistor
        self.bus2 = bus2  # set the second bus as the one that that exits the resistor

        self.r = r  # set the resistor value in ohms
        self.g = self.calc_g()  # calculate g immediately

    # the METHOD of the class is defined below:
    # calc_g(): calculates the conductance value (1/R)

    def calc_g(self):
        return 1 / self.r  # calculate conductance based on the resistance

    # this sets a string representation of the resistor object
    # it returns a string representation of the resistor object showing its details

    def __str__(self):
        return f"Resistor (name={self.name}, bus1={self.bus1}, bus2={self.bus2}, resistance={self.r} ohms, conductance={self.g} S)"
