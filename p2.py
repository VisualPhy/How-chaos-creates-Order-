from manim import*
from myutils import*
import random as rd

class s3(Scene):
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

        def roll_die(n, labels, i):
            box = Square(stroke_width=1, fill_color=GREY, fill_opacity=0.4).scale(0.2).move_to(labels[i])

            for j in range(n):

                if i>=7:
                    i = -1
                sa(box)
                sw(0.1)
                if j==n-1:
                    return box
                sr(box)
                box.move_to(labels[i+1])
                i+=1
        def twothird(init_point, target):
            return [(2*target[0]+ init_point[0])/3,
                    (2*target[1]+ init_point[1])/3,
                    0]

        s = Square(stroke_color=TEAL, stroke_width=1).scale(1.5).scale(1.5)
        la1 = Text("A").next_to(s.get_corner(DL), DOWN*0.1 + LEFT*0.1).scale(0.3)
        lb1 = Text("B").next_to(s.get_corner(DR), DOWN*0.1 + RIGHT*0.1).scale(0.3)
        lc1 = Text("C").next_to(s.get_corner(UR), UP*0.1 + RIGHT*0.1).scale(0.3)
        ld1 = Text("D").next_to(s.get_corner(UL), UP*0.1 + LEFT*0.1).scale(0.3)
        le1 = Text("E").next_to(s.get_edge_center(DOWN), DOWN*0.1).scale(0.3)
        lf1 = Text("F").next_to(s.get_edge_center(RIGHT), RIGHT*0.1).scale(0.3)
        lg1 = Text("G").next_to(s.get_edge_center(UP), UP*0.1).scale(0.3)
        lh1 = Text("H").next_to(s.get_edge_center(LEFT), LEFT*0.1).scale(0.3)

        labels1 = VGroup(la1, le1 ,lb1, lf1, lc1,lg1, ld1, lh1)
        s11 = VGroup(s, labels1)
        s11.move_to(ORIGIN)

        sa(s11)
        sw(1.05)

        b1 = roll_die(13, labels1, 0)#3
        length = (s.get_arc_length()/4)
        sA = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN+LEFT)*length/3)
        sB = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN+RIGHT)*length/3)
        sC = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP+RIGHT)*length/3)
        sD = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP+LEFT)*length/3)
        sE = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((DOWN)*length/3)
        sF = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((RIGHT)*length/3)
        sG = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((UP)*length/3)
        sH = Square(side_length=length/3,fill_color=GREY, stroke_width=0,fill_opacity=0.5).shift((LEFT)*length/3)
        shaded_sqs = VGroup(sA, sB,sC,sD,sE,sF,sG,sH)
        trial_points = [[1.56, 2.01, 0], [1.56, -1.94, 0], [0.1, 1.4, 0], [1.16, 1.74, 0], [1.83, 1.3, 0], [-1.3, 1.82, 0], [1.95, 1.64, 0], [0.92, -2.05, 0], [-1.23, -0.02, 0], [-0.91, -2.11, 0], [0.64, 1.86, 0], [1.45, 0.18, 0], [0.34, -1.0, 0], [-2.01, -2.0, 0], [0.94, -1.62, 0], [0.31, 0.2, 0], [-0.41, -0.45, 0], [1.79, -0.36, 0], [0.07, 1.6, 0], [-2.07, -2.08, 0], [-1.4, 0.21, 0], [-1.57, 1.43, 0], [-1.59, 0.53, 0], [-2.0, -0.05, 0], [0.74, -1.8, 0], [-1.29, -0.35, 0], [-1.35, -0.99, 0], [0.82, 0.29, 0], [-1.99, 2.02, 0], [-1.05, 1.78, 0], [1.36, -1.04, 0], [0.35, 0.29, 0], [-1.0, 0.88, 0], [0.97, -1.54, 0], [-0.68, -0.06, 0], [1.92, 0.53, 0], [0.9, -0.28, 0], [1.18, 1.56, 0], [-0.13, 2.15, 0], [0.83, -1.45, 0], [1.07, -0.34, 0], [-0.42, 2.06, 0], [1.96, 0.09, 0], [-0.51, 1.2, 0], [-1.25, 1.54, 0], [-1.0, 0.77, 0], [1.07, -1.59, 0], [-0.86, 1.11, 0], [-0.32, 0.95, 0], [-1.87, -2.04, 0]]
        two_third_pointsA = VGroup(*[Dot(color=BLUE_A).scale(0.5).move_to(twothird(p, s.get_corner(DL))) for p in trial_points])
        two_third_pointsB = VGroup(*[Dot(color=BLUE_C).scale(0.5).move_to(twothird(p, s.get_corner(DR))) for p in trial_points])
        two_third_pointsC = VGroup(*[Dot(color=GREEN_A).scale(0.5).move_to(twothird(p, s.get_corner(UR))) for p in trial_points])
        two_third_pointsD = VGroup(*[Dot(color=GREEN_C).scale(0.5).move_to(twothird(p, s.get_corner(UL))) for p in trial_points])
        two_third_pointsE = VGroup(*[Dot(color=YELLOW_A).scale(0.5).move_to(twothird(p, s.get_edge_center(DOWN))) for p in trial_points])
        two_third_pointsF = VGroup(*[Dot(color=YELLOW_C).scale(0.5).move_to(twothird(p, s.get_edge_center(RIGHT))) for p in trial_points])
        two_third_pointsG = VGroup(*[Dot(color=RED_A).scale(0.5).move_to(twothird(p, s.get_edge_center(UP))) for p in trial_points])
        two_third_pointsH = VGroup(*[Dot(color=RED_C).scale(0.5).move_to(twothird(p, s.get_edge_center(LEFT))) for p in trial_points])
        trial_two_thirds_all = VGroup(two_third_pointsA,two_third_pointsB,two_third_pointsD, two_third_pointsE, two_third_pointsG, two_third_pointsH)

        t1 = Text("Possible points on rolling C").scale(0.4).next_to(lc1, (UP)*2)
        a1 = Line(t1.get_edge_center(DOWN), sC.get_center()).add_tip(tip_length=0.2, tip_width=0.2)
        sw(3)
        sp(fi(sC), fi(two_third_pointsC), w(t1), c(a1), fo(b1))#7
        sw(1.75)
        b2 = roll_die(15, labels1, 0)#11
        l1 = []

        



        two3rdofDdots = VGroup(*[Dot().scale(0.5).move_to(twothird(p, s.get_corner(UL))) for p in list(map(lambda d: d.get_center(), two_third_pointsC))])
        two3rdofDlines = VGroup(*[Line(p, s.get_corner(UL), stroke_width=1, stroke_color=TEAL) for p in list(map(lambda d: d.get_center(), two_third_pointsC))])
        

        
        trial_two_thirds_all.set_opacity(0)
        two_third_pointsF.set_opacity(0)
        scene1 = VGroup(s11,trial_two_thirds_all, two_third_pointsC, two3rdofDdots, two_third_pointsF)

        sw(3)
        sp(fi(two3rdofDdots), fi(two3rdofDlines))#15
        sw(9)
        sp(Unwrite(t1), scene1.animate.to_edge(LEFT), fo(two3rdofDlines), fo(b2), fo(sC), fo(a1))#25


        t2 = mt(r"1^{st} \text{ roll}").shift(RIGHT*2)
        t3 = mt(r"2^{nd} \text{ roll}").next_to(t2, RIGHT, buff=1)
        sw(2)
        sp(w(t2),w(t3)) #28

        second_roll_all_dots = []
        sr(trial_two_thirds_all, two_third_pointsF)
        trial_two_thirds_all.set_opacity(1)
        two_third_pointsF.set_opacity(1)
        first_roll_all_dots = VGroup(two_third_pointsC,two_third_pointsA,two_third_pointsB,two_third_pointsD, two_third_pointsE,two_third_pointsF, two_third_pointsG, two_third_pointsH)
        p1 = [s.get_corner(DL),s.get_corner(DR),s.get_corner(UR),s.get_corner(UL),
              s.get_edge_center(DOWN),s.get_edge_center(RIGHT),s.get_edge_center(UP),s.get_edge_center(LEFT)]
        
        first_roll=['C','A', 'B', 'D', 'E', 'F','G','H']
        second_roll=['A', 'B', 'C', 'D', 'E', 'F','G','H']
        for i in range(8):
            sa(first_roll_all_dots[i])
            for j in range(8):
                dots = VGroup(*[Dot().scale(0.5).move_to(twothird(p, p1[j])) for p in list(map(lambda d: d.get_center(), first_roll_all_dots[i]))])
                lines = VGroup(*[Line(p.get_center(), p1[j], stroke_width=1, stroke_color=TEAL) for p in first_roll_all_dots[i]])
                t4 = Text(f"{first_roll[i]}", color=YELLOW).next_to(t2, DOWN)
                t5 = Text(f"{second_roll[j]}", color=YELLOW).next_to(t3, DOWN)

                sa(t4,t5, dots,lines)
                sw(0.3)
                sr(t4,t5,lines)
            sr(first_roll_all_dots[i])

        #47.2
        sw(10.8)
        #58
        sw(1)
