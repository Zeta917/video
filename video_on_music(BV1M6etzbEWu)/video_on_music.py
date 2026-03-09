from manim import *
from waves_functions import *


class VibratingString(Scene):
    def construct(self):
        t = ValueTracker(0)

        string = always_redraw(lambda:FunctionGraph(
            lambda x:mixed_swave(x,t.get_value(),8,True,3,2),
            x_range = [-64/9,64/9],
            color = BLUE,
            stroke_width = 10))
        
        self.play(Create(string))
        self.wait()
        self.play(t.animate.set_value(3),run_time = 3,rate_func = rate_functions.linear)
        self.wait()

class Waves(Scene):
    def construct(self):
        t = ValueTracker(0)

        w0 = always_redraw(lambda:FunctionGraph(
            lambda x:wave(x,t.get_value(),A = 0.5,f = 0.5)+wave(x,t.get_value(),dir = 1,A = 0.5,f = 0.5),
            x_range = [-64/9,64/9],
            color = BLUE,
            stroke_width = 10))
        """w1 = always_redraw(lambda:FunctionGraph(
            lambda x:wave(x,t.get_value(),A = 0.5,f = 0.5),
            x_range = [-64/9,64/9],
            color = RED,
            stroke_width = 10,
            stroke_opacity = 0.5))
        w2 = always_redraw(lambda:FunctionGraph(
            lambda x:wave(x,t.get_value(),dir = 1,A = 0.5,f = 0.5),
            x_range = [-64/9,64/9],
            color = GREEN,
            stroke_width = 10,
            stroke_opacity = 0.5))"""

        self.play(Create(VGroup(w0)))
        self.wait()
        self.play(t.animate.set_value(18),run_time = 18,rate_func = rate_functions.linear)
        self.wait()

class WavePacketReflect(Scene):
    def construct(self):
        t = ValueTracker(0)

        w = always_redraw(lambda:FunctionGraph(
            lambda x:wave_packet(x,t.get_value(),A = 1,f = 0.5,u = 3)+wave_packet(x,t.get_value()-128/27,dir = 1,A = 1,f = 0.5,u = 3,phi = PI),
            x_range = [-64/9,64/9],
            color = BLUE,
            stroke_width = 10))

        self.play(Create(w))
        self.wait()
        self.play(t.animate.set_value(12),run_time = 12,rate_func = rate_functions.linear)

class EXPFunction(Scene):
    def construct(self):
        a = Axes(x_range = [0,3],y_range = [0,3],x_length= 3,y_length = 3).scale(2)
        f = a.plot(lambda x:np.exp(x-1.5),x_range = [0,3],color = PINK)
        lines = a.get_vertical_lines_to_graph(f,x_range = [0.5,2.5],num_lines = 25)

        lg1 = MathTex(r"\propto \lg_{}{f} ").shift(RIGHT*1.5)
        lg2 = MathTex(r"\propto \lg_{}{\frac{f_1}{f_2} } ").shift(RIGHT*1.5)

        self.play(Write(lg1))
        self.wait()
        self.play(ReplacementTransform(lg1,lg2))
        self.wait()
        self.play(Unwrite(lg2))
        self.play(Create(a))
        self.play(Create(f))
        self.wait()
        self.play(Create(lines),run_time = 3,rate_func = rate_functions.ease_in_quart)
        self.wait()

class Vibrate(Scene):
    def construct(self):
        p = ValueTracker(300)
        w = always_redraw(lambda:wave_graph(n = p.get_value()/50,color = BLUE).shift(LEFT*4).scale(1.5))
        t = always_redraw(lambda:DecimalNumber().set_value(p.get_value()).scale(1.5).shift(RIGHT*1.3))
        hz = Text("Hz").shift(RIGHT*3.2).set_color(BLUE)
        self.play(Create(w))
        self.wait()
        self.play(Create(VGroup(t,hz)))
        self.wait()
        self.play(p.animate.set_value(600),run_time = 1.5)
        self.play(p.animate.set_value(150),run_time = 2.25)
        self.wait()
        self.play(p.animate.set_value(440))
        self.wait()

