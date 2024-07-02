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

        self.next_section("Transition_to_graph")

        screen = FullScreenRectangle()

        self.grid = NumberPlane(
            x_range=(-5, 5, 1),
            y_range=(-3, 3, 1),
            x_length=screen.width,
            y_length=screen.height,
            tips=True,
            background_line_style={
                "stroke_color": RED,
                "stroke_opacity": 0.6,
            },
            axis_config={
                "include_numbers": True,
                "tip_shape": StealthTip,
            },
        )

        x_label = self.grid.get_x_axis_label("x")
        y_label = self.grid.get_y_axis_label("y")

        graph_screen = VGroup(self.grid, x_label, y_label)

        # Remember position before moving away
        graph_screen.generate_target()

        graph_screen.next_to(screen, DOWN)

        self.add(graph_screen)

        title.generate_target()
        title.target.shift(UP * 6)

        self.play(
            MoveToTarget(graph_screen),
            MoveToTarget(title),
            run_time=2,
        )
        self.wait()
