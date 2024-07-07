#!/usr/bin/env python

# Hüllkurven

from manim import *

class Envelope(Scene):
    def construct(self):
        self.transition()
        self.graph()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("4: Hüllkurven", color=PINK)

        self.add(title)
        self.wait()

        self.next_section("Graph")

        self.play(
            FadeOut(title)
        )
    
    def graph(self):
        pass
