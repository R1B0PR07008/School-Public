"""
Visualization components for the double pendulum simulation.
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from collections import deque
from typing import List, Optional
from .models import SimulationState, PendulumParameters, EnergyData, CartesianPositions
from .physics import PhysicsEngine


class AnimationRenderer:
    """Real-time visualization of pendulum motion using matplotlib."""
    
    def __init__(self, params: PendulumParameters, trail_length: int = 100):
        self.params = params
        self.trail_length = trail_length
        
        # Set up the figure and axis
        self.fig, (self.ax_pendulum, self.ax_energy) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Configure pendulum plot
        total_length = params.L1 + params.L2
        margin = 0.2
        self.ax_pendulum.set_xlim(-total_length - margin, total_length + margin)
        self.ax_pendulum.set_ylim(-total_length - margin, margin)
        self.ax_pendulum.set_aspect('equal')
        self.ax_pendulum.grid(True, alpha=0.3)
        self.ax_pendulum.set_title('Double Pendulum Simulation')
        self.ax_pendulum.set_xlabel('X Position (m)')
        self.ax_pendulum.set_ylabel('Y Position (m)')
        
        # Initialize pendulum elements
        self.rod1_line, = self.ax_pendulum.plot([], [], 'b-', linewidth=3, label='Rod 1')
        self.rod2_line, = self.ax_pendulum.plot([], [], 'r-', linewidth=3, label='Rod 2')
        self.bob1_circle, = self.ax_pendulum.plot([], [], 'bo', markersize=10, label='Mass 1')
        self.bob2_circle, = self.ax_pendulum.plot([], [], 'ro', markersize=10, label='Mass 2')
        self.pivot_point, = self.ax_pendulum.plot([0], [0], 'ko', markersize=8, label='Pivot')
        
        # Trail for second pendulum
        self.trail_x = deque(maxlen=trail_length)
        self.trail_y = deque(maxlen=trail_length)
        self.trail_line, = self.ax_pendulum.plot([], [], 'r-', alpha=0.3, linewidth=1, label='Trail')
        
        self.ax_pendulum.legend(loc='upper right')
        
        # Configure energy plot
        self.ax_energy.set_title('Energy Conservation')
        self.ax_energy.set_xlabel('Time (s)')
        self.ax_energy.set_ylabel('Energy (J)')
        self.ax_energy.grid(True, alpha=0.3)
        
        # Energy data storage
        self.time_data = []
        self.kinetic_data = []
        self.potential_data = []
        self.total_data = []
        
        # Energy plot lines
        self.kinetic_line, = self.ax_energy.plot([], [], 'g-', label='Kinetic')
        self.potential_line, = self.ax_energy.plot([], [], 'b-', label='Potential')
        self.total_line, = self.ax_energy.plot([], [], 'k-', label='Total')
        self.ax_energy.legend()
        
        # Energy text display
        self.energy_text = self.ax_energy.text(0.02, 0.98, '', transform=self.ax_energy.transAxes,
                                             verticalalignment='top', fontfamily='monospace')
    
    def update_frame(self, positions: CartesianPositions, energy: EnergyData):
        """Update the animation frame with new positions and energy data."""
        # Update pendulum visualization
        self.rod1_line.set_data([0, positions.x1], [0, positions.y1])
        self.rod2_line.set_data([positions.x1, positions.x2], [positions.y1, positions.y2])
        self.bob1_circle.set_data([positions.x1], [positions.y1])
        self.bob2_circle.set_data([positions.x2], [positions.y2])
        
        # Update trail
        self.trail_x.append(positions.x2)
        self.trail_y.append(positions.y2)
        self.trail_line.set_data(list(self.trail_x), list(self.trail_y))
        
        # Update energy data
        self.time_data.append(energy.timestamp)
        self.kinetic_data.append(energy.kinetic)
        self.potential_data.append(energy.potential)
        self.total_data.append(energy.total)
        
        # Keep only recent data for performance
        max_points = 1000
        if len(self.time_data) > max_points:
            self.time_data = self.time_data[-max_points:]
            self.kinetic_data = self.kinetic_data[-max_points:]
            self.potential_data = self.potential_data[-max_points:]
            self.total_data = self.total_data[-max_points:]
        
        # Update energy plots
        self.kinetic_line.set_data(self.time_data, self.kinetic_data)
        self.potential_line.set_data(self.time_data, self.potential_data)
        self.total_line.set_data(self.time_data, self.total_data)
        
        # Auto-scale energy plot
        if self.time_data:
            self.ax_energy.set_xlim(min(self.time_data), max(self.time_data))
            all_energies = self.kinetic_data + self.potential_data + self.total_data
            if all_energies:
                energy_min, energy_max = min(all_energies), max(all_energies)
                energy_range = energy_max - energy_min
                margin = 0.1 * energy_range if energy_range > 0 else 1.0
                self.ax_energy.set_ylim(energy_min - margin, energy_max + margin)
        
        # Update energy text
        energy_text = f"""Energy Status:
Kinetic:  {energy.kinetic:.3f} J
Potential: {energy.potential:.3f} J
Total:    {energy.total:.3f} J
Error:    {energy.conservation_percentage:.4f}%
Time:     {energy.timestamp:.2f} s"""
        self.energy_text.set_text(energy_text)
        
        return [self.rod1_line, self.rod2_line, self.bob1_circle, self.bob2_circle, 
                self.trail_line, self.kinetic_line, self.potential_line, self.total_line]
    
    def clear_trail(self):
        """Clear the pendulum trail."""
        self.trail_x.clear()
        self.trail_y.clear()
    
    def reset_energy_plots(self):
        """Reset energy plot data."""
        self.time_data.clear()
        self.kinetic_data.clear()
        self.potential_data.clear()
        self.total_data.clear()


class DoublePendulumSimulation:
    """Complete double pendulum simulation with real-time visualization."""
    
    def __init__(self, params: PendulumParameters, initial_state: SimulationState, dt: float = 0.01):
        self.params = params
        self.initial_state = initial_state
        self.current_state = initial_state
        self.dt = dt
        
        # Initialize physics and visualization
        self.physics = PhysicsEngine(params)
        self.renderer = AnimationRenderer(params)
        
        # Animation control
        self.animation = None
        self.running = False
        
    def animate_step(self, frame):
        """Single animation step."""
        if self.running:
            # Update physics
            self.current_state = self.physics.update_state(self.current_state, self.dt)
            
        # Get current positions and energy
        positions = self.physics.get_cartesian_positions(self.current_state)
        energy = self.physics.get_energy_data(self.current_state)
        
        # Update visualization
        return self.renderer.update_frame(positions, energy)
    
    def start_animation(self, interval: int = 20):
        """Start the real-time animation."""
        self.running = True
        self.animation = animation.FuncAnimation(
            self.renderer.fig, self.animate_step, interval=interval, blit=True, cache_frame_data=False
        )
        return self.animation
    
    def pause(self):
        """Pause the simulation."""
        self.running = False
    
    def resume(self):
        """Resume the simulation."""
        self.running = True
    
    def reset(self):
        """Reset to initial conditions."""
        self.current_state = self.initial_state
        self.physics.energy_calc.initial_energy = None  # Reset energy reference
        self.renderer.clear_trail()
        self.renderer.reset_energy_plots()
    
    def show(self):
        """Display the simulation window."""
        plt.tight_layout()
        plt.show()
    
    def set_speed(self, speed_factor: float):
        """Adjust simulation speed by changing time step."""
        self.dt = 0.01 * speed_factor