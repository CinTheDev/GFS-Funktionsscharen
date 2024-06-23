#!/usr/bin/env python

from manim import *

class Bundles(Scene):
    def construct(self):
        self.transition()
        self.first_example()
    
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
    
    def first_example(self):
        self.next_section("First_Example")

        equation = MathTex(r"f_a(x) = ax^2 - 4a")

        self.play(
            Write(equation),
            run_time=0.7,
        )
        self.wait()

        self.next_section("Move_Equation")

        equation.generate_target()
        equation.target.move_to(UP * 2)

        self.play(
            MoveToTarget(equation),
            run_time=0.7,
        )
        steps = [
            MathTex(r"f_a(x) = f_b(x); {{ a \neq b }}"),
            MathTex(r"f_1(x) = f_2(x)"),
            MathTex(r"1 \cdot x^2 - 4 \cdot 1 = 2 \cdot x^2 - 4 \cdot 2"),
            MathTex(r"x^2 - 4 = 2x^2 - 8"),
            MathTex(r"4 = x^2"),
            MathTex(r"\pm 2 = x"),
            MathTex(r"f_a(-2) = 0 = f_a(2)"),
        ]

        last_pos = equation
        all_equations = VGroup(equation)

        steps[0].submobjects[1].set_color(ORANGE)

        for step in steps:
            tex = step
            tex.next_to(last_pos, DOWN)

            self.play(
                FadeIn(tex, shift=UP),
                run_time=0.5
            )
            self.wait()
            self.next_section("Solve_Step")

            last_pos = tex
            all_equations.add(tex)
