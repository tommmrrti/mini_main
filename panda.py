from direct.showbase.ShowBase import ShowBase

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('block.egg')
        self.model.reparentTo(render)
        self.model.setScale(0.1)
        self.model.setPos(-2, 25, -3)

        self.model1 = loader.loadModel('Boeing707.egg')
        self.model1.reparentTo(render)
        self.model1.setScale(0.6)
        self.model1.setPos(-3, 50, -2)

        self.model2 = loader.loadModel('Fighter.egg')
        self.model2.reparentTo(render)
        self.model2.setScale(0.1)
        self.model2.setPos(-10, 50, -20)

        self.model2 = loader.loadModel('Sailboat.egg')
        self.model2.reparentTo(render)
        self.model2.setScale(0.5)
        self.model2.setPos(-10, 50, -20)


        
        base.camLens.setFov(90)


game = Game()
game.run()
