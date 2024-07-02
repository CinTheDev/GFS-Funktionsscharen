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

        self.play(
            SpinInFromNothing(title_intro),
            run_time=1,
        )
        self.play(
            FadeIn(title_text, shift=UP),
            run_time=1,
        )
        self.wait()