class s4(Scene):
    
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
        o3 = mt(r"\neq").scale(3)
        o1 = ImageMobject("c6").scale(0.53).next_to(o3, LEFT)
        
        o2 = ImageMobject("ideal_serp").next_to(o3, RIGHT).scale(0.5)

        g1 = Group(o1,o2).move_to(ORIGIN)
        g2 = Group(g1,o3).scale(0.8)

        t1 = Text("By Chaos Game", color=TEAL).next_to(o1, DOWN).scale(0.7)
        t2 = Text("Ideal One", color=YELLOW).next_to(o2, DOWN).scale(0.7)
        
        
        

        sp(fi(g1), w(t1), w(t2), run_time=2)
        sw(1.5) 
        sp(fi(o3), run_time=0.5) #4
        
        

        

        

        d1 = Dot().move_to(o1.get_center()).scale(0.7)
        glow = create_glow(d1, color=GREEN)
        sw(5)
        sp(fi(d1)) #10
        for i in range(3):
            sp(fi(glow), run_time=0.5)
            sp(fo(glow), run_time=0.5)

        #13
        sw(11)
        sp(fo(g1), fo(d1)) #25

        def carpet(n, init_point):
            sq = Square()
            
            
            
            points = [init_point]
            for i in range(n):
                choices = [*sq.get_vertices(), sq.get_edge_center(UP), sq.get_edge_center(DOWN), sq.get_edge_center(LEFT), sq.get_edge_center(RIGHT)]
                r_point = rd.choice(choices)
                two_third_point = [(init_point[0]+2*r_point[0])/3, (init_point[1]+2*r_point[1])/3, 0]
                points.append(two_third_point)
                init_point = two_third_point
            return points

        points = carpet(10000,[rd.randint(-100,100)/100, rd.randint(-100,100)/100,0])
        t3 = mt(r"n = ")
        n = ValueTracker(0)
        
        
        dots = VGroup(*[Dot(color=GRAY_A).move_to(p).scale(0.2/3) for p in points]).move_to(o1.get_center()).scale(2.7)
        t4 = always_redraw(lambda: Integer(n.get_value()).next_to(dots,UP))
        g3 = VGroup(t3,t4).next_to(dots, UP)
        sa(t4)

        s = Square(side_length=3,stroke_color=TEAL, stroke_width=0, fill_color=WHITE, fill_opacity=1)
        length = s.side_length  # Use side_length instead of get_arc_length()/4
        
        sq = VGroup()
        r1 = Square(side_length=length/3, fill_color=BLACK, fill_opacity=1, stroke_width=0)
        
        # Fixed loop ranges - from -1 to 1 inclusive (3 positions)
        for i in range(-1, 2):  # -1, 0, 1
            for j in range(-1, 2):  # -1, 0, 1
                r = Square(
                    side_length=length/9,  # For Sierpinski carpet pattern
                    fill_color=BLACK, 
                    fill_opacity=1, 
                    stroke_width=0
                ).move_to([i * length/3, j * length/3, 0])  # Spacing is 1/3 of main square
                sq.add(r)
        

        sq2 = VGroup()
        for i in range(-4, 5):  # -1, 0, 1    9
            for j in range(-4, 5):  # -1, 0, 1
                r = Square(
                    side_length=length/27,  # For Sierpinski carpet pattern
                    fill_color=BLACK, 
                    fill_opacity=1, 
                    stroke_width=0
                ).move_to([i * length/9, j * length/9, 0])  # Spacing is 1/3 of main square
                sq2.add(r)

        

        sq3 = VGroup()
        for i in range(-13, 14):  # -1, 0, 1    27
            for j in range(-13, 14):  # -1, 0, 1
                r = Square(
                    side_length=length/81,  # For Sierpinski carpet pattern
                    fill_color=BLACK, 
                    fill_opacity=1, 
                    stroke_width=0
                ).move_to([i * length/27, j * length/27, 0])  # Spacing is 1/3 of main square
                sq3.add(r)

        
        sqq = VGroup(s,r1,sq,sq2,sq3).move_to(o2.get_center())


        
        sp(c(dots), n.animate.set_value(10000), fi(sqq, lag_ratio=0.5),run_time=8) #33

        self.clear()
        dots.move_to(ORIGIN)
        s5 = SurroundingRectangle(dots)

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

        s1 = random_noise_in_square(10000)
        s2 = VGroup(*[Dot().scale(0.2).move_to(p) for p in s1])
        sw(2)
        sa(s2)
        sp(ReplacementTransform(s2, dots))
        t5 = Text("Theoretically imperfect but Beautiful").next_to(dots, DOWN)
        sp(w(t5)) #38
        g1 = VGroup()
        g2 = VGroup()
        g3 = VGroup()
        g4 = VGroup()
        g5 = VGroup(g1,g2,g3,g4)
        
        sw(3)
        sw(16)
        for i in range(10):
            g1.add(create_glow(dots[i*5], color=GREEN))
        for i in range(10):
            g2.add(create_glow(dots[i*5+1]))
        for i in range(10):
            g3.add(create_glow(dots[i*5+2], color=RED))

        for i in range(10):
            g4.add(create_glow(dots[i*5+3],color=WHITE))

        for i in g5:
            sp(c(i))
            


        sw(20)

