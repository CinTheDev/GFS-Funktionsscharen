#!/usr/bin/env python

from generic_solve_blocks import *

class LocusContinuation(GenericSolveBlocks):
    def construct(self):
        self.default_color = RED

        self.prepare()
        self.solve_x()
        self.insert()

    def prepare(self):
        self.next_section("Transition")
        transition_title = Tex("Zurück zu Ortskurven", color=RED)

        self.add(transition_title)
        self.wait()

        self.next_section("Write_old_solution")

        title = Tex("Umwandlung der parameterisierten Funktion", color=RED)
        title.scale(0.6)
        title.move_to(UP * 3.5)

        self.play(
            Transform(transition_title, title),
            run_time=1
        )

        part_solution = [
            r"x(a) = ln(\frac{a}{2})",
            r"y(a) = -\frac{a^2}{4}",
        ]

        block = self.block('Alte "Lösung"', UP * 2, part_solution)

        self.next_section("Move_block_aside")

        block.generate_target()
        block.target.shift(LEFT * 4)

        self.play(
            MoveToTarget(block),
            run_time=1,
        )
    
    def solve_x(self):
        steps = [
            r"x = ln(\frac{a}{2})",
            r"e^x = \frac{a}{2}",
            r"2e^x = a",
        ]

        self.block("x-Teil nach a auflösen", UP * 2, steps)
    
    def insert(self):
        steps = [
            r"y = -\frac{a^2}{4}",
            r"y = -\frac{(2e^x)^2}{4}",
            r"y = -\frac{4 e^{2x}}{4}",
            r"y = -e^{2x}",
        ]

        self.block("a in y-Teil einsetzen", UP * 2 + RIGHT * 4, steps)
