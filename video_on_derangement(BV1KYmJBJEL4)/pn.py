from manim import *

class Pn(Scene):
    def construct(self):
        t1 = MathTex(r"a_n = n!\sum_{i=0}^n \frac{(-1)^i}{i!}")
        t2 = MathTex(r"p_n = \sum_{i=0}^n \frac{(-1)^i}{i!}")
        t3 = MathTex(r"\frac{1}{e} = \sum_{i=0}^{\infty} \frac{(-1)^i}{i!}")

        VGroup(t1,t3).arrange(DOWN)
        t2.move_to(t1)

        self.add(t1,t3)
        self.wait()
        self.play(ReplacementTransform(t1,t2))
        self.wait()
