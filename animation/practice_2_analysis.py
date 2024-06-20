#!/usr/bin/env python

from generic_solve_blocks import *

class Practice_2(GenericSolveBlocks):
    def construct(self):
        self.transition()
    
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
        self.wait()