class AgreeWithEachOther(Scene):
    def construct(self):
        p1 = ValueTracker(300)
        w1 = always_redraw(lambda:wave_graph(n = p1.get_value()/50,color = BLUE).shift(LEFT*5.5+UP).scale(1.5))
        hz1 = MathTex("f_1").shift(LEFT+UP).scale(1.5).set_color(BLUE)
        f1 = VGroup(w1,hz1)

        p2 = ValueTracker(300)
        w2 = always_redraw(lambda:wave_graph(n = p2.get_value()/50,color = GREEN).shift(LEFT*5.5+DOWN).scale(1.5))
        hz2 = MathTex("f_2").shift(LEFT+DOWN).scale(1.5).set_color(GREEN)
        f2 = VGroup(w2,hz2)
        
        hz1_c = hz1.copy()
        hz2_c = hz2.copy()
        f3 = MathTex(r"\frac{\ \ \ }{} \approx ").shift(RIGHT*2.3)
        cro = Cross(VGroup(hz1_c,hz2_c,f3)).shift(RIGHT*3)

        num1 = MathTex(r"\frac{2}{3}").shift(RIGHT*3.3).scale(1.5)
        num2 = MathTex(r"\frac{3}{4}").shift(RIGHT*3.3).scale(1.5)

        
        w3 = FunctionGraph(lambda x:0.3*np.sin(PI*8*x/3)+0.3*np.sin(PI*12*x/3),x_range = [0,3],stroke_color = WHITE).scale(1.5).move_to([2.5,0,0])
        w4 = FunctionGraph(lambda x:0.3*np.sin(PI*10*x/3)+0.3*np.sin(PI*7*x/3),x_range = [0,3],stroke_color = WHITE).scale(1.5).move_to([2.5,0,0])

        self.play(Create(f1))
        self.play(Create(f2))
        self.wait()
        self.add(hz1_c,hz2_c)
        self.play(hz1_c.animate.move_to([2,0.5,0]),hz2_c.animate.move_to([2,-0.5,0]),Write(f3))
        self.play(p1.animate.set_value(400),p2.animate.set_value(600))
        self.wait()
        self.play(p1.animate.set_value(500),p2.animate.set_value(350),Create(cro))
        self.wait()
        self.play(FadeOut(cro))
        self.wait()
        self.play(Create(num1))
        self.play(ReplacementTransform(num1,num2))
        self.wait()
        self.play(FadeOut(VGroup(num2,hz1_c,hz2_c,f3)))
        self.wait()
        self.play(p1.animate.set_value(400),p2.animate.set_value(600))
        self.wait()

        w1_c = w1.copy()
        w2_c = w2.copy()

        self.add(w1_c,w2_c)
        self.play(w1_c.animate.move_to([2.5,0,0]),w2_c.animate.move_to([2.5,0,0]))
        self.play(FadeOut(VGroup(w1_c,w2_c)),FadeIn(w3))
        self.wait()
        self.play(p1.animate.set_value(500),p2.animate.set_value(350),FadeOut(w3))
        self.wait()

        w1_c = w1.copy()
        w2_c = w2.copy()

        self.add(w1_c,w2_c)
        self.play(w1_c.animate.move_to([2.5,0,0]),w2_c.animate.move_to([2.5,0,0]))
        self.play(FadeOut(VGroup(w1_c,w2_c)),FadeIn(w4))
        self.wait()

