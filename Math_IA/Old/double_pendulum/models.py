"""
Core data models for the double pendulum simulation.
"""
from dataclasses import dataclass
from typing import Tuple
import math


@dataclass
class SimulationState:
    """Represents the current state of the double pendulum system."""
    theta1: float      # Angle of first pendulum (radians)
    theta2: float      # Angle of second pendulum (radians)
    omega1: float      # Angular velocity of first pendulum (rad/s)
    omega2: float      # Angular velocity of second pendulum (rad/s)
    time: float        # Current simulation time (s)
    
    def __post_init__(self):
        """Normalize angles to [-π, π] range."""
        self.theta1 = self._normalize_angle(self.theta1)
        self.theta2 = self._normalize_angle(self.theta2)
    
    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Normalize angle to [-π, π] range."""
        # Use atan2 for robust normalization
        return math.atan2(math.sin(angle), math.cos(angle))
    
    def to_array(self) -> list:
        """Convert state to array format [θ1, θ2, ω1, ω2]."""
        return [self.theta1, self.theta2, self.omega1, self.omega2]
    
    @classmethod
    def from_array(cls, state_array: list, time: float = 0.0):
        """Create SimulationState from array format."""
        return cls(
            theta1=state_array[0],
            theta2=state_array[1], 
            omega1=state_array[2],
            omega2=state_array[3],
            time=time
        )


@dataclass
class PendulumParameters:
    """Physical parameters for the double pendulum system."""
    m1: float = 1.0    # Mass of first pendulum (kg)
    m2: float = 1.0    # Mass of second pendulum (kg)
    L1: float = 1.0    # Length of first rod (m)
    L2: float = 1.0    # Length of second rod (m)
    g: float = 9.81    # Gravitational acceleration (m/s²)
    
    def validate(self) -> Tuple[bool, str]:
        """
        Validate that all parameters are physically reasonable.
        
        Returns:
            Tuple of (is_valid, error_message)
        """
        if self.m1 <= 0:
            return False, "Mass m1 must be positive"
        if self.m2 <= 0:
            return False, "Mass m2 must be positive"
        if self.L1 <= 0:
            return False, "Length L1 must be positive"
        if self.L2 <= 0:
            return False, "Length L2 must be positive"
        if self.g <= 0:
            return False, "Gravitational acceleration g must be positive"
        
        # Check for reasonable bounds to prevent numerical issues
        if self.m1 > 1000 or self.m2 > 1000:
            return False, "Masses should be reasonable (< 1000 kg)"
        if self.L1 > 100 or self.L2 > 100:
            return False, "Lengths should be reasonable (< 100 m)"
            
        return True, ""
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        is_valid, error_msg = self.validate()
        if not is_valid:
            raise ValueError(f"Invalid parameters: {error_msg}")


@dataclass
class EnergyData:
    """Energy information for the double pendulum system."""
    kinetic: float
    potential: float
    total: float
    conservation_error: float
    timestamp: float
    
    @property
    def conservation_percentage(self) -> float:
        """Return energy conservation error as percentage."""
        return abs(self.conservation_error) * 100
    
    def is_conserved(self, threshold: float = 0.1) -> bool:
        """Check if energy is conserved within threshold percentage."""
        return self.conservation_percentage < threshold


@dataclass
class CartesianPositions:
    """Cartesian coordinates for visualization."""
    x1: float  # X position of first pendulum bob
    y1: float  # Y position of first pendulum bob  
    x2: float  # X position of second pendulum bob
    y2: float  # Y position of second pendulum bob
    
    def get_positions(self) -> Tuple[Tuple[float, float], Tuple[float, float]]:
        """Return positions as tuples: ((x1, y1), (x2, y2))."""
        return ((self.x1, self.y1), (self.x2, self.y2))