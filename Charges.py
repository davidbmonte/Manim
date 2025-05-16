from manim import *
import numpy as np

class CampoEletricoDinamico(Scene):
    def construct(self):
        # Cria a carga positiva móvel
        carga_positiva = Dot(point=np.array([1, 0, 0]), color=RED).scale(1.5)
        sinal_positivo = MathTex("+").scale(1.2).move_to(carga_positiva)
        sinal_positivo.add_updater(lambda m: m.move_to(carga_positiva.get_center()))

        # Cargas negativas fixas
        carga_neg1 = Dot(point=np.array([-0.5, 0.75, 0]), color=BLUE).scale(1.2)
        carga_neg2 = Dot(point=np.array([-0.5, -0.75, 0]), color=BLUE).scale(1.2)
        sinal_neg1 = MathTex("-").scale(1.2).move_to(carga_neg1)
        sinal_neg2 = MathTex("-").scale(1.2).move_to(carga_neg2)

        self.add(carga_positiva, carga_neg1, carga_neg2, sinal_positivo, sinal_neg1, sinal_neg2)

        # Campo elétrico calculado em tempo real
        def campo_eletrico(x, y):
            cargas = [
                (carga_positiva.get_center(), +1),
                (carga_neg1.get_center(), -1),
                (carga_neg2.get_center(), -1),
            ]
            ponto = np.array([x, y, 0])
            E = np.zeros(3)
            for pos, q in cargas:
                r = ponto - pos
                norm = np.linalg.norm(r)
                if norm < 0.15:
                    continue
                E += q * r / norm**3
            return E

        escala = 0.2

        # Campo vetorial com vetores curtos e denso
        vetor_campo = always_redraw(lambda: ArrowVectorField(
            lambda p: escala * campo_eletrico(p[0], p[1]),
            x_range=[-4, 4, 0.25],
            y_range=[-3, 3, 0.25],
            colors=[BLUE, GREEN, YELLOW, RED],
            opacity=0.6,
        ))

        # Linhas de fluxo do campo elétrico
        linhas = always_redraw(lambda: StreamLines(
            lambda p: campo_eletrico(p[0], p[1]),
            x_range=[-4, 4],
            y_range=[-3, 3],
            stroke_width=1.5,
            max_anchors_per_line=30,
            padding=0.5,
            colors=[BLUE, GREEN, YELLOW, RED],
        ))

        self.add(vetor_campo, linhas)
        self.play(FadeIn(linhas))
        self.wait(0.5)

        linhas.start_animation(warm_up=False, flow_speed=0.5)

        # Move a carga para a direita e depois volta
        self.play(carga_positiva.animate.shift(RIGHT * 2), run_time=3)
        self.wait(0.5)
        self.play(carga_positiva.animate.shift(LEFT * 2), run_time=3)
        self.wait(3)
