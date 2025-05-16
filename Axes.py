from manim import *
import numpy as np

class Equation(Scene):
    def construct(self):
        equation = MathTex(r"E = M*C^2")
        self.play(Write(equation))
        self.wait(2)

class Axis1(Scene):
    def construct(self):
        #Building axes
        #Simple axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 9, 1],
            x_length=7,
            y_length=5,
            axis_config={
                'color': WHITE,
                'include_ticks':True,
                'include_numbers':True,
            },
            tips=False
        )

        #Labeling axes
        labels=axes.get_axis_labels(x_label='x', y_label='y')

        # Ploting a function onto the axes / the function is called lambda
        f = axes.plot(
            lambda x:x**2,
            color=BLUE,
            x_range=[-3, 3],
        )
        f_label=axes.get_graph_label(f, label='f(x)')

        self.add(axes, labels)
        self.play(Create(axes), Create(f), Write(f_label))
        self.wait(3)

class Vector(Scene):
    def construct(self):
        axes = NumberPlane()

        O = np.array([0,0,0])
        A = np.array([1,1,0])
        
        vector = Arrow(O, A, color='YELLOW')

        self.play(Create(axes))
        self.wait(2)
        self.play(Create(vector))
        self.wait(3)

class ThreeD(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
            axis_config={
                'color': WHITE,
                'include_ticks':True,
                'include_numbers':True,
            },
            tips=False
        )

        labels=axes.get_axis_labels(x_label='x', y_label='y', z_label='z')

        f = axes.plot(
            lambda x: x**2,
            color=BLUE,
            x_range=[-2,2,1]
        )

        g = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t),t]),
            t_range = [-2 * PI, 2 * PI],
            color=RED,

        )

        rects = axes.get_riemann_rectangles(
            graph = f, 
            x_range=[-2,2], 
            dx=0.1,
            color=WHITE,
        )

        self.add(axes, f)
        self.play(Create(axes), Create(f), run_time=2)
        self.wait(2)
        self.move_camera(phi=60*DEGREES)
        self.wait()
        self.move_camera(theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(
            rate = 2*PI/10, 
            about="theta" #Radians per second
        )
        self.wait()
        self.play(Create(rects), run_time=3)
        self.play(Create(g))
        self.wait(30)
        


