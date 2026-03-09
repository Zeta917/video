from manim import *

class GalileoAndLorentzTransformationScene(LinearTransformationScene,MovingCameraScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates = False,
            show_basis_vectors = False,
            background_plane_kwargs = {
                "x_range" :[-128/9,128/9],
                "y_range" :[-7,7]
            }
        )
    
    def setup(self) -> None:
        LinearTransformationScene.setup(self)
        
        self.camera.frame.shift(UP*2.5)
        self.camera.frame.save_state()
        
        lb = VGroup()
        lb += MathTex("x/ct_0").move_to([6.5,0.5,0])
        lb += MathTex("t/t_0").move_to([0.5,6,0])
        self.label = lb

        self.transformable_items = [self.plane]
        self.movable_items = []
    
    @staticmethod
    def galileo_matrix(beta):
        return np.array([[1,-beta,0],[0,1,0],[0,0,1]])

    @staticmethod
    def lorentz_matrix(beta):
        gama = 1/np.sqrt(1-beta**2)
        return np.array([[gama,-beta*gama,0],[-beta*gama,gama,0],[0,0,1]])
    
    def apply_transformation(self,func,added_anims = [],run_time = 3,**kwargs):
        anims = [
            ApplyPointwiseFunction(func,mob)
            for mob in self.transformable_items
        ] + [
            mob.animate.move_to(func(mob.get_center()))
            for mob in self.movable_items
        ] + added_anims
        
        self.play(*anims,run_time=run_time,**kwargs)
    
    def galileo_transformation(self, beta, **kwargs):
        self.apply_transformation(lambda point: self.galileo_matrix(beta) @ point, **kwargs)
    
    def lorentz_transformation(self, beta, **kwargs):
        self.apply_transformation(lambda point: self.lorentz_matrix(beta) @ point, **kwargs)
        
    def add_light(self,animate = True):
        light = VGroup()
        light += self.plane.plot(lambda x:x,color = YELLOW,stroke_width = 2)
        light += self.plane.plot(lambda x:-x,color = YELLOW,stroke_width = 2)
        if animate:
            self.play(Create(light))
        else:
            self.add(light)

    def add_labels(self):
        self.add(self.label)