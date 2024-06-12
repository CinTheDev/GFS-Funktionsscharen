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

        self.play(
            Transform(function, base_function)
        )
        self.wait()
        # TODO: Write titles
