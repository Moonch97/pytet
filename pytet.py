#20171488 문채원
from matrix import *
import random

def draw_matrix(m):
    array = m.get_array() #2차원배열을 뽑아서 array로 저장
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###    
block1 = [[ 1, 1 ],      #원래 도형
          [ 1, 1 ]]

block2 = [
         [[ 0, 1, 1 ],
          [ 1, 1, 0 ],
          [ 0, 0, 0 ]], # 원래 도형

         [[ 0, 0, 1 ],
          [ 0, 1, 1 ],
          [ 0, 1, 0 ]], # 90도 회전

         [[ 0, 0, 0 ],
          [ 1, 1, 0 ],
          [ 0, 1, 1 ]], #180도 회전

         [[ 1, 0, 0 ],
          [ 1, 1, 0 ],
          [ 0, 1, 0 ]]] #270도 회전
        

block3 = [
         [[ 0, 0, 1 ],
          [ 0, 1, 1 ],
          [ 0, 1, 0 ]],  #원래 도형

         [[ 1, 1, 0 ],
          [ 0, 1, 1 ],
          [ 0, 0, 0 ]], #90도 회전

         [[ 0, 1, 0 ],
          [ 1, 1, 0 ],
          [ 1, 0, 0 ]], #180도 회전

         [[ 1, 1, 0 ],
          [ 0, 1, 1 ],
          [ 0, 0, 0 ]]] #270도 회전

block4 = [
         [[ 1, 0, 0 ],
          [ 1, 1, 1 ],
          [ 0, 0, 0 ]], #원래 도형
        
         [[ 0, 1, 1 ],
          [ 0, 1, 0 ],
          [ 0, 1, 0 ]], #90도 회전

         [[ 1, 1, 1 ],
          [ 0, 0, 1 ],
          [ 0, 0, 0 ]], #180도 회전

         [[ 0, 1, 0 ],
          [ 0, 1, 0 ],
          [ 1, 1, 0 ]]] #270도 회전



block5 = [
         [[ 0, 0, 1 ],
          [ 1, 1, 1 ],
          [ 0, 0, 0 ]], #원래 도형

         [[ 0, 1, 0 ],
          [ 0, 1, 0 ],
          [ 0, 1, 1 ]], #90도 회전
        
         [[ 1, 1, 1 ],
          [ 1, 0, 0 ],
          [ 0, 0, 0 ]], #180도 회전
         
         [[ 1, 1, 0 ],
          [ 0, 1, 0 ],
          [ 0, 1, 0 ]]] #270도 회전

block6 = [
         [[ 0, 1, 0 ],
          [ 1, 1, 1 ],
          [ 0, 0, 0 ]], #원래 도형

         [[ 0, 1, 0 ],
          [ 0, 1, 1 ],
          [ 0, 1, 0 ]], #90도 회전

         [[ 1, 1, 1 ],
          [ 0, 1, 0 ],
          [ 0, 0, 0 ]], #180도 회전

         [[ 0, 1, 0 ],
          [ 1, 1, 0 ],
          [ 0, 1, 0 ]]] #270도 회전

block7 = [
    [[ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ]], ## 원래 도형

    [[ 1, 1, 1, 1 ],
     [ 0, 0, 0, 0 ],
     [ 0, 0, 0, 0 ],
     [ 0, 0, 0, 0 ]], ## 90도 회전


    [[ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ],
     [ 0, 0, 1, 0 ]], ## 180도 회전


    [[ 1, 1, 1, 1 ],
     [ 0, 0, 0, 0 ],
     [ 0, 0, 0, 0 ],
     [ 0, 0, 0, 0 ]]] ## 270도 회전
N = 0
ran_num = random.randrange(1,8)
arrayBlk = [N][N]

if ran_num == 1:
    arrayBlk = block1

elif ran_num == 2:
    arrayBlk = block2[N]

elif ran_num == 3:
    arrayBlk = block3[N]

elif ran_num == 4:
    arrayBlk = block4[N]

elif ran_num == 5:
    arrayBlk = block5[N]

elif ran_num == 6:
    arrayBlk = block6[N]

elif ran_num == 7:
    arrayBlk = block7[N]





### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen) # 입력스크린
oScreen = Matrix(iScreen) # 출력 스크린
currBlk = Matrix(arrayBlk) # 화면에 등장하는 블록 (인자: 2차원배열로 줌)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx()) #clip (좌측상단좌표(top, left), 우측하단좌표
tempBlk = tempBlk + currBlk #16개원소를 각자 더함
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        N = (N + 1) % 4
        if ran_num == 1:
            arrayBlk = block1

        elif ran_num == 2:
            arrayBlk = block2[N]

        elif ran_num == 3:
            arrayBlk = block3[N]

        elif ran_num == 4:
            arrayBlk = block4[N]

        elif ran_num == 5:
            arrayBlk = block5[N]

        elif ran_num == 6:
            arrayBlk = block6[N]

        elif ran_num == 7:
            arrayBlk = block7[N]

    elif key == ' ': # drop the block
        for i in range(14):
            if tempBlk.anyGreaterThan(1):
                if key == ' ':
                    break
            top += 1    



    else:
        print('Wrong key!!!')
        continue
    currBlk = Matrix(arrayBlk) # 화면에 등장하는 블록 (인자: 2차원배열로 줌)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk

    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            N = N - 1
            if N < 0:
                N = 3
            if ran_num == 1:
                arrayBlk = block1

            elif ran_num == 2:
                arrayBlk = block2[N]

            elif ran_num == 3:
                arrayBlk = block3[N]

            elif ran_num == 4:
                arrayBlk = block4[N]

            elif ran_num == 5:
                arrayBlk = block5[N]

            elif ran_num == 6:
                arrayBlk = block6[N]

            elif ran_num == 7:
                arrayBlk = block7[N]
        elif key == ' ': # undo: move up
            top -= 1
            newBlockNeeded = True

        currBlk = Matrix(arrayBlk) # 화면에 등장하는 블록 (인자: 2차원배열로 줌)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
