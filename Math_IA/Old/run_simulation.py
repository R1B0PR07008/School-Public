"""
Complete double pendulum simulation with matplotlib visualization.
"""
import math
import matplotlib.pyplot as plt
from double_pendulum import (
    SimulationState, 
    PendulumParameters, 
    DoublePendulumSimulation
)


def create_chaotic_initial_conditions():
    """Create initial conditions that demonstrate chaotic behavior."""
    return SimulationState(
        theta1=math.pi/2,      # 90 degrees
        theta2=math.pi/2,      # 90 degrees  
        omega1=0.0,            # Start from rest
        omega2=0.0,            # Start from rest
        time=0.0
    )


def create_custom_parameters():
    """Create custom pendulum parameters."""
    return PendulumParameters(
        m1=1.0,    # 1 kg
        m2=1.0,    # 1 kg
        L1=1.0,    # 1 meter
        L2=1.0,    # 1 meter
        g=9.81     # Earth gravity
    )


def main():
    """Run the double pendulum simulation."""
    print("Double Pendulum Simulation")
    print("=" * 30)
    
    # Create parameters and initial state
    params = create_custom_parameters()
    initial_state = create_chaotic_initial_conditions()
    
    print(f"Parameters:")
    print(f"  Mass 1: {params.m1} kg")
    print(f"  Mass 2: {params.m2} kg")
    print(f"  Length 1: {params.L1} m")
    print(f"  Length 2: {params.L2} m")
    print(f"  Gravity: {params.g} m/s²")
    
    print(f"\nInitial Conditions:")
    print(f"  Angle 1: {math.degrees(initial_state.theta1):.1f}°")
    print(f"  Angle 2: {math.degrees(initial_state.theta2):.1f}°")
    print(f"  Angular velocity 1: {initial_state.omega1:.3f} rad/s")
    print(f"  Angular velocity 2: {initial_state.omega2:.3f} rad/s")
    
    # Create and start simulation
    print(f"\nStarting simulation...")
    print(f"Controls:")
    print(f"  - Close window to stop")
    print(f"  - Watch the energy conservation in real-time!")
    
    simulation = DoublePendulumSimulation(
        params=params,
        initial_state=initial_state,
        dt=0.01  # 10ms time step
    )
    
    # Start animation
    anim = simulation.start_animation(interval=20)  # 50 FPS
    
    # Show the simulation
    simulation.show()


if __name__ == "__main__":
    main()