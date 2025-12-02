"""
Unit tests for double pendulum data models.
"""
import unittest
import math
from double_pendulum.models import SimulationState, PendulumParameters, EnergyData, CartesianPositions


class TestSimulationState(unittest.TestCase):
    """Test cases for SimulationState class."""
    
    def test_initialization(self):
        """Test basic initialization of SimulationState."""
        state = SimulationState(
            theta1=math.pi/4,
            theta2=math.pi/6,
            omega1=0.5,
            omega2=-0.3,
            time=1.0
        )
        
        self.assertAlmostEqual(state.theta1, math.pi/4)
        self.assertAlmostEqual(state.theta2, math.pi/6)
        self.assertAlmostEqual(state.omega1, 0.5)
        self.assertAlmostEqual(state.omega2, -0.3)
        self.assertAlmostEqual(state.time, 1.0)
    
    def test_angle_normalization(self):
        """Test that angles are normalized to [-π, π] range."""
        # Test angle > π
        state = SimulationState(
            theta1=3*math.pi,
            theta2=5*math.pi/2,
            omega1=0,
            omega2=0,
            time=0
        )
        
        # 3π should normalize to π (or -π, both are equivalent)
        self.assertAlmostEqual(abs(state.theta1), math.pi, places=10)
        self.assertAlmostEqual(state.theta2, math.pi/2, places=10)
        
        # Test angle < -π
        state = SimulationState(
            theta1=-3*math.pi,
            theta2=-5*math.pi/2,
            omega1=0,
            omega2=0,
            time=0
        )
        
        # -3π should normalize to -π (or π, both are equivalent)
        self.assertAlmostEqual(abs(state.theta1), math.pi, places=10)
        self.assertAlmostEqual(state.theta2, -math.pi/2, places=10)
        
        # Test that normalized angles are in range [-π, π]
        test_angles = [0, math.pi/4, math.pi/2, math.pi, -math.pi/4, -math.pi/2, -math.pi,
                      2*math.pi, -2*math.pi, 7*math.pi/4, -7*math.pi/4]
        
        for angle in test_angles:
            state = SimulationState(theta1=angle, theta2=0, omega1=0, omega2=0, time=0)
            self.assertGreaterEqual(state.theta1, -math.pi)
            self.assertLessEqual(state.theta1, math.pi)
    
    def test_array_conversion(self):
        """Test conversion to and from array format."""
        original_state = SimulationState(
            theta1=math.pi/3,
            theta2=-math.pi/4,
            omega1=1.5,
            omega2=-2.0,
            time=2.5
        )
        
        # Test to_array
        array = original_state.to_array()
        expected = [math.pi/3, -math.pi/4, 1.5, -2.0]
        
        for i in range(4):
            self.assertAlmostEqual(array[i], expected[i])
        
        # Test from_array
        reconstructed_state = SimulationState.from_array(array, 2.5)
        
        self.assertAlmostEqual(reconstructed_state.theta1, original_state.theta1)
        self.assertAlmostEqual(reconstructed_state.theta2, original_state.theta2)
        self.assertAlmostEqual(reconstructed_state.omega1, original_state.omega1)
        self.assertAlmostEqual(reconstructed_state.omega2, original_state.omega2)
        self.assertAlmostEqual(reconstructed_state.time, original_state.time)


