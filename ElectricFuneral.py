from manim import  *
import numpy as np
import math

class ElectricFuneral(Scene):
	def construct(self):
		#Create charges on the vertices of a square
		charge1 = Dot(point=np.array([1,1,0]), color=RED).scale(3)
		charge2 = Dot(point=np.array([-1,1,0]), color=RED).scale(3)
		charge3 = Dot(point=np.array([-1,-1,0]), color=RED).scale(3)
		charge4 = Dot(point=np.array([1,-1,0]), color=RED).scale(3)

		#Symbol for positive charges
		plus1 = MathTex("+").scale(0.7).move_to(charge1)
		plus2 = MathTex("+").scale(0.7).move_to(charge2)
		plus3 = MathTex("+").scale(0.7).move_to(charge3)
		plus4 = MathTex("+").scale(0.7).move_to(charge4)

		#Method to keep the symbol on the charge
		plus1.add_updater(
			lambda x: x.move_to(charge1.get_center())
		)
		plus2.add_updater(
			lambda x: x.move_to(charge2.get_center())
		)
		plus3.add_updater(
			lambda x: x.move_to(charge3.get_center())
		)
		plus4.add_updater(
			lambda x: x.move_to(charge4.get_center())
		)

		self.add(
			charge1, 
			charge2, 
			charge3, 
			charge4, 
		)
		self.play(
			Create(charge1, run_time=2), 
			Create(charge2, run_time=2), 
			Create(charge3, run_time=2), 
			Create(charge4, run_time=2)
		)
		self.add(
			plus1,
			plus2, 
			plus3,
			plus4,
		)

		self.play(Create(plus1), Create(plus2), Create(plus3), Create(plus4))
		self.wait()

		#Link charges with dashed lines (Polygon did not work)
		lines =[
			DashedLine(charge1, charge2, dash_length=0.1),
			DashedLine(charge2, charge3, dash_length=0.1),
			DashedLine(charge3, charge4, dash_length=0.1),
			DashedLine(charge4, charge1, dash_length=0.1),
			DashedLine(charge2, charge4, dash_length=0.1),
		]

		self.play(*[Create(line) for line in lines])

		#Label one side of the square
		label = Text("x", font_size=20)
		label.move_to([0, 1.5, 0])

		self.add(label)
		self.play(Write(label))

		#Context
		txt = Text("Potencial em cada carga do sistema: ", font_size=30)

		#Write the equation for the potencial
		formula = MathTex(
			r"U = 2 \cdot k \cdot \frac{q^2}{x} + k \cdot \frac{q^2}{x \cdot \sqrt{2}}", font_size=25
		)

		#Plot everything in the same place at the same time on the top of the screen
		group = VGroup(txt, formula).arrange(RIGHT, buff=0.5).to_edge(UP)

		self.play(
			Write(group, run_time=5),
		)
		self.play(Circumscribe(formula, time_width=1))
		self.play(*[FadeOut(line) for line in lines])
		self.play(FadeOut(label))

		#Move the charges off the screen
		self.play(
			charge1.animate.move_to([1,-10,0]),
			charge2.animate.move_to([-1,-10,0]),
			charge3.animate.move_to([-1,-10,0]),
			charge4.animate.move_to([1,-10,0]),
		)

		self.remove(charge1, charge2, charge3, charge4)

		#Move context off the screen
		self.play(RemoveTextLetterByLetter(txt), run_time=1)

		#Move formula
		self.play(formula.animate.move_to([0,formula.get_center()[1],0]), run_time=1)

		#Reducing and manipulating the expression
		eq2 = MathTex(
			r"U = \frac{k q^2}{x} \left(2 + \frac{1}{\sqrt{2}}\right)", font_size=25
		).next_to(formula, DOWN)

		self.play(TransformFromCopy(formula, eq2))
		self.wait()

		eq3 = MathTex(
			r"U = \frac{k q^2}{x} \cdot \frac{2\sqrt{2} + 1}{\sqrt{2}}", font_size=25
		).next_to(eq2, DOWN)

		self.play(TransformFromCopy(eq2, eq3))
		self.wait()

		eq4 = MathTex(
			r"U = \left(\frac{k q^2}{x}\right)(\frac{4 + \sqrt{2}}{2})", font_size=25
		).next_to(eq3, DOWN)

		self.play(TransformFromCopy(eq3, eq4))
		self.play(Indicate(eq4))
		self.wait(3)

		self.play(
			Unwrite(eq3),
			Unwrite(eq2),
			Unwrite(formula),

		)

		self.play(eq4.animate.move_to([0,formula.get_center()[1], 0]))
		self.wait(2)

		#Write the conservation of energy and figure out the expression for velocity
		kinetic = MathTex(
			r" = 4 \cdot \frac{m \cdot v^2}{2}", font_size=25
		).next_to(eq4, RIGHT)

		self.play(Create(kinetic))
		txt2 = Text(
			"(Conservação da energia mecânica)", font_size=15, color=YELLOW
		).next_to(kinetic, RIGHT)
		self.play(Write(txt2))

		eq5 = MathTex(
			r"\frac{k q^2}{2x}(4 + \sqrt{2}) = m v^2", font_size=25
		).next_to(eq4, DOWN)

		eq6 = MathTex(
			r"\frac{k q^2}{2mx}(4 + \sqrt{2}) = v^2", font_size=25
		).next_to(eq5, DOWN)

		eq7 = MathTex(
			r"v = \sqrt{\frac{k q^2}{2mx}(4 + \sqrt{2})}", font_size=25
		).next_to(eq6, DOWN)

		self.play(TransformFromCopy(eq4, eq5))
		self.wait()

		self.play(TransformFromCopy(eq5, eq6))
		self.wait()

		self.play(TransformFromCopy(eq6, eq7))
		self.play(Circumscribe(eq7, fade_out=False))

		approx = MathTex(
			r" \approx 0.49 \frac{m}{s}", font_size=25, color=BLUE
		).next_to(eq7, RIGHT)

		self.play(Write(approx))

		self.wait(3)
			
