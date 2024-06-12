#!/usr/bin/env python

from manim import *

class Intro(Scene):
    def construct(self):
        self.title()
        self.intro()

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
        self.wait()
    
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
            Tex("- Funktionsschar"),
            Tex("- Funktionenschar"),
            Tex("- Kurvenschar"),
            Tex("- Parameterfunktion"),
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
            MoveToTarget(function),
            LaggedStart(
                *names_animations,
                lag_ratio=0.25,
                run_time=2,
            )
        )
        self.wait()
