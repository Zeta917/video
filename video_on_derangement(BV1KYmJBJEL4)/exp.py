from manim import *

class Exp(Scene):
    def construct(self):
        t1 = MathTex(r"a_n = n!\sum_{i=0}^n \frac{(-1)^i}{i!}")
        t2 = MathTex(r"e^x = \sum_{i=0}^{\infty} \frac{x^i}{i!}").shift(DOWN)
        t3 = MathTex(r"e^{-1} = \sum_{i=0}^{\infty} \frac{(-1)^i}{i!}").shift(DOWN)
        t4 = MathTex(r"\frac{n!}{e} = n!\sum_{i=0}^{\infty} \frac{(-1)^i}{i!}").shift(DOWN)

        self.play(Write(t1))
        self.wait()
        self.play(t1.animate.shift(UP*1),Write(t2))
        self.wait()
        self.play(ReplacementTransform(t2,t3))
        self.wait()
        self.play(ReplacementTransform(t3,t4))
        self.wait()

        t1c = VGroup()
        t1c += t1.copy().scale(0.8)
        t1c += t4.copy().scale(0.8)
        t1c.arrange(RIGHT,buff = 1).to_edge(UL)

        t5 = MathTex(r"R =",r"\frac{n!}{e} - a_n = n!\sum_{i=n+1}^{\infty} \frac{(-1)^i}{i!}")
        t6 = MathTex(r"R = \frac{(-1)^{n+1}}{n+1}+\frac{(-1)^{n+2}}{(n+1)(n+2)}+\frac{(-1)^{n+3}}{(n+1)(n+2)(n+3)}+\cdots")
        t7 = MathTex(r"|R|",r" = \frac{1}{n+1}-\frac{1}{(n+1)(n+2)}+\frac{1}{(n+1)(n+2)(n+3)}-\cdots")
        t8 = MathTex(r"\ \ \ < \frac{1}{2} - \frac{1}{(n+1)(n+2)}+\frac{1}{(n+1)(n+2)(n+3)}-\cdots")
        t9 = MathTex(r"< \frac{1}{2}")
        t10 = MathTex(r"|R| < \frac{1}{2}")

        VGroup(t7,t8,t9).arrange(DOWN)
        t9.shift(LEFT*5.2)
        t2c = VGroup(t1c.copy().scale(1.25),t10).arrange(DOWN,aligned_edge = LEFT).to_edge(UL)

        self.play(ReplacementTransform(VGroup(t1,t4),t1c),Write(t5[1]))
        self.wait()
        self.play(Write(t5[0]))
        self.wait()
        self.play(ReplacementTransform(t5,t6))
        self.wait()
        self.play(ReplacementTransform(t6,t7))
        self.wait()
        self.play(Write(t8))
        self.wait()
        self.play(Write(t9))
        self.wait()
        self.play(Unwrite(VGroup(t7[1],t8)),ReplacementTransform(VGroup(t7[0],t9),t10),ReplacementTransform(t1c,t2c[0]),run_time = 1.5)
        self.wait()

        l = NumberLine(x_range = [-3.5,3.5])
        t = Triangle(color = ORANGE).scale(0.2).shift(DOWN*0.5)
        r = Rectangle(color = YELLOW,height = 0.2,width = 1,fill_opacity = 0.5,stroke_width = 0)
        t11 = MathTex("a_n",color = ORANGE).scale(0.8).next_to(t,DOWN)
        t12 = MathTex(r"\frac{n!}{e}",color = YELLOW).scale(0.8).next_to(r,UP)
        t13 = MathTex(r"\frac{n!}{e} + \frac{1}{2}",color = YELLOW).scale(0.8).move_to(t12).shift(RIGHT*0.5)

        self.play(Create(VGroup(l,t,t11)))
        self.wait()
        self.play(FadeIn(r,t12))
        self.wait()
        self.play(r.animate.shift(RIGHT*0.5),ReplacementTransform(t12,t13))
        self.wait()

        t14 = MathTex(r"a_n = [\frac{n!}{e}+\frac{1}{2}]").scale(0.8).shift(DOWN*1.5)
        
        self.play(Write(t14))
        self.play(ReplacementTransform(t14,t14.copy().move_to(ORIGIN).scale(1.5)),Unwrite(t2c),FadeOut(VGroup(l,t,r,t11,t13)),run_time = 1)
        self.wait()
        
