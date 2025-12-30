from manim import*
import random as r
from myutils import*
import numpy as np

class intro(Scene):
    def construct(self):

        def create_neon_text(text_string, text_color=WHITE, 
                    glow_color=BLUE, font_size=48, **kwargs):
            """
            Creates neon text from scratch with glow effect.
            
            Example usage:
            neon_text = create_neon_text("CHAOS", glow_color=PURPLE)
            self.play(Write(neon_text))
            """
            # Create base text
            base_text = Text(text_string, font_size=font_size, **kwargs)
            base_text.set_color(text_color)
            
            # Create glow layers
            glow_layers = VGroup()
            
            # Create multiple stroke layers with decreasing opacity
            for i in range(15, 0, -1):
                layer = base_text.copy()
                layer.set_stroke(
                    color=glow_color,
                    width=i *2,  # Thicker strokes for outer layers
                    opacity=0.15 - (i * 0.01)  # Decreasing opacity
                )
                layer.set_fill(opacity=0)  # No fill, just stroke
                glow_layers.add(layer)
            
            # Add the base text on top
            final_text = VGroup(glow_layers, base_text)
            
            return final_text
        
        def carpet(n, init_point):
            sq = Square()
            
            
            
            points = [init_point]
            for i in range(n):
                choices = [*sq.get_vertices(), sq.get_edge_center(UP), sq.get_edge_center(DOWN), sq.get_edge_center(LEFT), sq.get_edge_center(RIGHT)]
                r_point = r.choice(choices)
                two_third_point = [(init_point[0]+2*r_point[0])/3, (init_point[1]+2*r_point[1])/3, 0]
                points.append(two_third_point)
                init_point = two_third_point
            return points
        

        def random_noise_in_square(num_points=1000, square_size=5):
            """
            Generate random noise points uniformly distributed in a square.
            
            Parameters:
            -----------
            num_points : int
                Number of random points to generate
            square_size : float
                Side length of the square (centered at origin)
            
            Returns:
            --------
            np.ndarray
                Array of shape (num_points, 3) with (x, y, 0) coordinates
            """
            half_size = square_size / 2
            
            # Generate random x, y coordinates within [-half_size, half_size]
            x_coords = np.random.uniform(-half_size, half_size, num_points)
            y_coords = np.random.uniform(-half_size, half_size, num_points)
            
            # Combine into 3D points (z=0)
            points = np.column_stack([x_coords, y_coords, np.zeros(num_points)])
            
            return points

        points = carpet(50,[r.randint(-100,100)/100, r.randint(-100,100)/100,0])

        dots = VGroup(*[Dot().move_to(p).scale(0.07) for p in points]).scale(3)
        t1 = Text("Number of points").to_edge(RIGHT).scale(0.8)
        t2 = Text("=").next_to(t1, DOWN).scale(0.8)
        glow_dots = VGroup(*[create_glow(dot) for dot in dots])
        vt1 = ValueTracker(50)
        t3 = always_redraw(lambda: Integer(vt1.get_value(), color=YELLOW).next_to(t2, RIGHT))
        g1 = VGroup(t1,t2,t3)
        points2 = carpet(10000-50, points[49])
        

        self.play(Create(dots), run_time=5)       
        self.play(dots.animate.to_edge(LEFT), FadeIn(g1), run_time=0.5) #5.5
        dots2 = VGroup(*[Dot().move_to(p).scale(0.07) for p in points2]).scale(3).move_to(dots)  
        self.play(Create(dots2), vt1.animate.set_value(10000), run_time=5.1) #10.6

        t4 = Text("Sierpinski Carpet", color=TEAL).next_to(t1, UP*5).scale(1.1)


        self.play(Write(t4), run_time=1.8) #12.4
        self.wait(5.6)
        self.play(FadeOut(g1), t4.animate.shift(DOWN*5)) #19

        points3 = random_noise_in_square(500, 1)
        points4 = random_noise_in_square(500, 1)
        points5 = random_noise_in_square(500, 1)
        points6 = random_noise_in_square(500, 1)
        dots3 = VGroup(*[Dot().move_to(p).scale(0.2) for p in points3]).to_edge(UP).shift(RIGHT*3).scale(1.5)
        dots4 = VGroup(*[Dot().move_to(p).scale(0.2) for p in points4]).next_to(dots3, RIGHT, buff=1).scale(1.5)
        dots5 = VGroup(*[Dot().move_to(p).scale(0.2) for p in points5]).next_to(dots4, DOWN, buff=1).scale(1.5)
        dots6 = VGroup(*[Dot().move_to(p).scale(0.2) for p in points6]).next_to(dots5, LEFT, buff=1).scale(1.5)
       
        noise = VGroup(dots3, dots4, dots5, dots6).shift(DOWN*0.5)
        o1 = VGroup(*[SurroundingRectangle(i, stroke_width=1, stroke_color=YELLOW) for i in noise])
        o2 = SurroundingRectangle(noise, stroke_color=WHITE,stroke_width=1).scale(1.2)
        t5 = MathTex(r"Noise ?").next_to(o2, DOWN)


        
        self.play(Create(noise), Create(o1), Create(o2), Write(t5), run_time=1.5) #20.5


        d1 = Dot().set_opacity(0)
        o3 = SurroundingRectangle(dots).set_opacity(0)
        o4 = TracedPath(d1.get_center,dissipating_time=0.8,stroke_width=4, stroke_opacity=[0, 1])
        self.add(o4)
        self.play(MoveAlongPath(d1, o3), run_time=2.5) #23

        scene1 = VGroup(dots, dots2, noise, o1, o2, t5, t4)
        text = Text("The Chaos Game")
        
        self.wait(7)
        self.play(ReplacementTransform(scene1, text)) #31
        # Color schemes for arcane/vibe effect
        color_schemes = [
            ["#FF6B6B", "#4ECDC4", "#FFD166", "#06D6A0"],  # Neon arcade
            ["#9D4EDD", "#FF9E00", "#00BBF9", "#F15BB5"],  # Cyberpunk
            ["#00F5D4", "#FF006E", "#8338EC", "#FB5607"],  # Electric
            ["#00F5FF", "#FF00AA", "#9D00FF", "#00FF9D"],  # Synthwave
            ["#FF0055", "#00FFAA", "#AA00FF", "#FFAA00"],  
        ]
        

        # Create initial text with random colors
        
        
        # Center the text
        
        
        # Animate with multiple color changes
        
        
        # First color change - rapid flash
        for i in range(5):
            for letter in text:
                letter.set_color(r.choice(color_schemes[i]))
            self.wait(0.2)
        for i in range(5):
            for letter in text:
                letter.set_color(r.choice(color_schemes[i]))
            self.wait(0.2)
            
        

        





        self.wait()

