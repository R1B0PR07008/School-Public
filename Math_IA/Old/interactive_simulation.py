"""
Interactive double pendulum simulation with user controls.
"""
import math
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from double_pendulum import (
    SimulationState, 
    PendulumParameters, 
    DoublePendulumSimulation
)


class InteractiveDoublePendulum:
    """Interactive double pendulum with GUI controls."""
    
    def __init__(self):
        # Default parameters
        self.params = PendulumParameters(m1=1.0, m2=1.0, L1=1.0, L2=1.0, g=9.81)
        self.initial_state = SimulationState(
            theta1=math.pi/2, theta2=math.pi/2, 
            omega1=0.0, omega2=0.0, time=0.0
        )
        
        # Create simulation
        self.simulation = DoublePendulumSimulation(self.params, self.initial_state)
        
        # Add control widgets
        self.setup_controls()
        
        # Start animation
        self.animation = self.simulation.start_animation(interval=20)
    
    def setup_controls(self):
        """Set up interactive control widgets."""
        fig = self.simulation.renderer.fig
        
        # Adjust figure to make room for controls
        fig.subplots_adjust(bottom=0.25)
        
        # Control panel area
        control_height = 0.04
        control_spacing = 0.05
        
        # Pause/Resume button
        ax_pause = plt.axes([0.1, 0.02, 0.1, control_height])
        self.btn_pause = widgets.Button(ax_pause, 'Pause')
        self.btn_pause.on_clicked(self.toggle_pause)
        
        # Reset button
        ax_reset = plt.axes([0.25, 0.02, 0.1, control_height])
        self.btn_reset = widgets.Button(ax_reset, 'Reset')
        self.btn_reset.on_clicked(self.reset_simulation)
        
        # Speed slider
        ax_speed = plt.axes([0.4, 0.02, 0.2, control_height])
        self.slider_speed = widgets.Slider(ax_speed, 'Speed', 0.1, 3.0, valinit=1.0)
        self.slider_speed.on_changed(self.update_speed)
        
        # Initial angle sliders
        ax_theta1 = plt.axes([0.1, 0.08, 0.2, control_height])
        self.slider_theta1 = widgets.Slider(ax_theta1, 'θ₁ (°)', -180, 180, 
                                          valinit=math.degrees(self.initial_state.theta1))
        self.slider_theta1.on_changed(self.update_initial_conditions)
        
        ax_theta2 = plt.axes([0.4, 0.08, 0.2, control_height])
        self.slider_theta2 = widgets.Slider(ax_theta2, 'θ₂ (°)', -180, 180,
                                          valinit=math.degrees(self.initial_state.theta2))
        self.slider_theta2.on_changed(self.update_initial_conditions)
        
        # Mass sliders
        ax_m1 = plt.axes([0.1, 0.14, 0.2, control_height])
        self.slider_m1 = widgets.Slider(ax_m1, 'm₁ (kg)', 0.1, 5.0, valinit=self.params.m1)
        self.slider_m1.on_changed(self.update_parameters)
        
        ax_m2 = plt.axes([0.4, 0.14, 0.2, control_height])
        self.slider_m2 = widgets.Slider(ax_m2, 'm₂ (kg)', 0.1, 5.0, valinit=self.params.m2)
        self.slider_m2.on_changed(self.update_parameters)
        
        # Length sliders
        ax_L1 = plt.axes([0.1, 0.20, 0.2, control_height])
        self.slider_L1 = widgets.Slider(ax_L1, 'L₁ (m)', 0.1, 3.0, valinit=self.params.L1)
        self.slider_L1.on_changed(self.update_parameters)
        
        ax_L2 = plt.axes([0.4, 0.20, 0.2, control_height])
        self.slider_L2 = widgets.Slider(ax_L2, 'L₂ (m)', 0.1, 3.0, valinit=self.params.L2)
        self.slider_L2.on_changed(self.update_parameters)
        
        self.paused = False
    
    def toggle_pause(self, event):
        """Toggle pause/resume."""
        if self.paused:
            self.simulation.resume()
            self.btn_pause.label.set_text('Pause')
            self.paused = False
        else:
            self.simulation.pause()
            self.btn_pause.label.set_text('Resume')
            self.paused = True
    
    def reset_simulation(self, event):
        """Reset simulation to initial conditions."""
        self.simulation.reset()
        if self.paused:
            self.toggle_pause(event)  # Resume if paused
    
    def update_speed(self, val):
        """Update simulation speed."""
        self.simulation.set_speed(val)
    
    def update_initial_conditions(self, val):
        """Update initial conditions from sliders."""
        self.initial_state = SimulationState(
            theta1=math.radians(self.slider_theta1.val),
            theta2=math.radians(self.slider_theta2.val),
            omega1=0.0,
            omega2=0.0,
            time=0.0
        )
        # Update simulation's initial state
        self.simulation.initial_state = self.initial_state
    
    def update_parameters(self, val):
        """Update physical parameters from sliders."""
        try:
            new_params = PendulumParameters(
                m1=self.slider_m1.val,
                m2=self.slider_m2.val,
                L1=self.slider_L1.val,
                L2=self.slider_L2.val,
                g=9.81
            )
            
            # Update simulation parameters
            self.params = new_params
            self.simulation.params = new_params
            self.simulation.physics.params = new_params
            self.simulation.physics.solver.params = new_params
            self.simulation.physics.energy_calc.params = new_params
            
            # Update visualization limits
            total_length = new_params.L1 + new_params.L2
            margin = 0.2
            ax = self.simulation.renderer.ax_pendulum
            ax.set_xlim(-total_length - margin, total_length + margin)
            ax.set_ylim(-total_length - margin, margin)
            
        except ValueError as e:
            print(f"Invalid parameters: {e}")
    
    def show(self):
        """Display the interactive simulation."""
        plt.show()


def main():
    """Run the interactive double pendulum simulation."""
    print("Interactive Double Pendulum Simulation")
    print("=" * 40)
    print("Controls:")
    print("  - Use sliders to adjust parameters and initial conditions")
    print("  - Pause/Resume button to control animation")
    print("  - Reset button to restart with current settings")
    print("  - Speed slider to adjust simulation speed")
    print("  - Close window to exit")
    print("\nStarting interactive simulation...")
    
    # Create and show interactive simulation
    interactive_sim = InteractiveDoublePendulum()
    interactive_sim.show()


if __name__ == "__main__":
    main()