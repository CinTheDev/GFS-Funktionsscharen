#!/usr/bin/env python

from manim import *

class Placeholder(Scene):
    def construct(self):
        self.next_section("Placeholder")

        text = Tex(r"This is some placeholder text")

        self.play(
            Write(text)
        )
        self.wait()