class s1(Scene):
    def construct(self):

        sw = self.wait
        sp = self.play
        sa = self.add
        sr = self.remove
        
        mt = MathTex

        w = Write
        fi = FadeIn
        fo = FadeOut
        c = Create

        s = Square(stroke_color=TEAL, stroke_width=1).scale(1.5).scale(1.5)
        la = Text("A").next_to(s.get_corner(DL), DOWN*0.1 + LEFT*0.1).scale(0.3)
        lb = Text("B").next_to(s.get_corner(DR), DOWN*0.1 + RIGHT*0.1).scale(0.3)
        lc = Text("C").next_to(s.get_corner(UR), UP*0.1 + RIGHT*0.1).scale(0.3)
        ld = Text("D").next_to(s.get_corner(UL), UP*0.1 + LEFT*0.1).scale(0.3)

        le = Text("E").next_to(s.get_edge_center(DOWN), DOWN*0.1).scale(0.3)
        lf = Text("F").next_to(s.get_edge_center(RIGHT), RIGHT*0.1).scale(0.3)
        lg = Text("G").next_to(s.get_edge_center(UP), UP*0.1).scale(0.3)
        lh = Text("H").next_to(s.get_edge_center(LEFT), LEFT*0.1).scale(0.3)

        labels = VGroup(la, le ,lb, lf, lc,lg, ld, lh)
        s1 = VGroup(s, labels)
        sw(1.5)
        sp(c(s)) #2.5
        sw(1.5) #4
        sp(fi(labels, lag_ratio=0.1), run_time=3)#7

        p1 = Dot().scale(0.5).move_to([-1,2,0])
        p1l = Integer(0).scale(0.5).next_to(p1, DOWN*0.1)
        sw(3) #10
        sp(fi(p1)) #11
        sw(1)
        sp(fi(p1l))#13

        def roll_die(n, labels, i):
            box = Square(stroke_width=1, fill_color=GREY, fill_opacity=0.4).scale(0.2).move_to(labels[i])

            for j in range(n):

                if i>=7:
                    i = -1
                sa(box)
                sw(0.15)
                if j==n-1:
                    return box
                sr(box)
                box.move_to(labels[i+1])
                i+=1

        def drawserpwithlines(iterations, init_point, stop_time, lines, points):
            choice_list = [s.get_corner(UL),s.get_corner(UR),s.get_corner(DL),s.get_corner(DR),
                           s.get_edge_center(DOWN),s.get_edge_center(UP),s.get_edge_center(LEFT),s.get_edge_center(RIGHT)]
            
            for i in range(iterations):
                choice = r.choice(choice_list)
                l = Line(init_point, choice, stroke_width=1)

                p2 = Dot().scale(0.5).move_to([(2*choice[0] + init_point[0])/3,
                                        (2*choice[1] + init_point[1])/3,
                                            0])
                sa(l, p2)
                sw(stop_time)
                #sr(l)
                lines.add(l)
                points.add(p2)

                init_point = p2.get_center()

            return init_point

        sw(9)#23  -1 from here
        b1 = roll_die(18,labels,0) #(2.7) #25.7

        p2 = Dot().scale(0.5).move_to([(2*s.get_edge_center(DOWN)[0] + p1.get_center()[0])/3,
                                       (2*s.get_edge_center(DOWN)[1] + p1.get_center()[1])/3,
                                        0])
        p2l = Integer(1).scale(0.5).next_to(p2, DOWN*0.1)
        li1 = Line(p1.get_center(), s.get_edge_center(DOWN), stroke_width=1, stroke_color=BLUE_D)
        t1 = mt(r"2:1").scale(0.5).next_to(p2, RIGHT)


        sw(6) #29
        sp(c(li1))#30
        sp(fi(p2), fi(t1))#31
        sw(4.5) #35.5
        sp(fi(p2l))#36.5
        
        sp(fo(li1), fo(b1),fo(t1),run_time=0.4)#37.5
        sw(2.5) #40
        b2 = roll_die(11, labels, 1) #(1.65)#41.5


        p3 = Dot().scale(0.5).move_to([(2*s.get_edge_center(RIGHT)[0] + p2.get_center()[0])/3,
                                       (2*s.get_edge_center(RIGHT)[1] + p2.get_center()[1])/3,
                                        0])
        p3l = Integer(2).scale(0.5).next_to(p3, DOWN*0.1)
        li2 = Line(p2.get_center(), s.get_edge_center(RIGHT), stroke_width=1, stroke_color=BLUE_D)
        
        sw(1) #42.5
        sp(c(li2))
        sp(fi(p3), fi(p3l))
        sp(fo(li2), fo(b2)) #45.5

        lines = VGroup()
        points = VGroup()
        sp(fo(p1l), fo(p2l), fo(p3l))

        
        
        last_point1 = drawserpwithlines(5, p3.get_center(), stop_time=0.5, lines=lines, points=points)
        last_point2 = drawserpwithlines(10, last_point1, stop_time=0.25, lines=lines, points=points)
        last_point3 = drawserpwithlines(35, last_point2, stop_time=0.12, lines=lines, points=points)

        scene1 = VGroup(s, labels,p1, p2,p3, lines, points)


        sp(scene1.animate.scale(0.8).to_edge(RIGHT))

        c1 = ImageMobject("c1").scale(0.2)
        t1 = mt(r"n=100", color=YELLOW).next_to(c1, DOWN).scale(0.5)
        
        c2 = ImageMobject("c2").scale(0.2).next_to(c1, RIGHT)
        t2 = mt(r"n=500", color=YELLOW).next_to(c2, DOWN).scale(0.5)
        
        c3 = ImageMobject("c3").scale(0.2).next_to(c2, RIGHT)
        t3 = mt(r"n=1000", color=YELLOW).next_to(c3, DOWN).scale(0.5)
        
        c4 = ImageMobject("c4").scale(0.2).next_to(t1, DOWN)
        t4 = mt(r"n=5000", color=YELLOW).next_to(c4, DOWN).scale(0.5)
        
        c5 = ImageMobject("c5").scale(0.2).next_to(c4, RIGHT)
        t5 = mt(r"n=10000", color=YELLOW).next_to(c5, DOWN).scale(0.5)
        
        c6 = ImageMobject("c6").scale(0.2).next_to(c5, RIGHT)
        t6 = mt(r"n=50000", color=YELLOW).next_to(c6, DOWN).scale(0.5)
        
        o1 = SurroundingRectangle(c1, stroke_color=WHITE,stroke_width=1)
        o2 = SurroundingRectangle(c2,stroke_color=WHITE, stroke_width=1)
        o3 = SurroundingRectangle(c3, stroke_color=WHITE,stroke_width=1)
        o4 = SurroundingRectangle(c4,stroke_color=WHITE, stroke_width=1)
        o5 = SurroundingRectangle(c5,stroke_color=WHITE, stroke_width=1)
        o6 = SurroundingRectangle(c6, stroke_color=WHITE,stroke_width=1)

        g1 = Group(c1,c2,c3,c4,c5,c6, t1,t2,t3,t4,t5,t6,o1,o2,o3,o4,o5,o6).to_edge(LEFT).shift(UP*1.5)
        g2 = Group(c1,c2,c3,c4,c5,c6)
        g3 = VGroup(o1,o2,o3,o4,o5,o6)
        g4 = VGroup(t1,t2,t3,t4,t5,t6)
        sp(fi(g2, lag_ratio=0.3), c(g3, lag_ratio=0.3), w(g4, lag_ratio=0.3))

        sw(10)

