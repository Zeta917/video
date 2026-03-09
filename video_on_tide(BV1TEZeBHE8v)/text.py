from manim import *

class EarthRotateAngularSpeed(Scene):
    def construct(self):
        t1 = MathTex(r"J = I\omega \approx 5.86 \times 10^{33}\ \mathrm{kg \cdot m^2/s} ")
        t2 = MathTex(r"\frac{\mathrm{d} T}{\mathrm{d} t} \approx 1.8\ \mathrm{ms/century}")
        VGroup(t1,t2).arrange(DOWN,aligned_edge=LEFT).to_edge(UL)
        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
