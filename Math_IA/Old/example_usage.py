"""
Example usage of the double pendulum data models.
"""
import math
from double_pendulum.models import SimulationState, PendulumParameters, EnergyData, CartesianPositions


def main():
    """Demonstrate basic usage of the data models."""
    print("Double Pendulum Data Models Example")
    print("=" * 40)
    
    # Create pendulum parameters
    print("\n1. Creating pendulum parameters:")
    params = PendulumParameters(m1=2.0, m2=1.5, L1=1.2, L2=0.8)
    print(f"   Mass 1: {params.m1} kg")
    print(f"   Mass 2: {params.m2} kg") 
    print(f"   Length 1: {params.L1} m")
    print(f"   Length 2: {params.L2} m")
    print(f"   Gravity: {params.g} m/s²")
    
    is_valid, error = params.validate()
    print(f"   Parameters valid: {is_valid}")
    
    # Create simulation state
    print("\n2. Creating simulation state:")
    state = SimulationState(
        theta1=math.pi/4,    # 45 degrees
        theta2=-math.pi/6,   # -30 degrees
        omega1=0.5,          # rad/s
        omega2=-0.3,         # rad/s
        time=0.0
    )
    
    print(f"   Angle 1: {state.theta1:.3f} rad ({math.degrees(state.theta1):.1f}°)")
    print(f"   Angle 2: {state.theta2:.3f} rad ({math.degrees(state.theta2):.1f}°)")
    print(f"   Angular velocity 1: {state.omega1:.3f} rad/s")
    print(f"   Angular velocity 2: {state.omega2:.3f} rad/s")
    print(f"   Time: {state.time:.3f} s")
    
    # Test angle normalization
    print("\n3. Testing angle normalization:")
    large_angle_state = SimulationState(
        theta1=5*math.pi,    # Large angle
        theta2=-7*math.pi/2, # Large negative angle
        omega1=0, omega2=0, time=0
    )
    
    print(f"   5π normalizes to: {large_angle_state.theta1:.3f} rad")
    print(f"   -7π/2 normalizes to: {large_angle_state.theta2:.3f} rad")
    
    # Array conversion
    print("\n4. Array conversion:")
    array = state.to_array()
    print(f"   State as array: {[f'{x:.3f}' for x in array]}")
    
    reconstructed = SimulationState.from_array(array, state.time)
    print(f"   Reconstructed θ1: {reconstructed.theta1:.3f}")
    
    # Energy data
    print("\n5. Energy data example:")
    energy = EnergyData(
        kinetic=5.2,
        potential=3.8,
        total=9.0,
        conservation_error=0.0005,
        timestamp=1.0
    )
    
    print(f"   Kinetic energy: {energy.kinetic:.3f} J")
    print(f"   Potential energy: {energy.potential:.3f} J")
    print(f"   Total energy: {energy.total:.3f} J")
    print(f"   Conservation error: {energy.conservation_percentage:.3f}%")
    print(f"   Energy conserved: {energy.is_conserved()}")
    
    # Cartesian positions
    print("\n6. Cartesian positions:")
    # Convert angles to positions (simplified calculation)
    x1 = params.L1 * math.sin(state.theta1)
    y1 = -params.L1 * math.cos(state.theta1)
    x2 = x1 + params.L2 * math.sin(state.theta2)
    y2 = y1 - params.L2 * math.cos(state.theta2)
    
    positions = CartesianPositions(x1=x1, y1=y1, x2=x2, y2=y2)
    print(f"   Bob 1 position: ({positions.x1:.3f}, {positions.y1:.3f})")
    print(f"   Bob 2 position: ({positions.x2:.3f}, {positions.y2:.3f})")
    
    pos_tuples = positions.get_positions()
    print(f"   As tuples: {pos_tuples}")


if __name__ == "__main__":
    main()