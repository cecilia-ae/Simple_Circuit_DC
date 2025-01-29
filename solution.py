# Cece Espadas
# 1-21-25
# ECE 2774: Project 1
# Solution Class

from circuit import Circuit

class Solution:
# this is a class that represents the voltage source in the simple DC circuit

    # the ATTRIBUTES of the class are defined below:
    # circuit (Circuit): When creating a solution object, you must pass a Circuit object as an argument

    def __init__(self, circuit: Circuit):

        if not isinstance(circuit, Circuit):
            raise TypeError("The 'circuit' argument must be a Circuit object.")

        self.circuit = circuit


    def do_power_flow(self):
        # solves the circuit by finding bus voltages and circuit current
            # calculate the total conductance in the circuit from the resistors and loads
            # calculate the current using ohm's Law (I = V * total_g)
            # determine the voltage at busses (using I and resistor conductance)

        if not self.circuit.vsource:
            raise ValueError("Voltage source needed to perform power flow calculation.")

        total_r = 0

        # conductance of resistors
        for resistor in self.circuit.resistors.values():
            total_r += resistor.r

        # conductance of loads
        for load in self.circuit.loads.values():
            total_r += load.r

        total_g = 1/total_r

        # calculate the current
        voltage = self.circuit.vsource.v  # Voltage from the source
        current = voltage * total_g
        self.circuit.set_i(current)

        #determine the voltage at each bus

        # set voltage of bus A equal to the source
        source_bus = self.circuit.vsource.bus1
        self.circuit.buses[source_bus].set_bus_v(voltage)
        current_voltage = voltage

        # loop through resistors to calculate voltage at each connected bus
        for resistor in self.circuit.resistors.values():
            # calculate the voltage drop across the resistor, v =ir
            voltage_drop = current * resistor.r

            # update the voltage for the next bus
            current_voltage -= voltage_drop

            # set the voltage of the second bus of the resistor
            self.circuit.buses[resistor.bus2].set_bus_v(current_voltage)
