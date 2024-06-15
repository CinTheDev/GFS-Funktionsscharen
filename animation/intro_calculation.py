#!/usr/bin/env python

from manim import *

class IntroCalculation(Scene):
    def construct(self):
        self.transition()
        # TODO: Better function names
        self.first_option()
        self.second_option()
    
    def transition(self):
        self.next_section("Transition_Title")
        self.clear()

        title = Tex("Aber wie rechnet man mit sowas?")

        self.add(title)
        self.wait()

        self.next_section("Transition_Fadeout")

        self.play(
            FadeOut(title)
        )
    
    def first_option(self):
        title = Tex("1. Fall: Wert für a einsetzen", color=YELLOW)

        self.play(
            Write(title)
        )
        self.wait()

        self.next_section("First_Option_Example")

        # Move text to upper edge of screen
        title.generate_target()
        title.target.move_to(UP * 3)

        self.play(
            MoveToTarget(title)
        )

        # Write the equation
        equation = MathTex(
            r"f_a(x) = x^4 - 0.4ax^2",
            substrings_to_isolate="a",
        )
        equation.set_color_by_tex("a", color=PURPLE)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Parameter_Assignment")

        parameter_equation = MathTex(
            r"a = 3",
            substrings_to_isolate="a",
        )
        parameter_equation.set_color_by_tex("a", color=PURPLE)
        parameter_equation.next_to(equation, DOWN)

        parameter_equation_invisible = parameter_equation.copy()
        parameter_equation_invisible.set_opacity(0)
        parameter_equation_invisible.move_to(equation)

        self.add(parameter_equation_invisible)
        self.play(
            FadeTransform(parameter_equation_invisible, parameter_equation, replace_mobject_with_target_in_scene=True),
            run_time=0.5,
        )
        self.wait()

        self.next_section("Parameter_Evaluation")

        # TODO: Improve animation (it kinda looks confusing; it should only transform changed parts)
        # TODO: Color the "3" purple
        equation_inserted = MathTex(r"f_3(x) = x^4 - 0.4(3)x^2")

        self.play(
            Transform(equation, equation_inserted),
        )
        self.wait()

        self.next_section("Parameter_Evaluation_solve")

        # TODO: Same as above
        equation_solved = MathTex(r"f_3(x) = x^4 - 1.2x^2")

        self.play(
            Transform(equation, equation_solved),
        )
        self.wait()

        self.next_section("Fadeout")

        self.play(
            FadeOut(equation),
            FadeOut(parameter_equation),
            FadeOut(title),
        )
    
    def second_option(self):
        title = Tex("Yeah", color=YELLOW)

        self.play(
            Write(title)
        )
        self.wait()
