#!/usr/bin/env python

from manim import *

class AnalysisExponentialAdvanced(Scene):
    def construct(self):
        self.transition()

    def transition(self):
        self.next_section("Transition")
        title = Tex("Noch ein Beispiel")
        title.move_to(UP * 3)

        self.play(
            Write(title),
            run_time=1
        )
        self.wait()
