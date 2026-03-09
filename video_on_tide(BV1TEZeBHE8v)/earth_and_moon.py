from manim import *
from planet import Planet

def get_component(vector,direction,color = None,**kwargs):
    vec = vector.get_end() - vector.get_start()
    e = direction / np.linalg.norm(direction)
    comp = np.dot(vec,e)
    line = DashedLine(start = vector.get_end(),end = vector.get_start() + comp * e,stroke_width=2)
    comp_vec = Arrow(start = vector.get_start(),end = vector.get_start() + comp * e,buff = 0,color = vector.get_color() if color is None else color,**kwargs)
    return VGroup(line, comp_vec)

def torque(direction = 0,color = ORANGE,**kwargs):
    arrow1 = CurvedArrow(start_point = [-0.5,0,0],end_point = [0.5,0,0],angle = 4*PI/5,color = color,**kwargs)
    arrow2 = CurvedArrow(start_point = [0.5,0,0],end_point = [-0.5,0,0],angle = 4*PI/5,color = color,**kwargs)
    return VGroup(arrow1,arrow2) if direction == 0 else VGroup(arrow1,arrow2).rotate(PI,axis = RIGHT)

class DifferentialForce(Scene):
    def construct(self):
        earth = Planet(radius = 2).shift(LEFT*3.5)
        moon = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        earth_center = Dot(earth.c)
        moon_center = Dot(moon.c)
        mass_center = Dot(earth.c + np.array([earth.r*0.7,0,0]),color = YELLOW)
        mass_center_label = Text("地月质心",color= YELLOW).scale(0.5).next_to(mass_center,direction = DOWN,buff = 0.2)
        l = Line(start = earth.c,end = moon.c,color = WHITE)
        
        self.play(FadeIn(earth))
        self.play(FadeIn(moon))
        self.play(Create(VGroup(earth_center,moon_center,mass_center_label,l,mass_center)))
        self.wait()

        self.play(earth.animate.set_opacity(0.4))
        center_force = Arrow(start = earth.c,end = earth.c + np.array([0.9,0,0]),color = RED,buff = 0)
        self.play(Write(center_force))
        self.wait()
        self.play(earth.animate.set_opacity(1))
        self.wait()

        t1 = MathTex(r"F = \frac{GMm}{r^2}").to_edge(UL)
        gravity = earth.gravitational_forces(np.arange(0,2*PI,PI/18),moon.c,0.9,color = ORANGE)
        self.play(Write(VGroup(t1,gravity)))
        self.wait()

        c = Circle(radius = earth.r,color = YELLOW).move_to(earth.c)
        self.play(ShowPassingFlash(c))
        self.play(Indicate(earth_center))
        self.wait()
        self.play(Wiggle(gravity))
        self.play(Wiggle(center_force))
        self.wait()

        t2 = VGroup(MathTex(r"\vec{a}_{\text{tide}}",color = BLUE),MathTex(r"="),MathTex(r"\vec{g}_{\text{surface}}",color = ORANGE),MathTex(r"-"),MathTex(r"\vec{g}_{\text{center}}",color = RED)).arrange(RIGHT).next_to(t1,direction = RIGHT,buff = 1)
        self.play(Write(t2))
        self.wait()

        self.play(FadeOut(VGroup(t1,gravity,mass_center,mass_center_label)),t2.animate.to_edge(UL))
        self.wait()
        
