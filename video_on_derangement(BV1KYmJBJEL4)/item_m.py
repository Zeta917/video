from manim import *

class ItemM(Scene):
    def construct(self):
        eq = VGroup()
        eq += MathTex(r"C_m^1 - C_m^2 + C_m^3 - \cdots + (-1)^m C_m^{m-1}")
        eq += MathTex(r"1 - C_m^1 + C_m^2 - C_m^3 + \cdots + (-1)^{m-1} C_m^{m-1}")
        eq += MathTex(r"C_m^0 - C_m^1 + C_m^2 - C_m^3 + \cdots + (-1)^{m-1} C_m^{m-1}")
        eq += MathTex(r"C_m^0 - C_m^1 + C_m^2 - C_m^3 + \cdots + (-1)^{m-1} C_m^{m-1}",r"+ (-1)^{m} C_m^{m} + (-1)^{m+1} C_m^{m}").arrange(DOWN).shift(DOWN*0.5)
        eq += MathTex(r"(1-1)^m + (-1)^{m+1} C_m^{m}")
        eq += MathTex(r"(-1)^{m+1}")

        self.play(Write(eq[0]))
        for i in range(1,6):
            self.wait()
            self.play(Transform(eq[0],eq[i]))
        self.wait()