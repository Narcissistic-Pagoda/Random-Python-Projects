from manim import *
import numpy as np

class FluidFlow(Scene):
    def construct(self):
        # Parameters for the simulation
        n_steps = 200 # Number of steps
        x = np.linspace(-5, 5, n_steps)
        y = np.linspace(-5, 5, n_steps)
        X, Y = np.meshgrid(x, y)

        # Define the differential equation for fluid flow
        def fluid_flow(x, y):
            u = np.sin(x)*np.cos(y)
            v = np.cos(x)*np.sin(y)
            return u, v

        # Compute the flow field using the differential equation
        U, V = fluid_flow(X, Y)

        # Create the streamplot
        streamplot = StreamLines(
            lambda x, y: np.array(fluid_flow(x, y)).T,
            color=BLUE,
            max_stroke_width=1, # width of each streamline
        ).fade(0.5) # fade out the oldest streamlines

        # Add the streamplot to the scene
        self.add(streamplot)

if __name__ == "__main__":
    # Create the animation using the FluidFlow class
    animation = FluidFlow()

    # Render the animation
    renderer = renderer = Renderer(
        file_writer_config=ffmpeg_writer_config,
        scene=animation
    )
    renderer.render()
