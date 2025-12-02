"""
Double Pendulum Simulation Package

A physics-accurate double pendulum simulation with energy conservation
using symplectic numerical integration and real-time visualization.
"""

from .models import SimulationState, PendulumParameters, EnergyData, CartesianPositions
from .physics import PhysicsEngine, LagrangianSolver, SymplecticIntegrator, EnergyCalculator
from .visualization import DoublePendulumSimulation, AnimationRenderer

__version__ = "1.0.0"
__all__ = [
    "SimulationState",
    "PendulumParameters", 
    "EnergyData",
    "CartesianPositions",
    "PhysicsEngine",
    "LagrangianSolver",
    "SymplecticIntegrator", 
    "EnergyCalculator",
    "DoublePendulumSimulation",
    "AnimationRenderer"
]