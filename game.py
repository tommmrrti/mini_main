# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanger
from hero import Hero

class Game(ShowBase):
    def __init__(S):
        ShowBase.__init__(S)
        S.land = Mapmanger()
        S.land.load_land('level_01.json')
        base.camLens.setFov(90)
        S.hero = Hero((0, 0, 5), S.land)

game = Game()
game.run()