class TidalAcceleration(Scene):
    def construct(self):
        earth = Planet(radius = 2).shift(LEFT*3.5)
        moon = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        earth_center = Dot(earth.c)
        moon_center = Dot(moon.c)
        l = Line(start = earth.c,end = moon.c,color = WHITE)
        center_force = Arrow(start = earth.c,end = earth.c + np.array([0.9,0,0]),color = RED,buff = 0)
        t1 = VGroup(MathTex(r"\vec{a}_{\text{tide}}",color = BLUE),MathTex(r"="),MathTex(r"\vec{g}_{\text{surface}}",color = ORANGE),MathTex(r"-"),MathTex(r"\vec{g}_{\text{center}}",color = RED)).arrange(RIGHT).to_edge(UL)
        
        theta = PI/3
        point_p = Dot(earth.c + earth.r * np.array([np.cos(theta), np.sin(theta), 0]), color = YELLOW)
        
        p_label = Text("P").scale(0.6).next_to(point_p, UP+RIGHT, buff=0.1)
        
        radius_r = Line(earth.c, point_p.get_center(), color = GREEN_B)
        r_label = MathTex("R",color = GREEN_B).scale(0.6).next_to(radius_r.get_center(),direction=UL)
        
        theta_arc = Arc(radius=0.4, start_angle=0, angle=theta, color=GREEN_B,arc_center = earth.c)
        theta_label = MathTex(r"\theta",color = GREEN_B).scale(0.7).next_to(theta_arc,RIGHT+UP*0.2,buff=0.1).shift(DOWN*0.1)
        
        r_distance_label = MathTex("r").scale(0.6).next_to(l, DOWN, buff=0.3)
        
        distance_s = Line(point_p.get_center(), moon.c, color = BLUE)
        s_label = MathTex("s",color = BLUE).scale(0.6).next_to(distance_s.get_center(),direction=UR)
        
        force = earth.gravitational_force(theta,moon.c,1.8)

        force_x = get_component(force,LEFT,color = YELLOW_D,stroke_width = 5)
        
        force_y = get_component(force,UP,color = YELLOW_D,stroke_width = 5)
        
        force_direction = force.get_unit_vector()
        phi_angle = np.arctan2(force_direction[1], force_direction[0])
        phi_arc = Arc(radius=1.1, start_angle=PI, angle=phi_angle, color=BLUE,arc_center = moon.c)
        phi_label = MathTex(r"\phi",color = BLUE).scale(0.7).next_to(phi_arc, LEFT, buff=0.3)
        
        self.add(earth,moon,earth_center,moon_center,l,center_force,t1) 
        
        a = Axes(x_range = [0,1],y_range = [0,1],x_length = 1.2,y_length = 1.2,axis_config = {"stroke_width": 6}).to_edge(UR)
        al = a.get_axis_labels(MathTex("x"),MathTex('y'))
        
        self.play(Create(VGroup(a,al,point_p,p_label,radius_r,r_label,r_distance_label,theta_arc,theta_label,distance_s,s_label,force,force_x,force_y,phi_arc,phi_label)),run_time = 2.5)
        self.wait()

        t2 = MathTex(r"\frac{GM}{s^2}(\cos{\phi}\ \hat{x}-\sin{\phi}\ \hat{y})",color = ORANGE)
        t3 = MathTex(r"-")
        t4 = MathTex(r"\frac{GM}{r^2}\hat{x}",color = RED)
        VGroup(t2,t3,t4).arrange(RIGHT).next_to(t1[1],RIGHT)
        
        self.play(ReplacementTransform(t1[2],t2),ReplacementTransform(t1[3],t3),ReplacementTransform(t1[4],t4))
        self.wait()
        
        earth.save_state()
        moon.save_state()
        self.play(FadeOut(VGroup(earth_center,moon_center,l,center_force,point_p,p_label,radius_r,r_label,r_distance_label,theta_arc,theta_label,distance_s,s_label,force,force_x,force_y,phi_arc,phi_label),run_time = 1))
        self.play(earth.animate.move_to([-6,0,0]).scale_to_fit_width(0.4),moon.animate.move_to([6,0,0]).scale_to_fit_width(0.1),run_time = 2)
        
        r_p = Line(earth.c,moon.c,stroke_width = 2)
        r_p_label = MathTex(r"384404\ \text{km}").scale(0.5).next_to(r_p, DOWN)
        earth_radius = MathTex(r"r_{\text{earth}} = 6371\ \text{km}",color = GRAY).scale(0.5).next_to(earth, DOWN)
        moon_radius = MathTex(r"r_{\text{moon}} = 1737\ \text{km}",color = GRAY).scale(0.5).next_to(moon, DOWN)

        self.play(Write(VGroup(r_p,r_p_label,earth_radius,moon_radius)),run_time = 1.5)
        self.wait()
        
        t5 = MathTex(r"s^2 = (r - R \cos\theta)^2 + (R \sin\theta)^2 \approx r^2 \left(1 - \frac{2R}{r} \cos\theta\right)").scale(0.5).next_to(t4,DOWN).to_edge(LEFT)
        t6 = MathTex(r"\vec{a}_{\text{tide}} \approx \frac{GM}{r^2} \left[ \cos\phi \left(1 + \frac{2R}{r} \cos\theta \right) - 1 \right] \hat{x} - \frac{GM}{r^2} \left[ 1 + \frac{2R}{r} \cos\theta \right] \sin\phi \hat{y}").scale(0.5).next_to(t5,DOWN).to_edge(LEFT)
        t7 = MathTex(r"\cos{\phi} \approx 1, \sin{\phi} \approx \frac{R \sin{\theta}}{r}").scale(0.5).next_to(t6,DOWN).to_edge(LEFT).shift(DOWN*2)
        t8 = VGroup(MathTex(r"\vec{a}_{\text{tide}}",color = BLUE),MathTex(r" \approx \frac{GMR}{r^3} \left(2 \cos\theta \hat{x} - \sin\theta \hat{y}\right)",color = YELLOW)).arrange(RIGHT).next_to(t7,DOWN).to_edge(LEFT)

        self.play(Write(VGroup(t5,t6,t7,t8)))
        self.wait()

        t9 = MathTex(r"\vec F_{\text{tide}} = m\vec a_{\text{tide}}",color = GRAY).next_to(t8,RIGHT,buff = 1.5)
        self.play(Write(t9))
        self.wait(2)

        self.play(FadeOut(VGroup(t1,t2,t3,t4,t5,t6,t7,t9,r_p,r_p_label,earth_radius,moon_radius)),t8.animate.to_edge(UL),Restore(earth),Restore(moon))
        self.play(FadeIn(VGroup(earth_center,moon_center,l)))
        self.wait()

