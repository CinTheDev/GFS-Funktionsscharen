#!/usr/bin/env python

# Ortskurven

from manim import *

class Locus(Scene):
    def construct(self):
        self.transition()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Ortskurven", color=RED)

        self.play(
            SpinInFromNothing(title)
        )
        self.wait()
