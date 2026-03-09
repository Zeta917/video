from manim import *

class Recursion(Scene):
    def construct(self):
        eq1 = MathTex(r"a_n = (n-1)(a_{n-1} + a_{n-2})",
                     r"a_n -n a_{n-1}= -[a_{n-1} - (n-1)a_{n-2}]",
                     r"a_n -n a_{n-1}=(-1)^n\ \ \ (n \geq 2)",
                     r"\frac{a_n}{n!} -\frac{a_{n-1}}{(n-1)!}=\frac{(-1)^n}{n!}\ \ \ (n \geq 2)",
                     r"\sum_{i = 2}^n{(\frac{a_i}{i!} -\frac{a_{i-1}}{(i-1)!})}=\sum_{i = 2}^n\frac{(-1)^i}{i!}",
                     r"\frac{a_n}{n!} = \sum_{i = 2}^n\frac{(-1)^i}{i!} \ \ \ (n \geq 2)",
                     r"a_n = n!\sum_{i = 0}^n\frac{(-1)^i}{i!} \ \ \ (n \geq 1)").arrange(DOWN,aligned_edge = LEFT).scale(0.8).to_edge(LEFT)
        self.play(Write(eq1))
        self.wait()

        eq2 = Text("Attention is all you need!").to_edge(RIGHT)
        self.play(Write(eq2))
        self.wait()