class Musical8th(Scene):
    def construct(self):
        p1 = ValueTracker(500)
        w1_o = wave_graph(n = p1.get_value()/50,color = BLUE).shift(LEFT*5.5+UP).scale(1.5)
        w1 = always_redraw(lambda:wave_graph(n = p1.get_value()/50,color = BLUE).scale(1.5).move_to([-3,0,0]))

        p2 = ValueTracker(350)
        w2_o = wave_graph(n = p2.get_value()/50,color = GREEN).shift(LEFT*5.5+DOWN).scale(1.5)
        w2 = always_redraw(lambda:wave_graph(n = p2.get_value()/50,color = GREEN).scale(1.5).move_to([3,0,0]))
        t = MathTex(r"1 \ \ \ \ \ \ \ \ \ \ : \ \ \ \ \ \ \ \ \ \ 2 ").scale(1.5).shift(UP*2)
        c4 = Text("C4").move_to([-3,-2,0])
        c5 = Text("C5").move_to([3,-2,0])
        g4 = Text("G4").move_to([-3,-2,0])
        g5 = Text("G5").move_to([3,-2,0])
        d5 = Text("D5").move_to([-3,-2,0])
        d6 = Text("D6").move_to([3,-2,0])

        self.add(w1_o,w2_o)
        self.wait()
        self.play(ReplacementTransform(w1_o,w1),ReplacementTransform(w2_o,w2))
        self.play(p1.animate.set_value(200),p2.animate.set_value(400))
        self.wait()
        self.play(Write(t))
        self.wait()
        self.play(Write(VGroup(c4,c5)))
        self.wait()
        self.play(ReplacementTransform(c4,g4),
                  ReplacementTransform(c5,g5),
                  p1.animate.set_value(300),
                  p2.animate.set_value(600))
        self.wait()
        self.play(ReplacementTransform(g4,d5),
                  ReplacementTransform(g5,d6),
                  p1.animate.set_value(450),
                  p2.animate.set_value(900))
        self.wait()

class TwelveToneEqual(Scene):
    def construct(self):
        power1 = VGroup()
        power1 += MathTex("(\\sqrt[12]{2} )^{1} \\approx 1.059463 \\approx \\frac{16}{15} ")
        power1 += MathTex("(\\sqrt[12]{2} )^{2} \\approx 1.122462 \\approx \\frac{9}{8} ")
        power1 += MathTex("(\\sqrt[12]{2} )^{3} \\approx 1.189207 \\approx \\frac{6}{5} ")
        power1 += MathTex("(\\sqrt[12]{2} )^{4} \\approx 1.259921 \\approx \\frac{5}{4} ")
        power1 += MathTex("(\\sqrt[12]{2} )^{5} \\approx 1.334840 \\approx \\frac{4}{3} ")
        power1 += MathTex("(\\sqrt[12]{2} )^{6} \\approx 1.414214").set_color(GRAY)
        power1.arrange(DOWN,aligned_edge = LEFT).to_edge(LEFT,buff = 1.5)
        
        power2 = VGroup()
        power2 += MathTex("(\\sqrt[12]{2} )^{7 \ } \\approx 1.498307 \\approx \\frac{3}{2} ")
        power2 += MathTex("(\\sqrt[12]{2} )^{8 \ } \\approx 1.587401 \\approx \\frac{8}{5} ")
        power2 += MathTex("(\\sqrt[12]{2} )^{9 \ } \\approx 1.681793 \\approx \\frac{5}{3} ")
        power2 += MathTex("(\\sqrt[12]{2} )^{10} \\approx 1.781797 \\approx \\frac{16}{9} ")
        power2 += MathTex("(\\sqrt[12]{2} )^{11} \\approx 1.887749").set_color(GRAY)
        power2.arrange(DOWN,aligned_edge = LEFT).to_edge(RIGHT,buff = 1.5)

        self.play(Write(power1))
        self.play(Write(power2))
        self.wait()
        self.play(Unwrite(VGroup(power1,power2)))

