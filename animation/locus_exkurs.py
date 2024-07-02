#!/usr/bin/env python

from manim import *

class ExkursParametricFunction(Scene):
    def construct(self):
        self.transition()
    
    def transition(self):
        self.next_section("Transition")

        title_intro = Tex("Kurzer Exkurs:", color=RED)
        title_text = Tex("Parameterisierte Funktionen", color=RED)
        title = VGroup(title_intro, title_text)
        title.arrange(DOWN)

        self.add(title)
        self.wait()
