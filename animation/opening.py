#!/usr/bin/env python

from manim import *

class Intro(Scene):
    def construct(self):
        self.next_section("Title")
        title = Tex(r"GFS Funktionsscharen")
        formula = Tex(r"Mit \LaTeX yeah whats going on")

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
