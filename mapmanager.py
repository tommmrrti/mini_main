# напиши здесь код создания и управления картой
# from direct.showbase.ShowBase import ShowBase
import json
import pickle

class Mapmanger:
    def __init__(S):
        S.model = 'block.egg'
        S.block_types = {
            1: ('block.png',(0.1,0.10,0.29, 1) ), 
            2: ('brick.png', (0.11,0.16,0.25, 1)), 
            3: ('stone.png', (0,0.2,0.1, 1)),
            4: ('wood.png', (0.23,0.22,0.21,1))
        }
        S.startNew()
        # S.addBlock((0, 0, 0),4)

    def startNew(S):
        S.land = render.attachNewNode('Land')

    def clear(S):
        S.land.removeNode()
        S.startNew()

    def addBlock(S, pos, block_type):
        S.block = loader.loadModel(S.model)
        S.block.setTexture(loader.loadTexture(S.block_types[block_type][0]))
        S.block.setPos(pos)
        S.block.setColor(S.block_types[block_type][1])
        S.block.reparentTo(S.land)
        S.block.setTag('bl', str(pos))
        S.block.setTag('dt', str(block_type))

    def load_land(S, file_name):
        with open(file_name, 'r', encoding='UTF-8')as file:
            data = json.load(file)['data']
        z = 0
        for level in data:
            for area in level:
                x = area['x']
                y = area['y']
                blocks = area['map']
                for line in blocks:
                    for block in list(map(int, line.split(' '))):
                        S.addBlock((x, y, z), block)
                        x += 1
                    y += 1
                    x = area['x']
            z += 1
    
    def findBlocks(S, pos):
        return S.land.findAllMatches('=bl=' + str(pos))
    
    def isEmpty(S, pos):
        blocks = S.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        
    def findHighestEmpty(S, pos):
        x,y,z = pos
        z = 1
        while S.isEmpty(pos) == False:
            z = z +1
        return x, y,z

    def saveMap(S):
        blocks = S.land.getChildren()
        with open('land_save.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y,z = block.getPos()
                block_type = block.getTag('dt')
                block = ((int(x), int(y), int(z)), block_type)
                pickle.dump(block, fout)



    def loadMap(S):
        S.clear()
        with open ('land_save.dat', 'rb') as fin:
            lenght = pickle.load(fin)
            for i in range(lenght):
                block = pickle.load(fin)
                # print(block)
                S.addBlock(block[0], int(block[1]))
        

        

    
