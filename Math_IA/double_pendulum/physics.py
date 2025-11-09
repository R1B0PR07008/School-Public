"""
Physics engine for double pendulum simulation using Lagrangian mechanics.
"""
import numpy as np
import math
from typing import List
from .models import SimulationState, PendulumParameters, EnergyData, CartesianPositions


class LagrangianSolver:
    """Implements the equations of motion for the double pendulum using Lagrangian mechanics."""
    
    def __init__(self, params: PendulumParameters):
        self.params = params
    
    def compute_accelerations(self, theta1: float, theta2: float, omega1: float, omega2: float) -> List[float]:
        """
        Compute angular accelerations using Lagrangian equations of motion.
        
        Returns:
            [alpha1, alpha2] - angular accelerations
        """
        m1, m2, L1, L2, g = self.params.m1, self.params.m2, self.params.L1, self.params.L2, self.params.g
        
        # Angle difference
        delta = theta2 - theta1
        cos_delta = math.cos(delta)
        sin_delta = math.sin(delta)
        
        # Denominators for the equations
        den1 = (m1 + m2) * L1 - m2 * L1 * cos_delta * cos_delta
        den2 = (L2 / L1) * den1
        
        # Numerators
        num1 = (-m2 * L1 * omega1 * omega1 * sin_delta * cos_delta +
                m2 * g * math.sin(theta2) * cos_delta +
                m2 * L2 * omega2 * omega2 * sin_delta -
                (m1 + m2) * g * math.sin(theta1))
        
        num2 = (-m2 * L2 * omega2 * omega2 * sin_delta * cos_delta +
                (m1 + m2) * g * math.sin(theta1) * cos_delta +
                (m1 + m2) * L1 * omega1 * omega1 * sin_delta -
                (m1 + m2) * g * math.sin(theta2))
        
        # Angular accelerations
        alpha1 = num1 / den1
        alpha2 = num2 / den2
        
        return [alpha1, alpha2]


class SymplecticIntegrator:
    """Symplectic integrator using Velocity Verlet algorithm for energy conservation."""
    
    def __init__(self, solver: LagrangianSolver):
        self.solver = solver
    
    def step(self, state: SimulationState, dt: float) -> SimulationState:
        """
        Advance the system state by one time step using Velocity Verlet.
        
        Args:
            state: Current simulation state
            dt: Time step
            
        Returns:
            New simulation state
        """
        # Current accelerations
        alpha = self.solver.compute_accelerations(state.theta1, state.theta2, state.omega1, state.omega2)
        
        # Update positions (angles)
        new_theta1 = state.theta1 + state.omega1 * dt + 0.5 * alpha[0] * dt * dt
        new_theta2 = state.theta2 + state.omega2 * dt + 0.5 * alpha[1] * dt * dt
        
        # Compute new accelerations at new positions
        new_alpha = self.solver.compute_accelerations(new_theta1, new_theta2, state.omega1, state.omega2)
        
        # Update velocities using average of old and new accelerations
        new_omega1 = state.omega1 + 0.5 * (alpha[0] + new_alpha[0]) * dt
        new_omega2 = state.omega2 + 0.5 * (alpha[1] + new_alpha[1]) * dt
        
        return SimulationState(
            theta1=new_theta1,
            theta2=new_theta2,
            omega1=new_omega1,
            omega2=new_omega2,
            time=state.time + dt
        )


class EnergyCalculator:
    """Calculates and monitors energy conservation for the double pendulum."""
    
    def __init__(self, params: PendulumParameters):
        self.params = params
        self.initial_energy = None
    
    def calculate_kinetic_energy(self, state: SimulationState) -> float:
        """Calculate kinetic energy of the system."""
        m1, m2, L1, L2 = self.params.m1, self.params.m2, self.params.L1, self.params.L2
        
        # Kinetic energy formula for double pendulum
        T1 = 0.5 * (m1 + m2) * L1 * L1 * state.omega1 * state.omega1
        T2 = 0.5 * m2 * L2 * L2 * state.omega2 * state.omega2
        T12 = m2 * L1 * L2 * state.omega1 * state.omega2 * math.cos(state.theta1 - state.theta2)
        
        return T1 + T2 + T12
    
    def calculate_potential_energy(self, state: SimulationState) -> float:
        """Calculate potential energy of the system."""
        m1, m2, L1, L2, g = self.params.m1, self.params.m2, self.params.L1, self.params.L2, self.params.g
        
        # Potential energy (taking pivot as reference level)
        V1 = -(m1 + m2) * g * L1 * math.cos(state.theta1)
        V2 = -m2 * g * L2 * math.cos(state.theta2)
        
        return V1 + V2
    
    def calculate_total_energy(self, state: SimulationState) -> EnergyData:
        """Calculate all energy components and conservation error."""
        kinetic = self.calculate_kinetic_energy(state)
        potential = self.calculate_potential_energy(state)
        total = kinetic + potential
        
        # Set initial energy on first calculation
        if self.initial_energy is None:
            self.initial_energy = total
            conservation_error = 0.0
        else:
            conservation_error = abs(total - self.initial_energy) / abs(self.initial_energy)
        
        return EnergyData(
            kinetic=kinetic,
            potential=potential,
            total=total,
            conservation_error=conservation_error,
            timestamp=state.time
        )


class PhysicsEngine:
    """Main physics engine that coordinates all components."""
    
    def __init__(self, params: PendulumParameters):
        self.params = params
        self.solver = LagrangianSolver(params)
        self.integrator = SymplecticIntegrator(self.solver)
        self.energy_calc = EnergyCalculator(params)
    
    def get_cartesian_positions(self, state: SimulationState) -> CartesianPositions:
        """Convert angular coordinates to Cartesian positions for visualization."""
        L1, L2 = self.params.L1, self.params.L2
        
        # First pendulum position
        x1 = L1 * math.sin(state.theta1)
        y1 = -L1 * math.cos(state.theta1)
        
        # Second pendulum position (relative to first)
        x2 = x1 + L2 * math.sin(state.theta2)
        y2 = y1 - L2 * math.cos(state.theta2)
        
        return CartesianPositions(x1=x1, y1=y1, x2=x2, y2=y2)
    
    def update_state(self, state: SimulationState, dt: float) -> SimulationState:
        """Update the system state by one time step."""
        return self.integrator.step(state, dt)
    
    def get_energy_data(self, state: SimulationState) -> EnergyData:
        """Get current energy information."""
        return self.energy_calc.calculate_total_energy(state)