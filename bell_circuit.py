import stim

print(stim.__version__)

circuit = stim.Circuit()

# Initialise a Bell pair
circuit.append("H", [0])
circuit.append("CNOT", [0, 1])

# Measure both qubits in Z basis
circuit.append("M", [0, 1])

# Display the circuit
circuit.diagram('timeline-svg')