class Tide(Scene):
    def construct(self):
        earth = Planet(radius = 2).shift(LEFT*3.5)
        moon = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        earth_center = Dot(earth.c)
        moon_center = Dot(moon.c)
        l = Line(start = earth.c,end = moon.c,color = WHITE)
        a = Axes(x_range = [0,1],y_range = [0,1],x_length = 1.2,y_length = 1.2,axis_config = {"stroke_width": 6}).to_edge(UR)
        al = a.get_axis_labels(MathTex("x"),MathTex('y'))
        t1 = VGroup(MathTex(r"\vec{a}_{\text{tide}}",color = BLUE),MathTex(r" \approx \frac{GMR}{r^3} \left(2 \cos\theta \hat{x} - \sin\theta \hat{y}\right)",color = YELLOW)).arrange(RIGHT).to_edge(UL)

        self.add(earth,moon,earth_center,moon_center,l,a,al,t1)

        a_tide = earth.tidal_forces(np.arange(0,2*PI,PI/18),0.5)

        self.play(Write(a_tide))
        self.wait()

        water = Circle(radius = 2.4,color = BLUE_B,fill_opacity = 0.5,z_index = -1,stroke_width = 0).move_to(earth.c)
        self.play(FadeOut(a_tide),GrowFromCenter(water))
        self.wait()

        self.play(water.animate.stretch_to_fit_height(4.2).stretch_to_fit_width(5.4),run_time = 2)
        self.wait()

        self.play(Rotate(earth,angle = 2*PI),run_time = 5,rate_func = rate_functions.linear)
        self.wait()

        self.play(FadeOut(VGroup(earth_center,moon_center,l,a,al)),Unwrite(t1),ShrinkToCenter(water),run_time = 0.5)
        self.wait()