class Piano(Scene):
    def construct(self):
        num = 18
        white_key_width = (128/9-0.02*(num - 1))/num
        black_key_width = 5*white_key_width/8
        black_keys_buff = white_key_width - (black_key_width - 0.02)
        black_keys_buff_to_edge = white_key_width - (black_key_width - 0.02)/2

        white_keys = VGroup()
        for i in range(0,num):
            white_keys += Rectangle(color = WHITE,height = 4,width = white_key_width,fill_opacity = 1,stroke_width = 0)
        white_keys.arrange(RIGHT,buff = 0.02).to_edge(LEFT,buff  = 0)

        black_keys = VGroup()
        for i in range(0,num):
            black_keys += Rectangle(color = GRAY_D,height = 2.5,width = black_key_width,fill_opacity = 1,stroke_width = 0)
        black_keys.arrange(RIGHT,buff = black_keys_buff).to_edge(LEFT,buff = black_keys_buff_to_edge).align_to(white_keys,UP)

        no_keys = VGroup()
        k = 2
        while k < len(black_keys):
            no_keys += black_keys[k]
            k += 4
            if k >= len(black_keys):
                break
            no_keys += black_keys[k]
            k += 3
        no_keys.set_opacity(0)

        Clabels = VGroup()
        Clabels += Text("C3").move_to(white_keys[0].get_bottom(),aligned_edge = DOWN).scale(0.6).set_color(BLACK)
        Clabels += Text("C4").move_to(white_keys[7].get_bottom(),aligned_edge = DOWN).scale(0.6).set_color(BLACK)
        Clabels += Text("C5").move_to(white_keys[14].get_bottom(),aligned_edge = DOWN).scale(0.6).set_color(BLACK)

        group1 = VGroup()
        for i in range(1,7):
            group1 += white_keys[i]
        for i in range(0,6):
            group1 += black_keys[i]

        group2 = VGroup()
        for i in range(8,14):
            group2 += white_keys[i]
        for i in range(7,13):
            group2 += black_keys[i]

        group3 = VGroup()
        for i in range(15,18):
            group3 += white_keys[i]
        for i in range(14,18):
            group3 += black_keys[i]

        a = Arc(radius = 0.2,arc_center = black_keys[7].get_corner(UL),start_angle = 0,angle = PI)
        at = MathTex(r"\sqrt[12]{2}").move_to(a.get_top(),aligned_edge = DOWN).scale(0.6)
        
        white_keys[0].set_color(BLUE_A)
        white_keys[7].set_color(BLUE_A)
        white_keys[14].set_color(BLUE_A)
        self.play(Create(white_keys[0]),Create(white_keys[7]),Create(white_keys[14]),
                  Write(Clabels[0]),Write(Clabels[1]),Write(Clabels[2]))
        self.wait()
        self.play(Create(group1),Create(group2),Create(group3),run_time = 2)
        self.wait()
        self.play(Create(VGroup(a,at)))
        self.wait()
        white_keys[9].set_color(RED_B)
        black_keys[11].set_color(RED_B)
        self.wait(0.2)
        white_keys[9].set_color(WHITE)
        black_keys[11].set_color(GRAY_D)
        white_keys[10].set_color(RED_B)
        white_keys[12].set_color(RED_B)
        self.wait(0.2)
        white_keys[10].set_color(WHITE)
        white_keys[12].set_color(WHITE)
        white_keys[8].set_color(RED_B)
        white_keys[13].set_color(RED_B)
        self.wait(0.2)
        white_keys[8].set_color(WHITE)
        white_keys[13].set_color(WHITE)
        white_keys[11].set_color(RED_B)
        white_keys[14].set_color(RED_B)
        self.wait(0.5)
        white_keys[11].set_color(WHITE)
        white_keys[14].set_color(BLUE_A)
        self.wait()

class MovingSineWave(Scene):
    def construct(self):
        w = FunctionGraph(lambda x:np.sin(5*x),x_range = [-64/9,20],color = BLUE,stroke_width = 10)

        self.add(w)
        self.play(w.animate.shift(LEFT*12),run_time = 6,rate_func = rate_functions.linear)

class SeriesOfSineWaves(Scene):
    def construct(self):
        w = VGroup()
        c1 = [BLUE,TEAL,GREEN,PURPLE]
        c2 = [BLUE_A,TEAL_A,GREEN_A,PURPLE_A]
        for i in range(0,4):
            g = VGroup()
            g += wave_graph(i+1,color = c1[i]).scale(1.5)
            g += wave_graph(i+1,color = c2[i]).rotate(PI,RIGHT).scale(1.5)
            w += g
        w.arrange(DOWN,buff = 0.7).to_edge(UP,buff = 1.2)

        t = VGroup()
        for i in range(0,4):
            t += MathTex(f"{i+1} \\times f").scale(1.5).move_to(w[i].get_edge_center(RIGHT)).set_color(c1[i])
        
        w[0][0].shift(UP*0.48)

        self.play(Create(w),run_time = 2)
        self.wait()
        self.play(w.animate.shift(LEFT*1.5),Write(t),lag_ratio = 0.1)
        self.wait()

class fGraph(Scene):
    def construct(self):
        a = Axes(x_range = [-10,0],y_range = [0,10],x_length = 10,y_length = 6,tips = False)

        self.play(Create(a),run_time = 2)
        self.wait()