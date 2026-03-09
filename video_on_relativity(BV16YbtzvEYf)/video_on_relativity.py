from manim import *
from transformation import *

class LorentzTransformation(GalileoAndLorentzTransformationScene):
    def construct(self):
        wl1 = self.plane.plot_parametric_curve(
            lambda t: np.array([0, t, 0]),
            t_range=[-8,8],
            color=RED,
            stroke_width = 10
        )
        wl2 = self.plane.plot(
            lambda x:2*x,
            color = PINK,
            stroke_width = 10
        )
        
        self.transformable_items += [wl1,wl2]

        self.add_labels()
        self.add_light()
        self.play(Create(VGroup(wl1,wl2)))
        self.wait()
        self.lorentz_transformation(0.5)
        self.wait()
        
class VisualiseTransformation(Scene):
    def construct(self):
        plane = NumberPlane()
        back_ground_plane = NumberPlane(**{
            "color": GREY,
            "axis_config": {
                "color": GREY,
            },
            "background_line_style": {
                "stroke_color": GREY,
                "stroke_width": 1,
            }})
        lb = plane.get_axis_labels('x','t')
        
        m = np.array([[2,-1,0],[1,1,0],[0,0,1]])
        def transformation(point):
            return m @ point
        
        p1 = Dot([2,1,0],color = RED,radius = 0.1)
        p2 = p1.copy().move_to(m @ p1.get_center())
        
        arrow = Arrow(p1.get_center(),p2.get_center(),color = WHITE,buff = 0.2)
        
        self.add(back_ground_plane,plane,lb)
        self.play(Create(p1))
        self.play(ApplyPointwiseFunction(transformation,plane),
                  TransformFromCopy(p1,p2),
                  GrowArrow(arrow),
                  run_time = 3)
        self.wait()

class ElectromagneticWave(ThreeDScene):
    def construct(self):
        a = ThreeDAxes(x_range = [-2,10],y_range = [-2,2],z_range = [-2,2],
                       x_length = 12,y_length = 4,z_length = 4)
        
        k = ValueTracker(0)
        bwave = always_redraw(lambda:a.plot_parametric_curve(lambda t:[t,np.sin(t-k.get_value()),0],t_range = [0,10],color = BLUE))
        ewave = always_redraw(lambda:a.plot_parametric_curve(lambda t:[t,0,np.sin(t-k.get_value())],t_range = [0,10],color = YELLOW))
        wave = VGroup(ewave,bwave)

        evecs = always_redraw(lambda:a.get_vertical_lines_to_graph(
            ewave,x_range = [0,10],
            num_lines = 50,
            line_func = Arrow,
            color = YELLOW,
            line_config = {"buff":0,
                           "max_tip_length_to_length_ratio":0.15,
                           "max_stroke_width_to_length_ratio":10}))
        
        bvecs = always_redraw(lambda:a.get_vertical_lines_to_graph(
                    bwave,x_range = [0,10],
                    num_lines = 50,
                    line_func = Arrow,
                    color = BLUE,
                    line_config = {"buff":0,
                                   "max_tip_length_to_length_ratio":0.15,
                                   "max_stroke_width_to_length_ratio":10}))

        self.play(DrawBorderThenFill(a),Create(wave),Create(evecs),Create(bvecs),run_time = 0.5)
        self.move_camera(phi = PI/3,theta = PI/3)
        self.play(k.animate.set_value(4*PI),run_time = 6,rate_func = rate_functions.linear)
        self.wait()

class AxesMoving(Scene):
    def construct(self):
        a1 = Axes(x_range = [0,1],y_range = [0,1],x_length = 4,y_length = 4).shift(LEFT*4)
        a1l = a1.get_axis_labels("x","t")
        o1 = Text("O").move_to(a1.get_origin(),aligned_edge = UR).scale(0.7)
        s1 = VGroup(a1,a1l,o1)
        
        a2 = Axes(x_range = [0,1],y_range = [0,1],x_length = 4,y_length = 4,axis_config = {"color":BLUE}).shift(LEFT*4)
        a2l = a2.get_axis_labels("x'","t'").set_color(BLUE)
        o2 = always_redraw(lambda :Text("O'",color = BLUE).move_to(a2.get_origin(),aligned_edge = UR).scale(0.7))
        s2 = VGroup(a2,a2l,o2)

        self.play(Create(s1),Create(s2))
        self.wait()
        self.play(s2.animate.shift(RIGHT*8),rate_func = rate_functions.linear,run_time = 6)

