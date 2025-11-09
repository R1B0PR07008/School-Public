# Design Document

## Overview

The double pendulum simulation implements a physics-accurate model using Lagrangian mechanics with symplectic numerical integration to ensure energy conservation. The system consists of a physics engine, visualization components, and real-time energy monitoring, built using Python with matplotlib for visualization and numpy for numerical computations.

## Architecture

The simulation follows a modular architecture with clear separation between physics calculations, numerical integration, visualization, and user interface components:

```
DoublePendulumSimulation
├── PhysicsEngine
│   ├── LagrangianSolver
│   ├── SymplecticIntegrator
│   └── EnergyCalculator
├── Visualization
│   ├── AnimationRenderer
│   └── EnergyPlotter
├── ParameterManager
└── SimulationController
```

## Components and Interfaces

### PhysicsEngine Class
**Purpose:** Core physics calculations and state management
**Key Methods:**
- `calculate_derivatives(state, t)`: Computes angular accelerations using Lagrangian equations
- `get_cartesian_positions()`: Converts angular coordinates to (x,y) positions for rendering
- `update_state(dt)`: Advances system state by one time step using symplectic integration

**State Vector:** `[θ1, θ2, ω1, ω2]` where θ represents angles and ω represents angular velocities

### LagrangianSolver Class
**Purpose:** Implements the equations of motion for the double pendulum
**Physics Implementation:**
- Lagrangian: L = T - V (kinetic minus potential energy)
- Kinetic Energy: T = ½m₁v₁² + ½m₂v₂²
- Potential Energy: V = -m₁gL₁cos(θ₁) - m₂g(L₁cos(θ₁) + L₂cos(θ₂))
- Equations of motion derived from Euler-Lagrange equations

**Key Methods:**
- `compute_accelerations(theta1, theta2, omega1, omega2)`: Returns [α₁, α₂] angular accelerations
- `get_coupling_matrix()`: Returns the mass-coupling matrix for the system

### SymplecticIntegrator Class
**Purpose:** Numerical integration preserving energy conservation
**Algorithm:** Velocity Verlet (symplectic, 2nd order accurate)
```
θ(t+dt) = θ(t) + ω(t)dt + ½α(t)dt²
ω(t+dt) = ω(t) + ½[α(t) + α(t+dt)]dt
```

**Key Methods:**
- `step(state, dt)`: Advances state by one time step
- `adaptive_timestep(state, target_error)`: Adjusts dt to maintain accuracy

### EnergyCalculator Class
**Purpose:** Real-time energy monitoring and conservation verification
**Energy Components:**
- Kinetic Energy: T = ½(m₁ + m₂)L₁²ω₁² + ½m₂L₂²ω₂² + m₂L₁L₂ω₁ω₂cos(θ₁-θ₂)
- Potential Energy: V = -(m₁ + m₂)gL₁cos(θ₁) - m₂gL₂cos(θ₂)
- Total Energy: E = T + V

**Key Methods:**
- `calculate_kinetic_energy(state)`: Returns current kinetic energy
- `calculate_potential_energy(state)`: Returns current potential energy
- `get_energy_drift()`: Monitors energy conservation accuracy

### AnimationRenderer Class
**Purpose:** Real-time visualization of pendulum motion
**Rendering Elements:**
- Pendulum rods (lines connecting pivot points and masses)
- Pendulum masses (circles with configurable size and color)
- Trajectory trails (optional path tracing)
- Coordinate system and scale indicators

**Key Methods:**
- `update_frame(positions)`: Updates visual elements for current frame
- `set_trail_length(length)`: Configures trajectory trail persistence
- `configure_appearance(colors, sizes)`: Customizes visual styling

### EnergyPlotter Class
**Purpose:** Real-time energy monitoring visualization
**Plot Components:**
- Time-series plots for kinetic, potential, and total energy
- Energy conservation error tracking
- Real-time numerical energy values display

**Key Methods:**
- `update_energy_plots(time, energies)`: Updates all energy visualizations
- `highlight_conservation_violations(threshold)`: Visual alerts for energy drift
- `reset_plots()`: Clears plot history for new simulation runs

## Data Models

### SimulationState
```python
@dataclass
class SimulationState:
    theta1: float      # Angle of first pendulum (radians)
    theta2: float      # Angle of second pendulum (radians)
    omega1: float      # Angular velocity of first pendulum (rad/s)
    omega2: float      # Angular velocity of second pendulum (rad/s)
    time: float        # Current simulation time (s)
```

### PendulumParameters
```python
@dataclass
class PendulumParameters:
    m1: float = 1.0    # Mass of first pendulum (kg)
    m2: float = 1.0    # Mass of second pendulum (kg)
    L1: float = 1.0    # Length of first rod (m)
    L2: float = 1.0    # Length of second rod (m)
    g: float = 9.81    # Gravitational acceleration (m/s²)
    
    def validate(self) -> bool:
        return all(val > 0 for val in [self.m1, self.m2, self.L1, self.L2, self.g])
```

### EnergyData
```python
@dataclass
class EnergyData:
    kinetic: float
    potential: float
    total: float
    conservation_error: float
    timestamp: float
```

## Error Handling

### Numerical Stability
- **Adaptive Time Stepping:** Automatically reduces dt when energy drift exceeds threshold (0.1%)
- **Singularity Detection:** Monitors for near-singular configurations in coupling matrix
- **Overflow Protection:** Validates that angular velocities remain within reasonable bounds

### Parameter Validation
- **Physical Constraints:** Ensures all masses and lengths are positive
- **Initial Condition Bounds:** Validates initial angles are within [-2π, 2π]
- **Numerical Limits:** Prevents parameters that could cause numerical instability

### User Input Handling
- **Real-time Validation:** Immediate feedback for invalid parameter inputs
- **Graceful Degradation:** Continues simulation with previous valid parameters if new ones are invalid
- **Error Messages:** Clear, actionable error messages for constraint violations

## Testing Strategy

### Unit Tests
- **Physics Accuracy:** Verify equations of motion against analytical solutions for small angles
- **Energy Conservation:** Test energy drift over extended simulations (< 0.1% over 10,000 steps)
- **Numerical Integration:** Compare symplectic integrator against reference implementations
- **Parameter Validation:** Test boundary conditions and invalid input handling

### Integration Tests
- **End-to-End Simulation:** Full simulation runs with various initial conditions
- **Performance Testing:** Ensure real-time performance (>30 FPS) for typical parameter ranges
- **Energy Monitoring:** Verify energy plots update correctly and highlight conservation violations
- **User Interface:** Test all simulation controls (start, pause, reset, parameter changes)

### Validation Tests
- **Physical Realism:** Compare simulation results with known double pendulum behaviors
- **Chaos Verification:** Confirm sensitive dependence on initial conditions
- **Conservation Laws:** Extended runs to verify long-term energy conservation
- **Limiting Cases:** Test behavior approaching single pendulum and other limiting configurations