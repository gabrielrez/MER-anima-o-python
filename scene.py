from manim import *

class Scene(Scene):
    def construct(self):
        # Titulo
        title = Text('Modelo Entidade Relacionamento', color='#ffffff').scale(1.20)
        name = Text('Gabriel Rezende | Sistema De Informação', color='#ffffff').scale(0.8)

        title.shift(UP * 0.5)
        name.shift(DOWN * 0.5)

        self.play(Write(title))
        self.wait()
        self.play(FadeIn(name))
        self.pause(15)
        self.play(FadeOut(title), FadeOut(name))

        # Explicação
        self.pause(1.5)
        explanation1 = Text('Modelo de entidade e relacionamento é uma', line_spacing=1.8).scale(0.8)
        explanation2 = Text('maneira de desenhar e mostrar como diferentes coisas', line_spacing=1.8).scale(0.8)
        explanation3 = Text('estão conectadas em um sistema.', line_spacing=1.8).scale(0.8)
        points = Text('Indentidades - Atributos - Relacionamentos').scale(0.5)

        explanation1.shift(UP * 1)
        explanation3.shift(DOWN * 1)
        points.shift(DOWN * 2)

        self.play(Write(explanation1))
        self.wait()
        self.play(Write(explanation2))
        self.wait()
        self.play(Write(explanation3))
        self.wait()
        self.pause(3)
        self.play(Write(points))
        self.pause(10)
        self.play(FadeOut(explanation1), FadeOut(explanation2), FadeOut(explanation3), FadeOut(points))
        self.pause(2)

        # Entidades
        entity = Text('Entidade: ').scale(0.8)
        entity_text = Text('Coisas ou objetos sobre os quais você quer armazenar informações.').scale(0.5)

        rt = Rectangle(width=entity_text.width + 0.4, height=entity_text.height + 0.4, stroke_color='#CF887C')
        entity.to_edge(UL)

        self.play(Create(entity))
        self.wait(0.5)
        self.play(Create(entity_text))
        self.pause(10)
        self.play(FadeIn(rt))
        self.pause(5)
        self.play(Uncreate(entity), Uncreate(entity_text))
        self.wait()
        self.play(FadeOut(rt))
        self.wait(2)

        # Atributos
        attribute = Text('Atributos: ').scale(0.8)
        attribute_text = Text('Características ou propriedades que descrevem uma entidade.').scale(0.5)
        
        elps = Ellipse(width=attribute_text.width*1.25, height=attribute_text.height * 2.5, stroke_color='#fffe6a')
        attribute.to_edge(UL)

        self.play(Create(attribute))
        self.wait(0.5)
        self.play(Create(attribute_text))
        self.pause(10)
        self.play(FadeIn(elps))
        self.pause(5)
        self.play(Uncreate(attribute), Uncreate(attribute_text))
        self.pause(5)
        self.play(FadeOut(elps))
        self.wait(2)

        # Relacionamento
        relationship = Text('Relacionamento: ').scale(0.8)
        relationship_text = Text('As conexões entre diferentes entidades.').scale(0.5)

        relationship.to_edge(UL)
        vertices = [
            LEFT * 6,
            UP * 1.2,
            RIGHT * 6,
            DOWN * 1.2,
        ]

        lsgl = Polygon(*vertices, stroke_color='#A2BC92')

        self.play(Create(relationship))
        self.wait(0.5)
        self.play(Create(relationship_text))
        self.pause(10)
        self.play(FadeIn(lsgl))
        self.pause(5)
        self.play(Uncreate(relationship), Uncreate(relationship_text))
        self.wait(2)
        self.play(FadeOut(lsgl))
        self.wait(2)

        #Exemplom simples
        entity1_text = Text('Cliente').scale(0.5)
        rt_entity1 = Rectangle(width=2.5, height=1, stroke_color='#CF887C')
        rt_entity1.to_edge(LEFT * 2)
        entity1_text.next_to(rt_entity1.get_center(), aligned_edge=RIGHT, buff=0)

        entity2_text = Text('Passagem').scale(0.5)
        rt_entity2 = Rectangle(width=2.5, height=1, stroke_color='#CF887C')
        rt_entity2.to_edge(RIGHT * 2)
        entity2_text.next_to(rt_entity2.get_center(), aligned_edge=RIGHT, buff=0)

        vertices_relationship = [
            LEFT * 1,
            UP * 1,
            RIGHT * 1,
            DOWN * 1,
        ]
        lsgl_relationship = Polygon(*vertices_relationship, stroke_color='#A2BC92')
        relationship_text = Text('Compra').scale(0.5)
        relationship_text.next_to(lsgl_relationship.get_center(), aligned_edge=RIGHT, buff=0)

        line1 = Line(rt_entity1.get_right(), lsgl_relationship.get_left(), color=WHITE)
        line2 = Line(rt_entity2.get_left(), lsgl_relationship.get_right(), color=WHITE)

        circle1 = Circle(radius=0.1, color=WHITE).move_to(rt_entity1.get_right())
        circle2 = Circle(radius=0.1, color=WHITE).move_to(rt_entity2.get_left())

        self.play(Create(rt_entity1), Create(entity1_text))
        self.play(Create(rt_entity2), Create(entity2_text))
        self.pause(3)
        self.play(Create(lsgl_relationship), Create(line1), Create(line2))
        self.play(Create(relationship_text), Create(circle1), Create(circle2))

        self.wait(5)

        self.play(Uncreate(rt_entity1), Uncreate(rt_entity2), Uncreate(entity1_text), Uncreate(entity2_text), Uncreate(line1), Uncreate(line2), Uncreate(relationship_text), Uncreate(lsgl_relationship), Uncreate(circle1), Uncreate(circle2))

        self.wait(5)