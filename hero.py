class Hero:
    def __init__(S, pos, land):
        S.land = land
        S.hero = loader.loadModel('smiley')
        S.hero.setColor((0.96,0.79,0.9, 1))
        S.hero.setPos(pos)
        S.hero.setScale(0.3)
        S.hero.reparentTo(render)
        S.hero.setH(180)
        S.hero.setP(20)
        S.mode = True
        S.cameraUp()
        # S.cameraBind()
        S.accept_events()
       
    
    def cameraBind(S):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(S.hero)
        base.camera.setPos(0, 0, 1.5)
        S.cameraOn = True

    def cameraUp(S):
        pos = S.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        S.cameraOn = False

    def accept_events(S):
        base.accept('n', S.turn_left)
        base.accept('n'+'-repeat', S.turn_left)
        base.accept('b', S.turn_right)
        base.accept('b'+'-repeat', S.turn_right)
        base.accept('d', S.changeView)
        base.accept('w', S.forward)
        base.accept('w'+ '-repeat', S.forward)
        base.accept('s', S.back)
        base.accept('s'+ '-repeat', S.back)
        base.accept('a', S.left)
        base.accept('a'+ '-repeat', S.left)
        base.accept('e', S.right)
        base.accept('e' + '-repeat', S.right)
        base.accept('q', S.move_up)
        base.accept('q' + '-repeat', S.move_up)
        base.accept('z', S.move_down)
        base.accept('z' + '-repeat', S.move_down)
        base.accept('m', S.changeMode)
        base.accept('1', lambda :S.build(1))
        base.accept('2', lambda :S.build(2))
        base.accept('3', lambda :S.build(3))
        base.accept('4', lambda :S.build(4))
        base.accept('p', S.land.saveMap)
        base.accept('o', S.land.loadMap)




        



        

    def changeView(S):
        if S.cameraOn:
            S.cameraUp()
        else:
            S.cameraBind()

    def changeMode(S):
        S.mode = not S.mode
        # print(S.mode)

    def turn_left(S):
        S.hero.setH((S.hero.getH()+5)%360)

    def turn_right(S):
        S.hero.setH((S.hero.getH()-5)%360)

    def move_to(S, angle):
        # print(angle)
        if S.mode:
            S.just_move(angle)
        else:
            S.try_move(angle)
            print('try_move')

   

    def try_move(S, angle):
        pos = S.look_at(angle)
        if S.land.isEmpty(pos):
            pos = S.land.findHighestEmpty(pos)
            S.hero.setPos(pos)
        else:
            pos = pos[0], pos[1], pos[2]+1
            if S.land.isEmpty(pos) :
                S.hero.setPos(pos)

    def build(S, ty):
        angle =S.hero.getH()% 360
        pos = S.look_at(angle)
        if S.mode:
            S.land.addBlock(pos, ty)
        else:
            S.buildBlock(pos, ty)

    def destroy(S):
        angle = S.hero.getH()% 360
        pos = S.look_at(angle)
        if S.mode:
            S.land.delBlock(pos)
        else:
            S.land.delBlockFrom(pos)


    def delBlock(S, pos):
        blocks = S.land.findBlocks(pos)
        for block in blocks:    
            block.destroy() 

    def buildBlock(S, pos, ty):
        x, y ,z = pos
        new = S.land.findHighestEmpty(pos)
        if new[2] <= z +1:
            S.land.addBlock(new, ty)

    def delBlockFrom(S, pos):
        x, y, z  = S.land.findHighestEmpty(pos)
        pos = x,y, z-1
        blocks = S.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def just_move(S, angle):
        pos = S.look_at(angle)
        S.hero.setPos(pos)

    def look_at(S, angle):
        from_x = round(S.hero.getX())
        from_y = round(S.hero.getY())
        from_z = round(S.hero.getZ())

        dx, dy = S.check_dir(angle)

        return from_x +dx, from_y+ dy, from_z
    
    def check_dir(S, angle):
        if angle >= 0 and angle <=20:
            return 0, -1
        elif angle >= 21 and angle <=65:
            return 1, -1
        elif angle >= 66 and angle <=110:
            return 1, 0
        elif angle >= 111 and angle <=115:
            return 1, 1
        elif angle >= 116 and angle <=200:
            return 0, 1
        elif angle >= 201 and angle <=245:
            return -1, 1
        elif angle >= 246 and angle <=290:
            return -1, 0
        elif angle >= 291 and angle <=335:
            return -1, -1
        elif angle >= 336 and angle <=360:
            return 0, 0
        
    def back(S):
        angle = (S.hero.getH()+180) %360
        S.move_to(angle)
    
    def forward(S):
        angle = S.hero.getH() %360
        S.move_to(angle)
    
    def left(S):
        angle = (S.hero.getH()+90) %360
        S.move_to(angle)
    
    def right(S):
        angle = (S.hero.getH()+270) %360
        S.move_to(angle)

    def move_up(S):
        if S.mode:
            S.hero.setZ(S.hero.getZ() +1)
        
    def move_down(S):
        if S.mode:
            S.hero.setZ(S.hero.getZ() -1)



    

        

        