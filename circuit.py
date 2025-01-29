# Cece Espadas
# 1-16-25
# ECE 2774: Project 1
# Circuit Class

from typing import Dict

# import all the other classes
from bus import Bus
from resistor import Resistor
from vsource import VSource
from load import Load

class Circuit:

    # this is a class that represents the voltage source in the simple DC circuit
    # the ATTRIBUTES of the class are defined below:

    # name (str): PROVIDED BY THE USER as an argument when defining the object

    # buses (Dict[str, Bus]): dict, each item has a bus name as key and bus object as value
    # bus object created using add_resistor method
    # resistors (Dict[str, Resistor]): dict, each item has a resistor name as key and resistor object as value
    # resistor object created using add_resistor method
    # loads (Dict[str, Load]): dict, each item has a load name as key and load object as value
    # load object created using the add_load method

    # vsource (Vsource): VSource object, created using the add_vsource
    # i (float): current flowing through the circuit, updated during the power flow calculation

    def __init__(self, name: str):
        self.name = name  # set the circuit name
        self.buses: Dict[str, Bus] = {}
        self.resistors: Dict[str, Resistor] = {}
        self.loads: Dict[str, Load] = {}
        self.vsource: VSource = None #set to none, the method will add this with add_vsource
        self.i: float = 0.0 #set to zero, the method will calculate this with the power flow calculation

    # the METHODS of the class are defined below:

    # add_bus(bus: str): Adds a bus to the circuit.
    # add_resistor_element(name: str, bus1: str, bus2: str, r: float): Adds a resistor to the circuit.
    # add_load_element(name: str, bus1: str, p: float, v: float): Adds a load to the circuit.
    # add_vsource_element(name: str, bus1: str, v: float): Adds a voltage source to the circuit.

    # set_i(i: float): Updates the i attribute.

    # print_nodal_voltage(): Prints voltages at all buses.
    # print_circuit_current(): Prints circuit current.

    def add_bus(self, bus_name: str):
        # adds a new bus object to the buses dictionary of the circuit object

        # check if the bus already exists in the dictionary
        if bus_name in self.buses:
            raise ValueError(f"Bus '{bus_name}' already exists.")


        # add the bus
        self.buses[bus_name] = Bus(bus_name)


    def add_resistor_element(self, name: str, bus1: str, bus2: str, r: float):
        # adds a new resistor object to the resistors dictionary of the circuit object

        if name in self.resistors:
            raise ValueError(f"Resistor '{name}' already exists.")
        if bus1 not in self.buses or bus2 not in self.buses:
            raise ValueError("Both buses must exist before adding a resistor.")

        #add the resistor
        # create the load object
        resistor = Resistor(name, bus1, bus2, r)

        self.resistors[name] = resistor


    def add_load_element(self, name: str, bus1: str, p: float, v: float):
        #adds the load object to the loads dictionary of the circuit object

        if name in self.loads:
            raise ValueError(f"Load '{name}' already exists.")
        if bus1 not in self.buses:
            raise ValueError("Bus must exist before adding a load.")

        #add the load
        # create the load object
        load = Load(name, bus1, p, v)

        # add the load
        self.loads[load.name] = load


    def add_vsource_element(self, name: str, bus1: str, v: float):
        # adds the voltage source

        if self.vsource:
            raise ValueError("A voltage source already exists in the circuit.")
        if bus1 not in self.buses:
            raise ValueError("Bus must exist before adding a voltage source.")

        self.vsource = VSource(name, bus1, v)

    def set_i(self, i: float):
        # calculates and sets the current in the circuit

        if not self.vsource:
            raise ValueError("Voltage source required.")

        self.i = i



    def print_nodal_voltage(self):

        for bus_name, bus in self.buses.items():
            print(f"{bus_name} voltage = {bus.v:.2f} V")

    def print_circuit_current(self):

        print(f"Circuit Current: {self.i:.2f} A")

    def __repr__(self):
        return f"Circuit(name={self.name}, buses={self.buses}, resistors={self.resistors}, loads={self.loads}, vsource={self.vsource}, i={self.i})"