class MaxwelsEquations(Scene):
    def construct(self):

        f1 = MathTex(r"""\begin{aligned}
                        &\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0} \\
                        &\nabla \cdot \mathbf{B} = 0 \\
                        &\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \\
                        &\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
                        \end{aligned}""").shift(LEFT*2.5)
        f2 = MathTex(r"""\begin{aligned}
                        \Rightarrow c &= \frac{1}{\sqrt{\mu_0 \epsilon_0} } \\
                        &=299792458m/s
                        \end{aligned}""").shift(RIGHT*2.5)

        self.play(Write(f1))
        self.wait()
        self.play(Write(f2))

class mmexperiment(Scene):
    def construct(self):
        a = VGroup()
        for i in np.arange(-3.5,4,1):
            a += Arrow(start = [-7,i,0],end = [7,i,0],color = GRAY,buff = 0.25)
        
        o = Dot(radius = 0.1,color = YELLOW)
        
        lv = []
        for k in np.arange(0,2,1/6):
            lv.append(np.array([2*np.cos(k*PI)+1,2*np.sin(k*PI),0]))

        l = VGroup()
        for i in range(12):
            l += Line(start = [0,0,0],end = [0,0,0],color = YELLOW_B)

        def update_l(l,dt):
            for i in range(12):
                l[i].put_start_and_end_on([0,0,0],l[i].get_end()+lv[i]*dt)
            
        self.play(*[GrowArrow(a[x]) for x in range(8)])
        self.add(l)
        self.play(Create(o))
        self.wait()
        l.add_updater(update_l)
        self.wait(8)

