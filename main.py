# Cece Espadas
# 1-29-25
# ECE 2774: Project 1
# Main Code


from circuit import Circuit
from solution import Solution


# create the Circuit object
circuit = Circuit("MyCircuit")

# Add components to the circuit
circuit.add_bus("BusA")
circuit.add_bus("BusB")
circuit.add_vsource_element("Va", "BusA", 100)
circuit.add_resistor_element("R1", "BusA", "BusB", 5)
circuit.add_load_element("Lb", "BusB", 2000, 50)

# Create the solution object
solution = Solution(circuit)

# Perform the power flow calculation
solution.do_power_flow()

# Print the results
solution.circuit.print_nodal_voltage()
solution.circuit.print_circuit_current()
