#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_2(GenericSolveBlocks):
    def construct(self):
        self.transition()

        self.introduce_problem()

        self.solve_nullstellen()
        self.clear_blocks()

        self.solve_turning_points()
        self.clear_blocks()
        
        self.solve_inflection_points()
    
    def transition(self):
        self.next_section("Transition")
        title = Tex("Ok, jetzt machen wir eine vollständige Analyse")

        self.add(title)
        self.wait()

        self.next_section("Prepare")

        self.play(
            Unwrite(title),
            run_time=0.5,
        )
    
    def introduce_problem(self):
        equation = MathTex(r"f_a(x) = x^3 - ax^2")

        comment = Tex("Vollständige Analyse der Funktion, also:", color=YELLOW)
        comment.scale(0.6)

        subcomments = [
            Tex("- Nullpunkte herausfinden", color=YELLOW).scale(0.5),
            Tex("- Extrempunkte bestimmen (auch die Art)", color=YELLOW).scale(0.5),
            Tex("- Wendepunkte bestimmen (ohne Krümmung)", color=YELLOW).scale(0.5),
        ]

        comment_group = VGroup(comment, *subcomments)
        comment_group.arrange(DOWN, aligned_edge=LEFT)
        comment_group.next_to(equation, DOWN)

        self.play(
            Write(equation),
            run_time=0.5,
        )
        self.play(
            LaggedStart(
                [Write(c) for c in comment_group],
                lag_ratio=0.5,
                run_time=5,
            )
        )
        self.wait()

        self.next_section("Make_Room")

        functions = [
            r"f_a(x) = x^3 - ax^2",
            r"f'_a(x) = 3x^2 - 2ax",
            r"f''_a(x) = 6x - 2a",
            r"f'''_a(x) = 6",
        ]

        self.play(
            Unwrite(comment_group),
            Unwrite(equation),
            run_time=0.5,
        )

        self.block(r"Funktionen \& Ableitungen", LEFT * 5 + UP * 3.25, functions, scale=0.8, invincible=True)
    
    def solve_nullstellen(self):
        self.nullstellen_solve()
    
    def nullstellen_solve(self):
        steps = [
            r"f_a(x) = 0",
            r"x^3 - ax^2 = 0",
            r"x^2(x - a) = 0",
            r"x_1 = 0; x_2 = a",
        ]

        self.block("Nullstellen", UP * 2 + RIGHT * 2, steps)
    
    def solve_turning_points(self):
        self.turning_points_solve_x()

        self.turning_points_solve_y_0()
        self.turning_points_maximum_0()
        self.turning_points_minimum_0()
        self.turning_points_saddle_0()

        self.clear_specific_blocks(2)

        self.turning_points_solve_y_1()
        self.turning_points_maximum_1()
        self.turning_points_minimum_1()
        self.turning_points_saddle_1()
    
    def turning_points_solve_x(self):
        steps = [
            r"f'_a(x) = 0",
            r"3x^2 - 2ax = 0",
            r"x(3x - 2a) = 0",
            r"x_1 = 0; x_2 = \frac{2}{3} a",
        ]

        self.block("Extremstellen", UP * 3.5, steps)
    
    def turning_points_solve_y_0(self):
        steps = [
            r"y_0 = f_a(0) = 0",
        ]

        self.block("Extrempunkte für x=0", UP * 3.5 + RIGHT * 4.5, steps)
    
    def turning_points_solve_y_1(self):
        steps = [
            r"y_{\frac{2}{3} a} = f_a(\frac{2}{3} a)",
            r"y_{\frac{2}{3} a} = (\frac{2}{3} a)^3 - a(\frac{2}{3} a)^2",
            r"y_{\frac{2}{3} a} = -\frac{4}{27} a",
        ]

        self.block("Extrempunkte für x=(2/3)a", UP * 3.5 + RIGHT * 4.5, steps)
    
    def turning_points_maximum_0(self):
        steps = [
            r"f''_a(0) < 0",
            r"-2a < 0",
            r"a > 0",
        ]

        self.block("Hochpunkt für x=0", DOWN * 1 + LEFT * 4, steps)
    
    def turning_points_maximum_1(self):
        steps = [
            r"f''_a(\frac{2}{3} a) < 0",
            r"6(\frac{2}{3} a) - 2a < 0",
            r"4a - 2a < 0",
            r"2a < 0",
            r"a < 0",
        ]

        self.block("Hochpunkt für x=(2/3)a", DOWN * 0.25 + LEFT * 4.5, steps, scale=0.6)
    
    def turning_points_minimum_0(self):
        steps = [
            r"f''_a(0) > 0",
            r"-2a > 0",
            r"a < 0",
        ]

        self.block("Tiefpunkt für x=0", DOWN * 1, steps)
    
    def turning_points_minimum_1(self):
        steps = [
            r"f''_a(\frac{2}{3} a) > 0",
            #r"6(\frac{2}{3} a) - 2a > 0",
            #r"4a - 2a > 0",
            #r"2a > 0",
            r"a > 0",
        ]

        self.block("Tiefpunkt für x=(2/3)a", DOWN * 1, steps)
    
    def turning_points_saddle_0(self):
        steps = [
            r"f''_a(0) = 0",
            r"-2a = 0",
            r"a = 0",
        ]

        self.block("Sattelpunkt für x=0", DOWN * 1 + RIGHT * 4, steps)
    
    def turning_points_saddle_1(self):
        steps = [
            r"f''_a(\frac{2}{3} a) = 0",
            #r"6(\frac{2}{3} a) - 2a = 0",
            #r"4a - 2a = 0",
            #r"2a = 0",
            r"a = 0",
        ]

        self.block("Sattelpunkt für x(2/3)", DOWN * 1 + RIGHT * 4, steps)
    
    def solve_inflection_points(self):
        self.inflection_points_solve_x()
        self.inflection_points_check()
        self.inflection_points_solve_y()
    
    def inflection_points_solve_x(self):
        steps = [
            r"f''_a(x) = 0",
            r"6x - 2a = 0",
            r"6x = 2a",
            r"x = \frac{1}{3} a",
        ]

        self.block("Wendestellen", UP * 3.5, steps)

    def inflection_points_check(self):
        steps = [
            r"f'''_a(x) \neq 0",
            r"6 \neq 0",
        ]

        self.block("Wendestelle prüfen", DOWN * 1, steps)
    
    def inflection_points_solve_y(self):
        steps = [
            r"y_{\frac{1}{3} a} = f_a(\frac{1}{3} a)",
            r"y_{\frac{1}{3} a} = (\frac{1}{3} a)^3 - a(\frac{1}{3} a)^2",
            r"y_{\frac{1}{3} a} = \frac{1}{27} a^3 - \frac{1}{9} a^3",
            r"y_{\frac{1}{3} a} = -\frac{2}{27} a^3",
        ]

        self.block("Wendepunkte", UP * 3.5 + RIGHT * 4.5, steps)