class s2(Scene):
    def construct(self):

        sw = self.wait
        sp = self.play
        sa = self.add
        sr = self.remove
        
        mt = MathTex

        w = Write
        fi = FadeIn
        fo = FadeOut
        c = Create

        s = Square(stroke_color=TEAL, stroke_width=1).scale(1.5).scale(1.5)
        la = Text("A").next_to(s.get_corner(DL), DOWN*0.1 + LEFT*0.1).scale(0.3)
        lb = Text("B").next_to(s.get_corner(DR), DOWN*0.1 + RIGHT*0.1).scale(0.3)
        lc = Text("C").next_to(s.get_corner(UR), UP*0.1 + RIGHT*0.1).scale(0.3)
        ld = Text("D").next_to(s.get_corner(UL), UP*0.1 + LEFT*0.1).scale(0.3)

        le = Text("E").next_to(s.get_edge_center(DOWN), DOWN*0.1).scale(0.3)
        lf = Text("F").next_to(s.get_edge_center(RIGHT), RIGHT*0.1).scale(0.3)
        lg = Text("G").next_to(s.get_edge_center(UP), UP*0.1).scale(0.3)
        lh = Text("H").next_to(s.get_edge_center(LEFT), LEFT*0.1).scale(0.3)

        labels = VGroup(la, le ,lb, lf, lc,lg, ld, lh)
        s1 = VGroup(s, labels)

        def roll_die(n, labels, i):
            box = Square(stroke_width=1, fill_color=GREY, fill_opacity=0.4).scale(0.2).move_to(labels[i])

            for j in range(n):

                if i>=7:
                    i = -1
                sa(box)
                sw(0.15)
                if j==n-1:
                    return box
                sr(box)
                box.move_to(labels[i+1])
                i+=1

        def twothird(init_point, target):
            return [(2*target[0]+ init_point[0])/3,
                    (2*target[1]+ init_point[1])/3,
                    0]
    
        sp(fi(s1))
        sw(5) #6

        p1 = Dot().scale(0.5).move_to([-1,-2,0])
        p1l = Integer(0).scale(0.5).next_to(p1, DOWN*0.1)

        sp(fi(p1), fi(p1l), run_time=2) #9
        sw(1)#10
        b1 = roll_die(13, labels, 0) #(2) 12
        sw(9)

        length = (s.get_arc_length()/4)
        sA = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN+LEFT)*length/3)
        sB = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN+RIGHT)*length/3)
        sC = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP+RIGHT)*length/3)
        sD = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP+LEFT)*length/3)
        sE = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN)*length/3)
        sF = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((RIGHT)*length/3)
        sG = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP)*length/3)
        sH = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((LEFT)*length/3)
        shaded_sqs = VGroup(sA, sB,sD,sE,sG,sH)


        sp(fi(sC)) #22


        p2 = Dot().scale(0.5).move_to([(2*s.get_corner(UR)[0] + p1.get_center()[0])/3,
                                       (2*s.get_corner(UR)[1] + p1.get_center()[1])/3,
                                        0])
        p2l = Integer(1).scale(0.5).next_to(p2, DOWN*0.1)
        li1 = Line(p1.get_center(), s.get_corner(UR), stroke_width=1, stroke_color=BLUE_D)


        sp(fi(li1), fi(p2), fi(p2l)) #23
        sw(6)

        trial_points = [[1.56, 2.01, 0], [1.56, -1.94, 0], [0.1, 1.4, 0], [1.16, 1.74, 0], [1.83, 1.3, 0], [-1.3, 1.82, 0], [1.95, 1.64, 0], [0.92, -2.05, 0], [-1.23, -0.02, 0], [-0.91, -2.11, 0], [0.64, 1.86, 0], [1.45, 0.18, 0], [0.34, -1.0, 0], [-2.01, -2.0, 0], [0.94, -1.62, 0], [0.31, 0.2, 0], [-0.41, -0.45, 0], [1.79, -0.36, 0], [0.07, 1.6, 0], [-2.07, -2.08, 0], [-1.4, 0.21, 0], [-1.57, 1.43, 0], [-1.59, 0.53, 0], [-2.0, -0.05, 0], [0.74, -1.8, 0], [-1.29, -0.35, 0], [-1.35, -0.99, 0], [0.82, 0.29, 0], [-1.99, 2.02, 0], [-1.05, 1.78, 0], [1.36, -1.04, 0], [0.35, 0.29, 0], [-1.0, 0.88, 0], [0.97, -1.54, 0], [-0.68, -0.06, 0], [1.92, 0.53, 0], [0.9, -0.28, 0], [1.18, 1.56, 0], [-0.13, 2.15, 0], [0.83, -1.45, 0], [1.07, -0.34, 0], [-0.42, 2.06, 0], [1.96, 0.09, 0], [-0.51, 1.2, 0], [-1.25, 1.54, 0], [-1.0, 0.77, 0], [1.07, -1.59, 0], [-0.86, 1.11, 0], [-0.32, 0.95, 0], [-1.87, -2.04, 0]]
        trial_dots = VGroup(*[Dot(color=WHITE).scale(0.5).move_to(p) for p in trial_points])
        trial_linesC = VGroup(*[Line(p, s.get_corner(UR), stroke_width=1, stroke_color=TEAL) for p in trial_points])


        sp(fi(trial_dots, lag_ratio=0.1)) #30
        sp(trial_dots.animate.set_opacity(0.2))#31


        two_third_pointsA = VGroup(*[Dot(color=BLUE_A).scale(0.5).move_to(twothird(p, s.get_corner(DL))) for p in trial_points])
        two_third_pointsB = VGroup(*[Dot(color=BLUE_C).scale(0.5).move_to(twothird(p, s.get_corner(DR))) for p in trial_points])
        two_third_pointsC = VGroup(*[Dot(color=GREEN_A).scale(0.5).move_to(twothird(p, s.get_corner(UR))) for p in trial_points])
        two_third_pointsD = VGroup(*[Dot(color=GREEN_C).scale(0.5).move_to(twothird(p, s.get_corner(UL))) for p in trial_points])
        two_third_pointsE = VGroup(*[Dot(color=YELLOW_A).scale(0.5).move_to(twothird(p, s.get_edge_center(DOWN))) for p in trial_points])
        two_third_pointsF = VGroup(*[Dot(color=YELLOW_C).scale(0.5).move_to(twothird(p, s.get_edge_center(RIGHT))) for p in trial_points])
        two_third_pointsG = VGroup(*[Dot(color=RED_A).scale(0.5).move_to(twothird(p, s.get_edge_center(UP))) for p in trial_points])
        two_third_pointsH = VGroup(*[Dot(color=RED_C).scale(0.5).move_to(twothird(p, s.get_edge_center(LEFT))) for p in trial_points])
        trial_two_thirds_all = VGroup(two_third_pointsA,two_third_pointsB,two_third_pointsD, two_third_pointsE, two_third_pointsG, two_third_pointsH)


        sp(c(two_third_pointsC, lag_ratio=0.1), c(trial_linesC, lag_ratio=0.1)) #32
        sw(4)
        sp(fo(trial_linesC), fo(li1), fo(p1l), fo(p2l)) #37

        
        trial_linesF = VGroup(*[Line(p, s.get_edge_center(RIGHT), stroke_width=1, stroke_color=TEAL) for p in trial_points])
        sw(4)
        sp(c(trial_linesF, lag_ratio=0.1), c(two_third_pointsF, lag_ratio=0.1)) #42
        sw(1)
        sp(b1.animate.move_to(lf))
        sp(fi(sF)) #45
        sp(fo(trial_linesF), fo(b1))#46


        for i in range(len(shaded_sqs)): #(1.8)
            sp(fi(trial_two_thirds_all[i]), fi(shaded_sqs[i]), run_time=0.3)
        sw(0.2) #48
        sp(fo(trial_dots))
        sp(fo(trial_two_thirds_all), fo(two_third_pointsC), fo(two_third_pointsF), fo(p1), fo(p2))
        sw(12)
        r1 = Square(side_length=length/3, fill_color=RED, fill_opacity=0.7, stroke_width=0)
        t1 = Text("Can't lie in\n this region").scale(0.3)
        sp(fi(r1), w(t1)) #1.01
        sp(fo(t1))

        shaded_sqs.add(sC, sF)
        carpet = VGroup(s, labels, shaded_sqs, r1)

        step1 = Text("Steps = 1").shift(RIGHT*2)
        step2 = Text("Steps = 2").shift(RIGHT*2)
        step3 = Text("Steps = 3").shift(RIGHT*2)
        sw(1)
        sp(carpet.animate.to_edge(LEFT), fi(step1)) #1.04
        sw(5)
        sp(shaded_sqs.animate.set_opacity(1), r1.animate.set_opacity(1))#1.10


        sq = VGroup()
        for i in range(-1, 2):  # -1, 0, 1
            for j in range(-1, 2):  # -1, 0, 1
                r = Square(
                    side_length=length/9,  # For Sierpinski carpet pattern
                    fill_color=RED, 
                    fill_opacity=1, 
                    stroke_width=0
                ).move_to([i * length/3, j * length/3, 0])  # Spacing is 1/3 of main square
                sq.add(r)
        sq.move_to(s.get_center())

        sa(sq)
        sr(step1)
        sa(step2)
        sw(1)

        sq2 = VGroup()
        for i in range(-4, 5):  # -1, 0, 1
            for j in range(-4, 5):  # -1, 0, 1
                r = Square(
                    side_length=length/27,  # For Sierpinski carpet pattern
                    fill_color=RED, 
                    fill_opacity=1, 
                    stroke_width=0
                ).move_to([i * length/9, j * length/9, 0])  # Spacing is 1/3 of main square
                sq2.add(r)
        sq2.move_to(s.get_center())
        sa(sq2)
        sr(step2)
        sa(step3)
        sw(1)

        scene1 = VGroup(s, labels ,shaded_sqs,r1, sq,sq2,step3)
        sd = Square(stroke_color=TEAL, stroke_width=1).scale(1.5).scale(1.5)
        la1 = Text("A").next_to(sd.get_corner(DL), DOWN*0.1 + LEFT*0.1).scale(0.3)
        lb1 = Text("B").next_to(sd.get_corner(DR), DOWN*0.1 + RIGHT*0.1).scale(0.3)
        lc1 = Text("C").next_to(sd.get_corner(UR), UP*0.1 + RIGHT*0.1).scale(0.3)
        ld1 = Text("D").next_to(sd.get_corner(UL), UP*0.1 + LEFT*0.1).scale(0.3)

        le1 = Text("E").next_to(sd.get_edge_center(DOWN), DOWN*0.1).scale(0.3)
        lf1 = Text("F").next_to(sd.get_edge_center(RIGHT), RIGHT*0.1).scale(0.3)
        lg1 = Text("G").next_to(sd.get_edge_center(UP), UP*0.1).scale(0.3)
        lh1 = Text("H").next_to(sd.get_edge_center(LEFT), LEFT*0.1).scale(0.3)

        labels1 = VGroup(la1, le1 ,lb1, lf1, lc1,lg1, ld1, lh1)
        s11 = VGroup(sd, labels1)
        s11.move_to(ORIGIN)
        sp(ReplacementTransform(scene1,s11))
        
        sw(2)






        



















        sw(1)


        


        













        sw(1)
        