class DerivationOfLorentzTransformation(Scene):
    def construct(self):
        f1 = MathTex(r"\left\{\begin{matrix}   x' = ax + bt \\    t' = px + qt\end{matrix}\right.")
        f2 = MathTex(r"\left\{\begin{matrix}   x = \frac{q}{aq-bp} x' + \frac{-b}{aq-bp} t'\\    t = \frac{-p}{aq-bp} x' + \frac{a}{aq-bp} t'\end{matrix}\right.")
        
        f3_1 = MathTex(r"x = ut \to x' = 0")
        f3_2 = MathTex(r"\begin{matrix}x' = aut + bt\\\ t' = put + qt\end{matrix}")
        f3_3 = MathTex(r"x' = \frac{au+b}{pu+q} t'")
        f3_4 = MathTex(r"au+b = 0")
        
        f4_1 = MathTex(r"x = 0 \to x' = -ut'")
        f4_2 = MathTex(r"ax + bt = -upx - uqt")
        f4_3 = MathTex(r"(a+up)x = -(b+uq)t")
        f4_4 = MathTex(r"b + uq = 0")
        
        f5_1 = MathTex(r"x = ct \to x' = ct'")
        f5_2 = MathTex(r"ax + bt = cpx + cqt")
        f5_3 = MathTex(r"(a - cp)x = (cq - b)t")
        f5_4= MathTex(r"cq - b = ac - c^2 p")
        
        f6 = MathTex(r"""\Rightarrow \left\{\begin{matrix} 
                        q = a\\
                        b = c^2 p
                        \end{matrix}\right.""")
        f7 = MathTex(r"\left\{\begin{matrix}  x' = ax - aut\\t' = -\frac{au}{c^2} x + at \end{matrix}\right.")
        f8_1 = MathTex(r"\left\{\begin{matrix}  x = ax' + aut'\\t = \frac{au}{c^2} x' - at' \end{matrix}\right.")
        f8_2 = MathTex(r"a = \frac{q}{aq-bp} ").move_to([0,-2,0])
        f8_3 = MathTex(r"a = \frac{a}{a^2 - \frac{a^2 u^2}{c^2} } ").move_to([0,-2,0])
        f8_4 = MathTex(r"a = \frac{1}{\sqrt{1-(\frac{u}{c})^2 } } = \gamma ").move_to([0,-2,0])
        f9 = MathTex(r"\left\{\begin{matrix}   x' = \gamma(x - ut) \\    t' = \gamma(t - \frac{ux}{c^2} )\end{matrix}\right. \ \ \ \ \ \ \gamma = \frac{1}{\sqrt{1-(\frac{u}{c})^2 } }")
        
        self.play(Write(f1))
        self.wait()
        self.play(f1.animate.move_to([-6.5,3,0],aligned_edge = UL))
        self.wait()
        self.play(Write(f3_1))
        self.play(f3_1.animate.shift(UP))
        self.wait()
        self.play(Write(f3_2))
        self.wait()
        self.play(ReplacementTransform(f3_2,f3_3))
        self.play(Indicate(f3_1))
        self.wait()
        self.play(ReplacementTransform(f3_3,f3_4))
        self.wait()
        self.play(f3_4.animate.move_to([-6.5,1,0],aligned_edge = UL),Unwrite(f3_1))
        self.wait()
        self.play(Write(f4_1))
        self.play(f4_1.animate.shift(UP))
        self.wait()
        self.play(Write(f4_2))
        self.wait()
        self.play(ReplacementTransform(f4_2,f4_3))
        self.play(Indicate(f4_1))
        self.wait()
        self.play(ReplacementTransform(f4_3,f4_4))
        self.wait()
        self.play(f4_4.animate.move_to([-6.5,0.2,0],aligned_edge = UL),Unwrite(f4_1))
        self.wait()
        self.play(Write(f5_1))
        self.play(f5_1.animate.shift(UP))
        self.wait()
        self.play(Write(f5_2))
        self.wait()
        self.play(ReplacementTransform(f5_2,f5_3))
        self.play(Indicate(f5_1))
        self.wait()
        self.play(ReplacementTransform(f5_3,f5_4))
        self.wait()
        self.play(f5_4.animate.move_to([-6.5,-0.6,0],aligned_edge = UL),Unwrite(f5_1))
        self.wait()
        self.play(Write(f6.shift(LEFT)))
        self.wait()
        self.play(Write(f7.to_edge(RIGHT,buff = 1)))
        self.wait()
        self.play(Unwrite(VGroup(f6,f3_4,f4_4,f5_4)))
        self.play(f7.animate.move_to([-6.5,0,0],aligned_edge = LEFT))
        self.wait()
        self.play(Write(f8_1))
        self.wait()
        self.play(Indicate(f7[0][10]),Indicate(f7[0][11]),Indicate(f7[0][22]),run_time = 2)
        self.play(Indicate(f7[0][21]))
        self.wait()
        self.play(Write(f2.move_to([0,3,0],aligned_edge = UP)))
        self.wait()
        self.play(Write(f8_2))
        self.wait()
        self.play(ReplacementTransform(f8_2,f8_3))
        self.play(ReplacementTransform(f8_3,f8_4))
        self.wait()
        self.play(Unwrite(VGroup(f1,f2,f7,f8_1,f8_4))) 
        self.play(Write(f9))
        self.wait()

class TimeInferenceOfLorentzTransformation(Scene):
    def construct(self):
        f1 = MathTex(r"\begin{matrix}P_1(x_1,t_1) \ \ \ P_2(x_2,t_2)\\P_1'(x_1',t_1') \ \ \ P_2'(x_2',t_2')\end{matrix}").move_to([0,1.8,0])
        f2 = MathTex(r"t_1' = \gamma(t_1 - \frac{ux_1}{c^2} ) \ \ \ t_2' = \gamma (t_2 - \frac{ux_2}{c^2} )").move_to([0,0,0])
        f3 = MathTex(r"t_1'- t_2'= \gamma(t_1 - t_2) + \frac{\gamma u}{c^2}(x_2 - x_1) ").move_to([0,-1.5,0])
        f4 = MathTex(r"t_1'- t_2'= \frac{\gamma u}{c^2}(x_2 - x_1)").move_to([0,-1.5,0])
        f3_ = MathTex(r"t_1'- t_2'= \gamma(t_1 - t_2) + \frac{\gamma u}{c^2}(x_2 - x_1) ").move_to([0,-1.5,0])
        f5 = MathTex(r"t_1'- t_2'= \gamma(t_1 - t_2)").move_to([0,-1.5,0])
        f6 = MathTex(r"\Delta t' = \gamma \Delta t").move_to([0,-1.5,0])

        self.play(Write(f1))
        self.wait()
        self.play(Write(f2))
        self.play(Write(f3))
        self.wait()
        self.play(ReplacementTransform(f3,f4))
        self.wait()
        self.play(ReplacementTransform(f4,f3_))
        self.wait()
        self.play(ReplacementTransform(f3_,f5))
        self.wait()
        self.play(ReplacementTransform(f5,f6))
        self.wait()

