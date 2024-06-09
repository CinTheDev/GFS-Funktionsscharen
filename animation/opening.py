#!/usr/bin/env python

from manim import *

class Intro(Scene):
    def construct(self):
        self.next_section("Title")
        title = Tex(r"GFS Funktionsscharen")

        self.play(
            Write(title)
        )

        self.wait()
        self.next_section("Example")

        formula = MathText(r"Mit \LaTeX yeah what's going on")

        self.play(
            Write(formula)
        )

        self.wait()

