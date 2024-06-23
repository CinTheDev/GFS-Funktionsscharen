#!/usr/bin/env python

from manim import *

class Bundles(Scene):
    def construct(self):
        self.transition()
    
    def transition(self):
        self.next_section("Transition")

        title = Tex("Spezielle Eigenschaften von Funktionenscharen", color=BLUE)

        subtitle = Tex("1: Bestimmen von Funktionsbündeln", color=BLUE)
        subtitle.scale(0.6)
        subtitle.next_to(title, DOWN)

        self.play(
            Write(title),
        )
        self.play(
            FadeIn(subtitle, shift=UP),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Make_Room")

        subtitle.generate_target()
        subtitle.target.move_to(UP * 3.5)

        self.play(
            Unwrite(title),
            run_time=0.5,
        )
        self.play(
            MoveToTarget(subtitle),
            run_time=0.7
        )
        self.wait()