class TestPendulumParameters(unittest.TestCase):
    """Test cases for PendulumParameters class."""
    
    def test_valid_parameters(self):
        """Test initialization with valid parameters."""
        params = PendulumParameters(m1=2.0, m2=1.5, L1=1.2, L2=0.8, g=9.81)
        
        self.assertEqual(params.m1, 2.0)
        self.assertEqual(params.m2, 1.5)
        self.assertEqual(params.L1, 1.2)
        self.assertEqual(params.L2, 0.8)
        self.assertEqual(params.g, 9.81)
    
    def test_default_parameters(self):
        """Test default parameter values."""
        params = PendulumParameters()
        
        self.assertEqual(params.m1, 1.0)
        self.assertEqual(params.m2, 1.0)
        self.assertEqual(params.L1, 1.0)
        self.assertEqual(params.L2, 1.0)
        self.assertEqual(params.g, 9.81)
    
    def test_invalid_parameters(self):
        """Test that invalid parameters raise ValueError."""
        # Test negative mass
        with self.assertRaises(ValueError):
            PendulumParameters(m1=-1.0)
        
        # Test zero mass
        with self.assertRaises(ValueError):
            PendulumParameters(m2=0.0)
        
        # Test negative length
        with self.assertRaises(ValueError):
            PendulumParameters(L1=-0.5)
        
        # Test zero gravity
        with self.assertRaises(ValueError):
            PendulumParameters(g=0.0)
        
        # Test unreasonably large values
        with self.assertRaises(ValueError):
            PendulumParameters(m1=2000.0)  # Too large mass
        
        with self.assertRaises(ValueError):
            PendulumParameters(L1=200.0)   # Too large length
    
    def test_validation_method(self):
        """Test the validate method directly."""
        params = PendulumParameters()
        is_valid, error_msg = params.validate()
        
        self.assertTrue(is_valid)
        self.assertEqual(error_msg, "")


class TestEnergyData(unittest.TestCase):
    """Test cases for EnergyData class."""
    
    def test_initialization(self):
        """Test basic initialization of EnergyData."""
        energy = EnergyData(
            kinetic=5.0,
            potential=3.0,
            total=8.0,
            conservation_error=0.001,
            timestamp=1.5
        )
        
        self.assertEqual(energy.kinetic, 5.0)
        self.assertEqual(energy.potential, 3.0)
        self.assertEqual(energy.total, 8.0)
        self.assertEqual(energy.conservation_error, 0.001)
        self.assertEqual(energy.timestamp, 1.5)
    
    def test_conservation_percentage(self):
        """Test conservation error percentage calculation."""
        energy = EnergyData(
            kinetic=5.0,
            potential=3.0,
            total=8.0,
            conservation_error=0.001,
            timestamp=1.0
        )
        
        self.assertAlmostEqual(energy.conservation_percentage, 0.1)
        
        # Test negative error
        energy.conservation_error = -0.002
        self.assertAlmostEqual(energy.conservation_percentage, 0.2)
    
    def test_is_conserved(self):
        """Test energy conservation checking."""
        # Well conserved energy
        energy = EnergyData(
            kinetic=5.0,
            potential=3.0,
            total=8.0,
            conservation_error=0.0005,  # 0.05%
            timestamp=1.0
        )
        
        self.assertTrue(energy.is_conserved())
        self.assertTrue(energy.is_conserved(threshold=0.1))
        
        # Poorly conserved energy
        energy.conservation_error = 0.002  # 0.2%
        
        self.assertFalse(energy.is_conserved())
        self.assertFalse(energy.is_conserved(threshold=0.1))
        self.assertTrue(energy.is_conserved(threshold=0.5))


class TestCartesianPositions(unittest.TestCase):
    """Test cases for CartesianPositions class."""
    
    def test_initialization(self):
        """Test basic initialization of CartesianPositions."""
        pos = CartesianPositions(x1=1.0, y1=-0.5, x2=0.8, y2=-1.2)
        
        self.assertEqual(pos.x1, 1.0)
        self.assertEqual(pos.y1, -0.5)
        self.assertEqual(pos.x2, 0.8)
        self.assertEqual(pos.y2, -1.2)
    
    def test_get_positions(self):
        """Test position tuple extraction."""
        pos = CartesianPositions(x1=1.0, y1=-0.5, x2=0.8, y2=-1.2)
        positions = pos.get_positions()
        
        self.assertEqual(positions, ((1.0, -0.5), (0.8, -1.2)))


if __name__ == '__main__':
    unittest.main()