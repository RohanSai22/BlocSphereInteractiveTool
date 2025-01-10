import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit as st

# Utility: Calculate Bloch Sphere Coordinates
def bloch_sphere_coordinates(theta, phi):
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return x, y, z

# Utility: Apply Quantum Gate
def apply_quantum_gate(vector, gate):
    """Apply a quantum gate to a Bloch vector."""
    x, y, z = vector
    if gate == "X (Pauli-X)":
        return x, -y, -z
    elif gate == "Y (Pauli-Y)":
        return -x, y, -z
    elif gate == "Z (Pauli-Z)":
        return -x, -y, z
    elif gate == "Hadamard":
        new_x = (x + z) / np.sqrt(2)
        new_z = (z - x) / np.sqrt(2)
        return new_x, y, new_z
    return x, y, z

# Plot: 2D Bloch Sphere
def plot_bloch_2d(ax, vector):
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True)
    ax.add_artist(plt.Circle((0, 0), 1, color='cyan', alpha=0.2))
    ax.arrow(0, 0, vector[0], vector[1], color='purple', head_width=0.1, linewidth=2)
    ax.set_title("2D Bloch Sphere Projection", fontsize=14)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

# Plot: 3D Bloch Sphere with Plotly
def plot_bloch_plotly(vector):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    sphere = go.Surface(
        x=x, y=y, z=z,
        colorscale=[[0, 'cyan'], [1, 'cyan']],
        opacity=0.2, showscale=False
    )

    vector_trace = go.Cone(
        x=[0], y=[0], z=[0],
        u=[vector[0]], v=[vector[1]], w=[vector[2]],
        colorscale='Purples',
        sizemode='absolute',
        sizeref=0.2
    )

    layout = go.Layout(
        title="3D Bloch Sphere (Interactive)",
        scene=dict(
            xaxis=dict(range=[-1, 1], title="X-axis"),
            yaxis=dict(range=[-1, 1], title="Y-axis"),
            zaxis=dict(range=[-1, 1], title="Z-axis"),
            aspectmode='cube'
        )
    )

    fig = go.Figure(data=[sphere, vector_trace], layout=layout)
    return fig

# Plot: 3D Bloch Sphere with Matplotlib
def plot_bloch_3d(ax, vector):
    # Create the Bloch sphere (unit sphere)
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the sphere
    ax.plot_surface(x, y, z, color='cyan', alpha=0.2, rstride=4, cstride=4)

    # Plot the Bloch vector as a cone
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2], color='purple', length=1.1, normalize=True)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("3D Bloch Sphere", fontsize=14)

# Main Streamlit App
def main():
    st.title("Advanced Bloch Sphere Visualization")
    st.sidebar.title("Quantum State Controls")

    # Sidebar: Input Controls
    theta = st.sidebar.slider("Theta (rad)", 0.0, np.pi, np.pi / 2, step=0.01)
    phi = st.sidebar.slider("Phi (rad)", 0.0, 2 * np.pi, np.pi / 2, step=0.01)
    gate = st.sidebar.selectbox("Quantum Gate", ["None", "X (Pauli-X)", "Y (Pauli-Y)", "Z (Pauli-Z)", "Hadamard"])

    # Calculate initial Bloch vector
    x, y, z = bloch_sphere_coordinates(theta, phi)
    initial_vector = (x, y, z)

    # Apply quantum gate if selected
    if gate != "None":
        x, y, z = apply_quantum_gate(initial_vector, gate)
        st.sidebar.write(f"Applied {gate} Gate")

    # 2D Plot
    st.write("### 2D Bloch Sphere Projection")
    fig2d, ax2d = plt.subplots(figsize=(6, 6))
    plot_bloch_2d(ax2d, (x, y))
    st.pyplot(fig2d)

    # 3D Plot with Plotly
    st.write("### 3D Bloch Sphere (Interactive with Plotly)")
    plotly_fig = plot_bloch_plotly((x, y, z))
    st.plotly_chart(plotly_fig)

    # 3D Plot with Matplotlib
    st.write("### 3D Bloch Sphere (Matplotlib)")
    fig3d = plt.figure(figsize=(8, 8))
    ax3d = fig3d.add_subplot(111, projection="3d")
    plot_bloch_3d(ax3d, (x, y, z))
    st.pyplot(fig3d)

    # State vector details
    st.write(f"### Quantum State: |\u03C8⟩ = {np.cos(theta / 2):.2f} |0⟩ + ({np.sin(theta / 2) * np.exp(1j * phi):.2f}) |1⟩")
    st.write(f"### Bloch Vector: X = {x:.2f}, Y = {y:.2f}, Z = {z:.2f}")

    # Quantum State Description
    st.markdown("""
    The **Bloch sphere** is a geometric representation of the quantum state of a qubit.
    It provides a visualization of the **superposition** and **entanglement** of quantum states.
    The **quantum gates** manipulate the qubit's state vector, rotating it on the Bloch sphere, which leads to different quantum outcomes.

    - The **Pauli-X gate** (also known as the NOT gate) flips the state between |0⟩ and |1⟩.
    - The **Pauli-Y and Pauli-Z gates** introduce phase shifts along the Y and Z axes, respectively.
    - The **Hadamard gate** puts the qubit in an equal superposition state of |0⟩ and |1⟩.

    Adjust the sliders and apply quantum gates to explore how these operations affect the qubit's state.
    """)

if __name__ == "__main__":
    main()
