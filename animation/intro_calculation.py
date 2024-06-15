#!/usr/bin/env python

from manim import *

class IntroCalculation(Scene):
    def construct(self):
        self.transition()
    
    def transition(self):
        self.next_section("Transition_Title")
        self.clear()

        title = Tex("Aber wie rechnet man mit sowas?")

        self.add(title)
        self.wait()