class s5_redo(Scene):
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

        t1 = Text("Wait...")
        t2 = Text("Wait...").next_to(t1)
        t3 = Text("Wait...").next_to(t2)

        g1 = VGroup(t1,t2,t3).move_to(ORIGIN)
        sw(1.5)
        for i in g1:
            sa(i)
            sw(0.3)

        #2.5
        
        t4 = Text("Randomness is Essential")
        t5 = Text("?").next_to(t4)
        t6 = Text("Yes, ").next_to(t4, LEFT)
        
        sw(3)
        sp(Uncreate(g1, lag_ratio=0.5), Write(t4)) #6.5
        sp(fi(t5))
        sw(11.5)
        sp(fo(t5), fi(t6), run_time=2) #19
        
        for i in range(12, len(t4)):
            t4[i].set_color(YELLOW)
            sw(0.1)
        #23
        sw(10)
        self.clear()

        s = Square(stroke_color=TEAL, stroke_width=1).scale(1.5).scale(1.5)
        la1 = Text("A").next_to(s.get_corner(DL), DOWN*0.1 + LEFT*0.1).scale(0.3)
        lb1 = Text("B").next_to(s.get_corner(DR), DOWN*0.1 + RIGHT*0.1).scale(0.3)
        lc1 = Text("C").next_to(s.get_corner(UR), UP*0.1 + RIGHT*0.1).scale(0.3)
        ld1 = Text("D").next_to(s.get_corner(UL), UP*0.1 + LEFT*0.1).scale(0.3)
        le1 = Text("E").next_to(s.get_edge_center(DOWN), DOWN*0.1).scale(0.3)
        lf1 = Text("F").next_to(s.get_edge_center(RIGHT), RIGHT*0.1).scale(0.3)
        lg1 = Text("G").next_to(s.get_edge_center(UP), UP*0.1).scale(0.3)
        lh1 = Text("H").next_to(s.get_edge_center(LEFT), LEFT*0.1).scale(0.3)

        labels1 = VGroup(la1, le1 ,lb1, lf1, lc1,lg1, ld1, lh1)
        s11 = VGroup(s, labels1)
        s11.move_to(ORIGIN)

        sp(fi(s11)) #34

        p1 = Dot().scale(0.5).move_to([-1,2,0])
        

        def twothird(init_point, target):
            return [(2*target[0]+ init_point[0])/3,
                    (2*target[1]+ init_point[1])/3,
                    0]
        corners = [s.get_corner(DL),s.get_corner(DR),s.get_corner(UR),s.get_corner(UL)]
        j = 0
        l1 = VGroup()
        sw(1)
        for i in range(20):
            if j>3:
                j = 0
            p2 = Dot().scale(0.5).move_to(twothird(p1.get_center(),corners[j]))
            p2l = Integer(i+1).scale(0.5).next_to(p2, DOWN*0.1)
            li1 = Line(p1.get_center(),corners[j], stroke_width=1, stroke_color=BLUE_D)
            sa(p2,p2l, li1)
            sw(0.2)
            l1.add(p2,p2l,li1)
            p1 = p2
            j+=1
            
        #39

        # p2 = Dot().scale(0.5).move_to(twothird(p1.get_center(), s.get_corner(DL)))
        # p3 = Dot().scale(0.5).move_to(twothird(p2.get_center(), s.get_corner(DR)))
        # p4 = Dot().scale(0.5).move_to(twothird(p3.get_center(), s.get_corner(UR)))
        # p5 = Dot().scale(0.5).move_to(twothird(p4.get_center(), s.get_corner(UL)))
        # p6 = Dot().scale(0.5).move_to(twothird(p5.get_center(), s.get_corner(DL)))
        # p7 = Dot().scale(0.5).move_to(twothird(p6.get_center(), s.get_corner(DR)))
        # p8 = Dot().scale(0.5).move_to(twothird(p7.get_center(), s.get_corner(UR)))
        # p9 = Dot().scale(0.5).move_to(twothird(p8.get_center(), s.get_corner(UL)))
        # g2 = VGroup(p1,p2,p3,p4,p5,p6,p7,p8,p9)
        sw(20+5)
        self.clear()

        t7 = mt(r"\infty Perimeter !?").to_corner(UL)
        t8 = mt(r"Area = 0 ?").next_to(t7, DOWN)
        t9 = mt(r"\text{Fractional Dimensions !!? (1.89D instead of 2D)}").next_to(t8, DOWN).shift(RIGHT*4)
        g2 = VGroup(t7,t8,t9)

        o1 = ImageMobject("cantor3d").to_edge(LEFT).scale(0.6)
        o2 = ImageMobject("mandel").scale(0.12)

        sp(w(g2)) #1.05
        sp(fi(o1), fi(o2))
        

        sw(10)

        self.clear()

        t1 = Text("Math is Interesting if you \nare curious")
        t2 = Text(":)").next_to(t1, buff=1).scale(1.3)
        t2.rotate(-PI/2, about_point=t2.get_center())
        t3 = Text(";)").next_to(t1, buff=1).scale(1.3)
        t3.rotate(-PI/2, about_point=t3.get_center())

        g1 = VGroup(t1,t2,t3).move_to(ORIGIN)

        sp(w(t1)) #1.17
        sa(t2)
        sw(1)
        sr(t2)
        sa(t3)
        sw(0.3)
        sa(t2)
        sr(t3)
        sw(6)
        t5 = Text("Thank You...")

        sp(Unwrite(t1), fo(t2)) #1.24

        sp(fi(t5), run_time=3)
        sw(2)
        sp(fo(t5))



        sw(1)
