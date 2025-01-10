
# Bloch Sphere Interactive Tool

## Overview
The **Bloch Sphere Interactive Tool** allows you to visualize quantum states of a qubit on a Bloch sphere in 2D and 3D. It enables users to interactively explore the effects of various quantum gates, such as Pauli-X, Pauli-Y, Pauli-Z, and Hadamard, on a qubit's state. The tool uses Streamlit for an easy-to-use web interface, Matplotlib for 2D and 3D static Bloch sphere plots, and Plotly for an interactive 3D Bloch sphere.

## Features
- **2D Bloch Sphere Projection**: A simple 2D visualization of the quantum state.
- **3D Bloch Sphere Visualization**:
  - Interactive 3D plot using Plotly.
  - Static 3D plot using Matplotlib.
- **Quantum Gate Application**: Apply quantum gates (Pauli-X, Pauli-Y, Pauli-Z, Hadamard) and observe their effects on the qubit's state vector.
- **Quantum State Details**: Display the quantum state vector `|ψ⟩` in terms of the angles `θ` and `φ`, as well as the corresponding Bloch vector coordinates (X, Y, Z).

## LIVE 

Try it now at [Bloc Sphere App](https://blocsphere.streamlit.app/)

## Requirements
- Python 3.7+
- Required libraries:
  - `numpy`
  - `matplotlib`
  - `plotly`
  - `streamlit`

You can install the required libraries using pip:

```bash
pip install numpy matplotlib plotly streamlit
```

## Usage

### Running the Application
To run the application, simply execute the following command in the project directory by cloning the repo:

```bash
streamlit run streamlit_app.py
```

This will open a new tab in your browser with the interactive tool.

### Input Controls
In the sidebar, you can control the following parameters:
- **Theta (rad)**: The polar angle of the quantum state, which defines the rotation of the state vector along the Z-axis.
- **Phi (rad)**: The azimuthal angle of the quantum state, which defines the rotation of the state vector around the Y-axis.
- **Quantum Gate**: Choose from the following quantum gates:
  - **None**: No gate applied (default).
  - **Pauli-X (X)**: Flips the quantum state between `|0⟩` and `|1⟩`.
  - **Pauli-Y (Y)**: Introduces a phase shift along the Y-axis.
  - **Pauli-Z (Z)**: Introduces a phase shift along the Z-axis.
  - **Hadamard**: Puts the qubit in an equal superposition state of `|0⟩` and `|1⟩`.

### Output
Once you adjust the inputs, the following outputs are displayed:
- **2D Bloch Sphere Projection**: A 2D plot of the Bloch sphere showing the state vector.
- **3D Bloch Sphere**:
  - An interactive 3D plot of the Bloch sphere using Plotly.
  - A static 3D plot of the Bloch sphere using Matplotlib.
- **Quantum State**: The quantum state vector `|ψ⟩` in the form of `|0⟩` and `|1⟩`.
- **Bloch Vector**: The X, Y, and Z components of the Bloch vector that represents the quantum state.

## Quantum Gates Description
- **Pauli-X Gate**: Also known as the **NOT gate**, it flips the quantum state between `|0⟩` and `|1⟩`.
- **Pauli-Y Gate**: Introduces a phase shift along the Y-axis, affecting the phase of the qubit's state.
- **Pauli-Z Gate**: Introduces a phase shift along the Z-axis, affecting the relative phase of `|0⟩` and `|1⟩`.
- **Hadamard Gate**: Puts the qubit into a superposition state of `|0⟩` and `|1⟩` with equal probabilities.

## Example of Quantum State Representation

For a given `θ` and `φ`:
```
Quantum State: |ψ⟩ = cos(θ / 2) |0⟩ + (sin(θ / 2) * e^(iφ)) |1⟩
```

The Bloch vector components are calculated as:
```
Bloch Vector: X = sin(θ) * cos(φ), Y = sin(θ) * sin(φ), Z = cos(θ)
```

## Contributing
Contributions to this project are welcome! Please feel free to fork the repository, create an issue, or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **Quantum Computing Concepts**: This tool is based on the Bloch sphere representation of a qubit in quantum mechanics.
- **Streamlit**: Used for creating the interactive web interface.
- **Matplotlib** and **Plotly**: Used for generating visualizations.

---

Enjoy exploring the Bloch Sphere with the Quantum Gates and observe how they manipulate the quantum state!