class Stretch(Scene):
    def construct(self):
        earth = Planet(radius = 2)
        water = Circle(radius = 2.4,color = BLUE_B,fill_opacity = 0.5,z_index = -1,stroke_width = 0).move_to(earth.c)
        a1 = Arrow([3.5,0,0],[5.5,0,0])
        a2 = Arrow([-3.5,0,0],[-5.5,0,0])
        
        self.add(earth,water)
        self.wait()
        self.play(water.animate.stretch_to_fit_height(4.2).stretch_to_fit_width(5.4),GrowArrow(a1),GrowArrow(a2),run_time = 2)
        self.wait()
        
class Period(Scene):
    def construct(self):
        earth = Planet(radius = 2).shift(LEFT*3.5)
        moon = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        orbit = Circle(radius = 8,color = GRAY,stroke_width = 2).move_to(earth.c)
        
        
        h_l = DashedLine(earth.c,moon.c,color = GRAY)
        l = DashedLine(earth.c,moon.c,color = GRAY,z_index = -1)
        
        def l_update(mob):
            mob.put_start_and_end_on(earth.c,moon.c)
        
        l.add_updater(l_update)
        
        tip = Triangle(color = RED,fill_opacity = 1).scale(0.2).rotate(PI/2).move_to([-1.5,0,0],aligned_edge=LEFT)

        water = Circle(radius = 2.4,color = BLUE_B,fill_opacity = 0.5,z_index = -1,stroke_width = 0).move_to(earth.c).stretch_to_fit_height(4.2).stretch_to_fit_width(5.4)
        self.add(orbit,h_l,l,tip,water,earth,moon)
        self.wait()

        self.play(Rotate(earth,373.2*DEGREES),Rotate(tip,373.2*DEGREES,about_point=earth.c),Rotate(moon,13.2*DEGREES,about_point=earth.c),Rotate(water,13.2*DEGREES,about_point=earth.c),run_time = 5,rate_func = rate_functions.linear)
        self.wait()
        