class LengthInferenceOfLorentzTransformation(Scene):
    def construct(self):
        f1 = MathTex(r"x = 0").move_to([-4,1.5,0],aligned_edge = LEFT)
        f2 = MathTex(r"x = l").move_to([-4,0.5,0],aligned_edge = LEFT)
        f3 = MathTex(r"\Rightarrow").move_to([-1,1,0])
        f4 = MathTex(r"x' = -ut'").move_to([1,1.5,0],aligned_edge = LEFT)
        f5 = MathTex(r"x' = -ut' + \frac{l}{\gamma }").move_to([1,0.5,0],aligned_edge = LEFT)
        f6 = MathTex(r"l' = \frac{l}{\gamma }").move_to([0,-1.5,0])

        self.play(Write(VGroup(f1,f2)))
        self.wait()
        self.play(Write(f3))
        self.play(Write(VGroup(f4,f5)))
        self.wait()
        self.play(Write(f6))
        self.wait()

class FormulaOfTransformation(Scene):
    def construct(self):    
        f1 = MathTex(r"\left\{\begin{matrix} x' = x - ut \\ t' = t \ \ \ \ \ \ \ \end{matrix}\right. ")
        f2 = MathTex(r"\left\{\begin{matrix}   x' = \gamma(x - ut) \\    t' = \gamma(t - \frac{ux}{c^2} )\end{matrix}\right.")
        
        self.play(Write(f1))
        self.wait()
        self.play(Unwrite(f1))
        self.wait()
        self.play(Write(f2))
        self.wait()

class ReferenceSystem(MovingCameraScene):
    def construct(self):
        self.camera.frame.shift(UP*2.5)
        self.camera.frame.save_state()

        plane = NumberPlane(y_range = [-7,7],y_length = 14)
        lb = VGroup()
        lb += MathTex("x").move_to([6.5,0.5,0])
        lb += MathTex("t").move_to([0.5,6,0])
        
        k = ValueTracker(0)
        func = always_redraw(lambda:plane.plot_parametric_curve(lambda t:np.array([2*np.sin(t),t,0]),
                                           t_range = [0,k.get_value()],
                                           color = GREEN,
                                           stroke_width = 10))
        
        p = always_redraw(lambda:Dot([2*np.sin(k.get_value()),k.get_value(),0],color = WHITE,radius = 0.1))
        hl = always_redraw(lambda:DashedLine(start = p.get_center(),end = [0,p.get_y(),0]))
        vl = always_redraw(lambda:DashedLine(start = p.get_center(),end = [p.get_x(),0,0]))

        p1 = Dot([2*np.sin(1),1,0],color = GREEN,radius = 0.1)
        p2 = Dot([2*np.sin(3),3,0],color = GREEN,radius = 0.1)
        p3 = Dot([2*np.sin(4),4,0],color = GREEN,radius = 0.1)

        self.play(DrawBorderThenFill(plane),Create(lb),run_time  = 2)
        self.wait()
        self.play(Create(VGroup(p1,p2,p3)))
        self.play(Create(VGroup(func,hl,vl,p)))
        self.play(k.animate.set_value(7),run_time = 6,rate_func = rate_functions.linear)

