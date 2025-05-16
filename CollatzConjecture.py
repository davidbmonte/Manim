from manim import *

class CollatzPlot(Scene):
    def construct(self):
        start_number = 7  # You can change this
        sequence = [start_number]

        # Generate Collatz sequence
        n = start_number
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            sequence.append(n)

        # Set up the axes
        axes = Axes(
            x_range=[0, len(sequence), 1],
            y_range=[0, max(sequence) + 10, 10],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=False,
        )

        labels = axes.get_axis_labels(x_label="Step", y_label="Value")
        self.play(Create(axes), Write(labels), run_time=3)

        # Plot points
        points = [
            axes.coords_to_point(x, y)
            for x, y in enumerate(sequence)
        ]
        dots = [Dot(p, radius=0.05, color=BLUE) for p in points]
        lines = [
            Line(points[i], points[i+1], color=YELLOW)
            for i in range(len(points) - 1)
        ]

        # Animate the plot
        for i in range(len(dots)):
            self.play(FadeIn(dots[i]), run_time=0.1)
            if i > 0:
                self.play(Create(lines[i - 1]), run_time=0.1)

        self.wait(2)

class CollatzMultiplePlots(Scene):
    def construct(self):
        max_start = 10
        all_sequences = []

        max_length = 0
        max_value = 0

        # Generate all sequences from 1 to 10
        for start in range(1, max_start + 1):
            n = start
            seq = [n]
            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = 3 * n + 1
                seq.append(n)
            all_sequences.append(seq)
            max_length = max(max_length, len(seq))
            max_value = max(max_value, max(seq))

        # Set up axes
        axes = Axes(
            x_range=[0, max_length, 1],
            y_range=[0, max_value + 10, 10],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": False},
            tips=False,
        )
        labels = axes.get_axis_labels(x_label="Step", y_label="Value")
        self.play(Create(axes), Write(labels), run_time=3)

        # Colors for each sequence
        colors = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE, TEAL, MAROON, PINK, GOLD]

        # Plot each sequence
        for i, sequence in enumerate(all_sequences):
            points = [axes.coords_to_point(x, y) for x, y in enumerate(sequence)]
            graph = VMobject(color=colors[i % len(colors)])
            graph.set_points_as_corners(points)
            label = Text(str(i + 1), font_size=18, color=colors[i % len(colors)]).move_to(points[0] + LEFT * 0.3 + UP * 0.2)
            self.play(Create(graph), FadeIn(label), run_time=0.5)

        self.wait(3)