class TidalTorque(Scene):
    def construct(self):
        earth_i = Planet(radius = 2).shift(LEFT*3.5)
        moon_i = Planet(radius = 0.8,image = "moon.png").shift(RIGHT*4.5)
        
        earth = Planet(radius = 3.5).move_to([-9,0,0])
        moon = Planet(radius = 1.5,image = "moon.png")

        self.add(earth_i,moon_i)
        self.wait()
        self.play(ReplacementTransform(earth_i,earth),ReplacementTransform(moon_i,moon))
        
        moon.z_index = 1
        earth.z_index = 1
        
        orbit = Circle(radius = 9,color = GRAY,z_index = -1).move_to(earth.c)
        l = DashedLine(earth.c,moon.c,color = GRAY_B,z_index = -1)
        
        self.play(GrowFromPoint(VGroup(orbit,l),point = earth.c))
        self.wait()

        moon.z_index = 0
        earth.z_index = 1
        
        tidal_force = moon.tidal_forces(np.arange(0,2*np.pi,np.pi/12),scale = 0.5)
        self.play(Write(tidal_force))
        self.wait()

        lp = Dot(moon.get_edge_center(LEFT))
        rp = Dot(moon.get_edge_center(RIGHT))

        def lp_update(mob):
            mob.move_to(moon.get_edge_center(LEFT))
        
        def rp_update(mob):
            mob.move_to(moon.get_edge_center(RIGHT))
        
        lp.add_updater(lp_update)
        rp.add_updater(rp_update)

        self.play(FadeOut(tidal_force,run_time = 1),FadeIn(lp),FadeIn(rp))
        self.play(moon.stretch_animation(1.1,run_time = 2))
        
        lp.clear_updaters()
        rp.clear_updaters()
        lp.save_state()
        rp.save_state()

        self.wait()

        rotate = torque(stroke_width = 8).move_to(moon.c)

        self.play(SpinInFromNothing(rotate))
        self.wait()
        self.play(FadeOut(rotate))
        self.wait()

        l2 = l.copy()
        self.add(l2)
        
        moon2 = moon.copy()
        moon.save_state()
        moon2.rotate(PI/20,about_point=earth.c).rotate(PI/10,about_point=moon2.c)
        self.play(Transform(moon,moon2,path_arc = PI/20),VGroup(lp,rp).animate.rotate(PI/20,about_point=earth.c).rotate(PI/10,about_point=moon2.c),l2.animate.rotate(PI/20,about_point=earth.c),rate_func = rate_functions.linear)
        self.wait()

        p1 = lp.get_center()
        p2 = rp.get_center()

        l3 = DashedLine(p1,p2,buff = -0.2)
        angle = l3.get_angle()

        self.play(Write(l3),run_time = 0.5)
        self.wait()

        force1 = Arrow(p1,p1 + 2*(earth.c - p1)/np.linalg.norm(earth.c - p1),buff = 0,color = RED)
        force2 = Arrow(p2,p2 + 1.5*(earth.c - p2)/np.linalg.norm(earth.c - p2),buff = 0,color = BLUE)

        force1_comp = get_component(force1,np.array([np.cos(angle+PI/2),np.sin(angle+PI/2),0]))
        force2_comp = get_component(force2,np.array([np.cos(angle+PI/2),np.sin(angle+PI/2),0]))
        
        self.play(Write(VGroup(force1,force2)))
        self.play(Write(VGroup(force1_comp,force2_comp)))
        self.wait()
        
        torque1 = torque(direction = 1,color = ORANGE,stroke_width = 8).move_to(moon2.c).scale(0.7)

        self.play(SpinInFromNothing(torque1,angle = -PI/2))
        self.wait()

        self.play(FadeOut(VGroup(force1,force2,force1_comp,force2_comp,l3,torque1)),run_time = 0.5)
        self.play(l2.animate.rotate(-PI/20,about_point=earth.c),Restore(moon),Restore(lp),Restore(rp),run_time = 0.5)
        self.wait()

        moon3 = moon.copy()
        moon3.rotate(1.5*PI/20,about_point=earth.c).rotate(-PI/20,about_point=moon3.c)
        self.play(Transform(moon,moon3,path_arc = 1.5*PI/20),VGroup(lp,rp).animate.rotate(1.5*PI/20,about_point=earth.c).rotate(-PI/20,about_point=moon3.c),l2.animate.rotate(1.5*PI/20,about_point=earth.c),rate_func = rate_functions.linear)
        self.wait()

        l4 = DashedLine(lp.get_center(),rp.get_center(),buff = 0)

        self.play(Write(l4),run_time = 0.5)
        self.wait()

        torque2 = torque(color = ORANGE,stroke_width = 8).move_to(moon3.c).scale(0.7)
        self.play(SpinInFromNothing(torque2))
        self.wait()

        self.play(FadeOut(VGroup(torque2,l4,lp,rp)),run_time = 0.5)
        self.play(Restore(moon),l2.animate.rotate(-1.5*PI/20,about_point=earth.c),run_time = 0.5)
        self.wait()

class SynchronousRotate(Scene):
    def construct(self):
        earth = Planet(radius = 3.5).move_to([-9,0,0])
        moon = Planet(radius = 1.5,image = "moon.png").stretch_to_fit_width(2 * 1.5 * 1.1).stretch_to_fit_height(2 * 1.5 / 1.1)
        orbit = Circle(radius = 9,color = GRAY,z_index = -1).move_to(earth.c)
        l = DashedLine(earth.c,moon.c,color = GRAY_B,z_index = -1)
        
        self.add(orbit,l,earth,moon)
        self.wait()

        def l_update(mob):
            mob.put_start_and_end_on(earth.c,moon.c) 

        l.add_updater(l_update)

        def orbit_update(mob):
            mob.become(Circle(radius = np.linalg.norm(moon.c - earth.c),color = GRAY,z_index = -1).move_to(earth.c))
        
        orbit.add_updater(orbit_update)
        
        self.play(earth.animate.move_to(ORIGIN).scale_to_fit_width(1.8),moon.animate.move_to([3,0,0]).scale_to_fit_width(0.9))
        self.wait()
        
        self.play(Rotate(earth,27.32*1*PI),Rotate(moon,1*PI,about_point=ORIGIN),run_time = 8,rate_func = rate_functions.linear)




