from manim import *
import math

class Limit0(MovingCameraScene):
    def construct(self):
        def p(n):
            return sum([(-1)**k/math.factorial(k) for k in range(0,n + 1)])
        
        x_r = 20
        a = Axes(x_range = [0,x_r,2],y_range = [0.3,0.6,0.1],x_length = 12,y_length = 6).to_edge(LEFT,buff = 1.5)
        a.add_coordinates()
        al = a.get_axis_labels(MathTex("n"),MathTex("p_n"))
        
        limit = VGroup()
        limit += Dot(a.c2p(0,math.exp(-1)))
        limit += Line(start = a.c2p(0,math.exp(-1)),end = a.c2p(x_r,math.exp(-1)),stroke_width = 1)
        limit += MathTex(r"\frac{1}{e}").move_to(a.c2p(0,math.exp(-1)),aligned_edge = UR).shift(LEFT*0.4)

        d = VGroup()
        for x in range(2,x_r,1):
            d += Dot(a.c2p(x,p(x)),color = YELLOW)

        self.play(Write(a),Write(al))
        self.wait()
        self.play(Write(d))
        self.play(Write(limit))
        self.wait()

class Limit1(Scene):
    def construct(self):
        def p(n,m):
            return sum([((-1)**k * math.comb(n,k))/(math.factorial(k) * math.comb(n+m,k)) for k in range(0,n + 1)])
        
        x_r = 400
        a = Axes(x_range = [0,x_r,x_r/10],y_range = [0.3,0.6,0.1],x_length = 12,y_length = 6)
        a.add_coordinates()
        al = a.get_axis_labels(MathTex("n"),MathTex("p_n"))
        
        limit = VGroup()
        limit += Dot(a.c2p(0,math.exp(-1)))
        limit += Line(start = a.c2p(0,math.exp(-1)),end = a.c2p(x_r,math.exp(-1)),stroke_width = 1)
        limit += MathTex(r"\frac{1}{e}").move_to(a.c2p(0,math.exp(-1)),aligned_edge = UR).shift(LEFT*0.4)

        d = VGroup()
        c = [RED,ORANGE,YELLOW,GREEN,BLUE,PINK,PURPLE,GOLD,GRAY]

        for m in range(1,10):
            for x in range(m + 1,x_r):
                d += Dot(a.c2p(x,p(x,m)),radius = 0.02,color = c[m - 1])

        self.play(Write(a),Write(al))
        self.wait()
        self.play(Write(d))
        self.play(Write(limit))
        self.wait()

class Limit2(MovingCameraScene):
    def construct(self):
        def p(n,m):
            return sum([((-1)**k * math.comb(n,k))/(math.factorial(k) * math.comb(n+m,k)) for k in range(0,n + 1)])
        
        x_r = 2000
        a = Axes(x_range = [0,x_r,100],y_range = [0.3,0.6,0.1],x_length = x_r*12/400,y_length = 6).to_edge(LEFT,buff = 1.5)
        a.add_coordinates()
        al = a.get_axis_labels(MathTex("n"),MathTex("p_n"))
        
        limit = VGroup()
        limit += Dot(a.c2p(0,math.exp(-1)))
        limit += Line(start = a.c2p(0,math.exp(-1)),end = a.c2p(x_r,math.exp(-1)),stroke_width = 1)
        limit += MathTex(r"\frac{1}{e}").move_to(a.c2p(0,math.exp(-1)),aligned_edge = UR).shift(LEFT*0.4)

        d = VGroup()
        for x in range(3,x_r,2):
            d += Dot(a.c2p(x,p(x,2)),radius = 0.02,color = YELLOW)

        self.camera.frame.save_state()
        self.play(Write(a),Write(al))
        self.wait()
        self.play(Write(d))
        self.play(Write(limit))
        self.play(self.camera.frame.animate.shift(RIGHT*45),run_time = 2.5)
        self.wait()

class Limit3(Scene):
    def construct(self):
        t = MathTex(r"\lim_{n\to\infty}p_n = \lim_{n\to\infty}\sum_{k=0}^n \frac{(-1)^{k}C_n^k }{k!C_{n+m}^k}")
        self.play(Write(t))
        self.wait()