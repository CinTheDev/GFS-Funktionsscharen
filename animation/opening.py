#!/usr/bin/env python

from manim import *

class Intro(Scene):
    def construct(self):
        self.title()
        self.intro()
        self.play_graph()

    def title(self):
        self.next_section("Title")
        title = Tex(r"GFS Funktionsscharen")
        formula = Tex(r"Mit \LaTeX \:yeah whats going on")

        VGroup(title, formula).arrange(DOWN)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("Example")

        self.play(
            Write(formula)
        )
        self.wait()

        self.next_section("Transition")

        self.play(
            FadeOut(title),
            FadeOut(formula),
        )
    
    def intro(self):
        base_function = MathTex(r"f_a(x)")
        function_linear1 = MathTex(r"f_a(x) = ax")
        function_linear2 = MathTex(r"f_a(x) = x + a")

        function = base_function.copy()

        # Linear function examples

        self.play(
            Write(function)
        )
        self.wait()
        self.next_section("Linear1")

        self.play(
            Transform(function, function_linear1)
        )
        self.wait()
        self.next_section("Linear2")

        self.play(
            Transform(function, function_linear2)
        )
        self.wait()
        self.next_section("Names")

        # Different names for "Funktionsscharen"

        names = [
            Tex("- Funktionsschar", color=YELLOW),
            Tex("- Funktionenschar", color=YELLOW),
            Tex("- Kurvenschar", color=YELLOW),
            Tex("- Parameterfunktion", color=YELLOW),
        ]

        names_list = VGroup()
        names_animations = []

        function.generate_target()
        names_list.add(function.target)

        for name in names:
            names_list.add(name)
            names_animations.append(Write(name))

        names_list.arrange(DOWN, aligned_edge=LEFT)
        function.target.set_x(0) # Align function in center

        self.play(
            MoveToTarget(function)
        )
        self.play(
            LaggedStart(
                *names_animations,
                lag_ratio=0.25,
                run_time=2,
            )
        )
        self.wait()

        self.next_section("Transition")

        self.play(
            FadeOut(function),
            FadeOut(names_list),
        )
    
    def play_graph(self):
        screen = FullScreenRectangle()

        # Draw coordinate system
        grid = NumberPlane(
            x_range=(-5.1, 5.1, 1),
            y_range=(-1.1, 5.1, 1),
            x_length=screen.width,
            y_length=screen.height,
        )

        self.play(
            Create(grid, run_time=3, lag_ratio=0.1),
        )

        parabola = grid.plot(
            lambda x: x*x,
            color=YELLOW
        )

        self.play(
            Create(parabola)
        )
        self.wait()
