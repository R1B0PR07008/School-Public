"""
Simple demo of the double pendulum simulation.
Run this to see the graphical simulation in action!
"""
import math
import matplotlib.pyplot as plt
from double_pendulum import SimulationState, PendulumParameters, DoublePendulumSimulation


def main():
    """Run a simple double pendulum demo."""
    print("🎯 Double Pendulum Simulation Demo")
    print("=" * 35)
    
    # Create interesting initial conditions
    params = PendulumParameters(
        m1=1.0,    # Equal masses
        m2=1.0, 
        L1=1.0,    # Equal lengths
        L2=1.0,
        g=9.81
    )
    
    # Start with both pendulums horizontal (chaotic!)
    initial_state = SimulationState(
        theta1=math.pi/2,    # 90 degrees
        theta2=math.pi/2,    # 90 degrees
        omega1=0.0,          # Start from rest
        omega2=0.0,
        time=0.0
    )
    
    print("📊 Simulation Parameters:")
    print(f"   Masses: {params.m1} kg, {params.m2} kg")
    print(f"   Lengths: {params.L1} m, {params.L2} m")
    print(f"   Initial angles: {math.degrees(initial_state.theta1):.0f}°, {math.degrees(initial_state.theta2):.0f}°")
    
    print("\n🚀 Starting simulation...")
    print("   Left panel: Pendulum animation with trail")
    print("   Right panel: Energy conservation monitoring")
    print("   Close the window to stop the simulation")
    
    # Create and run simulation
    sim = DoublePendulumSimulation(params, initial_state, dt=0.005)
    
    # Start animation (50 FPS)
    animation = sim.start_animation(interval=20)
    
    # Add title to the figure
    sim.renderer.fig.suptitle('Double Pendulum: Chaos and Energy Conservation', fontsize=14)
    
    # Show the simulation
    sim.show()
    
    print("\n✅ Simulation completed!")


if __name__ == "__main__":
    main()