class Transform(Scene):
    def construct(self):
        a1 = Axes(x_range = [0,1],y_range = [0,1],x_length = 4,y_length = 4).shift(LEFT*3)
        a1l = a1.get_axis_labels("x","t")
        o1 = Text("O").move_to(a1.get_origin(),aligned_edge = UR).scale(0.7)
        p1 = Dot(a1@[0.5,0.3],color = RED)
        l1 = a1.get_lines_to_point(a1@[0.5,0.3],color = WHITE)
        p1l = MathTex(r"(x,t)").set_color(RED).move_to(p1.get_corner(UR),aligned_edge = DL)
        s1 = VGroup(a1,a1l,o1,l1,p1,p1l)

        a2 = Axes(x_range = [0,1],y_range = [0,1],x_length = 4,y_length = 4,axis_config = {"color":BLUE}).shift(RIGHT*3)
        a2l = a2.get_axis_labels("x'","t'").set_color(BLUE)
        o2 = Text("O'",color = BLUE).move_to(a2.get_origin(),aligned_edge = UR).scale(0.7)
        p2 = Dot(a2@[0.4,0.6],color = PINK)
        l2 = a2.get_lines_to_point(a2@[0.4,0.6],color = BLUE)
        p2l = MathTex(r"(x',t')").set_color(PINK).move_to(p2.get_corner(UR),aligned_edge = DL)
        s2 = VGroup(a2,a2l,o2,l2,p2,p2l)

        self.play(Create(s1),run_time = 2)
        self.play(Create(s2),run_time = 2)
        self.wait()

class MovingStick(Scene):
    def construct(self):
        k  = ValueTracker(0)
        r = always_redraw(lambda:Rectangle(color = BLUE,height = 1,width = 4,fill_opacity = 0.5).move_to([-4+k.get_value(),0,0]))
        
        self.play(Create(r))
        self.wait()
        self.play(k.animate.set_value(8),run_time = 4,rate_func = rate_functions.linear)

class Relativity(Scene):
    def construct(self):
        f1 = MathTex(r"\left\{\begin{matrix}   x' = \gamma(x - ut) \\    t' = \gamma(t - \frac{ux}{c^2} )\end{matrix}\right. \ \ \ \ \ \ \gamma = \frac{1}{\sqrt{1-(\frac{u}{c})^2 } }").shift(UP)
        f2 = MathTex(r"t_1 = t_2 \Rightarrow t_1' = t_2'").move_to([-3.5,-1,0])
        f3 = MathTex(r"\Delta t = \Delta t'").move_to([0,-2,0])
        f4 = MathTex(r"x_1 - x_2 = x_1' - x_2'").move_to([3.5,-1,0])

        c2 = Cross(f2)
        c3 = Cross(f3)
        c4 = Cross(f4)

        self.add(f1)
        self.wait()
        self.play(Write(f2))
        self.play(Write(f3))
        self.play(Write(f4))
        self.play(Create(c2))
        self.play(Create(c3))
        self.play(Create(c4))
        self.wait()

class InertialSystemsAreEqual(GalileoAndLorentzTransformationScene):
    def construct(self):
        self.add_labels()
        self.add_light(animate = False)

        wl = VGroup()
        c = [RED,ORANGE,YELLOW,GREEN,GREEN_A,BLUE,PURPLE]
        for i in range(0,7):
            g = self.plane.plot_parametric_curve(lambda t:np.array([(-0.75+i*0.25)*t,t,0]),t_range = [-2,10],stroke_width = 10,color = c[i])
            self.transformable_items += [g]
            wl += g
        
        self.add(wl)
        self.lorentz_transformation(0.75,run_time = 3,rate_func = rate_functions.linear)
        self.lorentz_transformation(-0.75,run_time = 3,rate_func = rate_functions.linear)
        self.lorentz_transformation(-0.75,run_time = 3,rate_func = rate_functions.linear)
        
class OneDMove(Scene):
    def construct(self):
        l = NumberLine(x_range = [-6,6],length = 12,stroke_width  = 5,color = BLUE)
        t = ValueTracker(0)
        
        s = always_redraw(lambda:Square(side_length = 1,color = RED,fill_opacity = 0.5).move_to([t.get_value()**2-4*t.get_value(),1,0]))
        p = always_redraw(lambda:Dot(radius = 0.1).move_to(s.get_center()))
        dl = always_redraw(lambda:DashedLine(start = s.get_center(),end = [s.get_x(),0,0]))

        self.play(Create(l))
        self.play(Create(s))
        self.play(Create(VGroup(p,dl)))
        self.play(t.animate.set_value(6),run_time = 6,rate_func = rate_functions.linear)