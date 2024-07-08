#!/usr/bin/env python

from manim import *

class Outro(Scene):
    def construct(self):
        heading = Tex("GFS Funktionenscharen", color=PINK)
        heading.scale(0.8)
        heading.move_to(LEFT * 4 + UP * 3.5)

        subheading = Tex("Vielen Dank für Aufmerksamkeit", color=PINK)
        subheading.scale(0.6)
        subheading.move_to(RIGHT * 4 + DOWN * 3)

        external_sources = self.construct_external_sources()
        animation_sources = self.construct_animation_sources()

        external_sources.align_on_border(RIGHT)
        external_sources.shift(UP * 1.5)

        animation_sources.align_on_border(LEFT)
        animation_sources.shift(DOWN * 1)

        self.play(
            LaggedStart(
                Write(heading),
                LaggedStart(
                    [FadeIn(s, shift=DOWN) for s in external_sources],
                    lag_ratio=0.1,
                    run_time=3
                ),
                LaggedStart(
                    [FadeIn(s, shift=DOWN) for s in animation_sources],
                    lag_ratio=0.1,
                    run_time=3
                ),
                Write(subheading),
                lag_ratio=0.5,
                run_time=3,
            )
        )

        self.wait()

    def construct_external_sources(self):
        heading = Tex("Externe Quellen", color=BLUE)
        heading.scale(0.6)

        block = VGroup(heading)

        sources = [
            f'<span fgcolor="{PURPLE}">Definition Funktionenschar</span>\nhttps://de.wikipedia.org/wiki/Kurvenschar',
            f'<span fgcolor="{PURPLE}">Wurfparabeln</span>\nhttps://de.wikipedia.org/wiki/Wurfparabel',
            f'<span fgcolor="{PURPLE}">Hüllkurven</span>\nhttps://de.wikipedia.org/wiki/Einh%C3%BCllende',
            f'<span fgcolor="{PURPLE}">Vereinfachung cos^2(tan^-1(x))</span>\nhttps://socratic.org/questions/how-do-you-simplify-cos-2-tan-1-x',
            f'<span fgcolor="{PURPLE}">Allgemein</span>\nLambacher Schweizer Mathematik Kursstufe Leistungsfach',
        ]

        for s in sources:
            source_text = MarkupText(s)
            source_text.scale(0.35)
            block.add(source_text)
        
        block.arrange(DOWN, aligned_edge=RIGHT)
        return block
    
    def construct_animation_sources(self):
        block = VGroup()

        sources = [
            f'<span fgcolor="{BLUE}">Animation mit Manim Community</span>',
            f'https://www.manim.community/',
            f'<span fgcolor="{BLUE}">Presenter</span>',
            f'https://github.com/CinTheDev/mp4-presenter',
            f'<span fgcolor="{BLUE}">GFS Projektdateien</span>',
            f'https://github.com/CinTheDev/GFS-Funktionsscharen',
        ]

        for s in sources:
            source_text = MarkupText(s)
            source_text.scale(0.35)
            block.add(source_text)

        block.arrange(DOWN, aligned_edge=LEFT)        
        return block
