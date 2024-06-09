#!/usr/bin/env python

from manim import *

class Placeholder(Scene):
    def construct(self):
        self.next_section("Placeholder")

        text = Tex(r"TODO")

        self.play(
            Write(text)
        )
        self.wait()
