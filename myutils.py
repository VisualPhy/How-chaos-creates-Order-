from manim import*


class ProcessBox(Scene):
    '''creates a text and rectangle around it, to show process 
    '''
    def __init__(self,text, pos=[0,0,0], fillcolor = TEAL, text_size= 1,**kwargs ):
        super().__init__(**kwargs)
        self.text = Text(text).move_to(pos).scale(text_size)

        rect_points = [self.text.get_corner(UL)+[-0.2,0.2,0],
                        self.text.get_corner(UR)+[0.2,0.2,0],
                        self.text.get_corner(DR)+[0.2,-0.2,0],
                        self.text.get_corner(DL)+[-0.2,-0.2,0] ]
        
        self.rect = Polygon(*rect_points,fill_color = fillcolor, fill_opacity=0.5, stroke_width=0).move_to(self.text.get_center())

        self.text.set_z_index(1)
        self.rect.set_z_index(0)
        self.final = VGroup(self.text, self.rect)
        
    def write_text(self, runtime=1):
        return Write(self.text, run_time=runtime)
    def create_rect(self, runtime=1):
        return DrawBorderThenFill(self.rect, run_time=runtime)
    def createall(self, runtime=1):
        return AnimationGroup(
            self.create_rect(),
            self.write_text()
        )
    def move(self, pos):
        return AnimationGroup(self.final.animate.move_to(pos))
    def nextto(self, mob, buff=0):
        return self.final.next_to(mob, buff=buff)
    def nextto_to(self, mob, side,buff=0):
        return self.final.next_to(mob, side, buff=buff)
    def getedge(self, side):
        return self.rect.get_edge_center(side)
    def scale(self, factor):
        return self.final.scale(factor)
    def change_text(self, newtext, runtime=1):
        self.newt = Text(newtext).move_to(self.text.get_center()).scale(self.text.get_height()/Text(newtext).get_height())
        
        anim = ReplacementTransform(self.text, self.newt, run_time=runtime)
        self.text = self.newt
        self.final = VGroup(self.rect, self.text)
        return anim
    def new_text_location(self):
        
        return self.newt.get_center()
    def highlight(self):
        return AnimationGroup(self.rect.animate.set_opacity(0.5), self.text.animate.set_opacity(1))
    def dehighlight(self):
        return AnimationGroup(self.rect.animate.set_opacity(0.1), self.text.animate.set_opacity(0.1))    

    
class ConditionBox(Scene):
    def __init__(self, text, pos=[0,0,0],text_size=1, object_size=1 ,color=YELLOW, **kwargs):
        super().__init__(**kwargs)
        self.text = Text(text).move_to(pos).scale(text_size)
        th = self.text.get_height()
        tw= self.text.get_width()

        diamond_points = [self.text.get_center()+[0,(th+tw)/2+0.2,0],
                        self.text.get_center()+[-(th+tw)/2-0.2,0,0],
                        self.text.get_center()+[0,-(th+tw)/2-0.2,0],
                        self.text.get_center()+[(th+tw)/2+0.2,0,0] ]
        
        self.diamond = Polygon(*diamond_points,fill_color = color, fill_opacity=0.5, stroke_width=0).move_to(self.text.get_center())

        self.text.set_z_index(1)
        self.diamond.set_z_index(0)
        self.final = VGroup(self.text, self.diamond).scale(object_size)

    def create_diamond(self):
        return DrawBorderThenFill(self.diamond)
    def write_text(self):
        return  Write(self.text)
    def create_all(self):
        return AnimationGroup(self.create_diamond(), self.write_text())
    def nexto(self, mob, dirn=RIGHT, buff=0):
        return self.final.next_to(mob, dirn,buff=buff)
    def scale(self, factor):
        return self.final.scale(factor) 
    def getedge(self, side):
        return self.diamond.get_edge_center(side)
    def change_text(self, newtext, runtime=1):
        self.newt = Text(newtext).move_to(self.text.get_center()).scale(self.text.get_height()/Text(newtext).get_height())
        
        anim = ReplacementTransform(self.text, self.newt, run_time=runtime)
        self.text = self.newt
        self.final = VGroup(self.text, self.diamond)
        return anim
    def new_text_location(self):
        
        return self.newt.get_center()
    def highlight(self):
        return AnimationGroup(self.diamond.animate.set_opacity(0.5), self.text.animate.set_opacity(1))
    def dehighlight(self):
        return AnimationGroup(self.diamond.animate.set_opacity(0.1), self.text.animate.set_opacity(0.1))
#copy this into construct function in  order to create shorthands

'''sp = self.play
sw = self.wait
w = Write
uw = Unwrite
c = Create 
uc = Uncreate
fi = FadeIn
fo = FadeOut
sa = self.add
sr = self.remove
ret = ReplacementTransform

dbt = DrawBorderThenFill
mt = MathTex
anc = self.camera.frame.animate
'''
#below are some defined functions (not manim default)

def create_glow(mob,ocity, rad=1, color=TEAL):
    glow_group = VGroup()
    for idx in range(60):
        new_circle = Circle(radius = rad*(1.002**(idx**2))/400, stroke_width=0, fill_color=color, fill_opacity=(0.2-idx/300)*ocity).move_to(mob)
        glow_group.add(new_circle)
        
    return glow_group
def StartProcess(size=1):
    t = Text("Start")
    s = Circle(radius = t.get_width()/2+0.2, fill_color=GREEN,stroke_width=0,stroke_opacity=0.7, fill_opacity=0.7)
    t.set_z_index(1)
    s.set_z_index(0)
    final = VGroup(t,s).scale(size)
    return final

def EndProcess(size=1):
    t = Text("End")
    s = Circle(radius = t.get_width()/2+0.2, fill_color=RED,stroke_width=0, fill_opacity=0.7)
    t.set_z_index(1)
    s.set_z_index(0)
    final = VGroup(t,s).scale(size)
    return final
    

