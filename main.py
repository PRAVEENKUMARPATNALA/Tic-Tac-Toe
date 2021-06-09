from itertools import combinations

total_moves=0
l=[0,0,0,0,0,0,0,0,0]
s=[False,False,False,False,False,False,False,False,False]
magic_square=[8,3,4,1,5,9,6,7,2]
d={8:0,3:1,4:2,1:3,5:4,9:5,6:6,7:7,2:8}
human_moves=[]
machine_moves=[]
corners=[0,2,6,8]
non_corners=[1,3,5,7]
human=0
flag=0

### This function will draw the Tic Tac Toe board to ouput console
def Board():
    for i in range(len(l)):
        if(i%3==0):
            print()
        print("| {0} | ".format(l[i]),end=" ")

### This function is to generate the next machine move in the game
def generate_move():
    global flag,human

    ### Here we are checking the possibility of chances of machine winning the game
    if (human >= 2):
        for i in range(len(machine_moves)):
            for j in range(len(machine_moves)):
                if(i!=j):
                    req=15-(magic_square[machine_moves[i]]+magic_square[machine_moves[j]])
                    pos=d.get(req,-1)
                    if(pos!=-1 and s[pos]==False):
                        return (pos,1)

    ### Here we are checking the human possibilities to win to prevent him from winning the game
    for i in range(len(human_moves)):
        for j in range(len(human_moves)):
            if (i != j):
                req = 15 - (magic_square[human_moves[i]] + magic_square[human_moves[j]])
                pos = d.get(req,-1)
                if (pos!=-1 and s[pos] == False):
                    return (pos,0)

    ### Priority of machine filling the board --> center, corners followed by non-corners
    if(s[4]==False):
        return (4,0)
    for i in corners:
        if (s[i] == False):
            return (i,0)
    for i in non_corners:
        if(s[i]==False):
            return (i,0)

### The game will start from here
print("\n\nWelcome To The World Of Tic Tac Toe")
Board()

print("\n\nIf you want to start the game, enter 'Yes' else enter 'no'")
if(input()=="Yes"):
    print("\nEnter your position to start")
    human_pos = int(input()) - 1
    l[human_pos] = "H"
    s[human_pos] = True
    human_moves.append(human_pos)
    Board()
    human += 1
    machine_pos = generate_move()
    print("\n\nMachine took the position of {0}".format(machine_pos[0]+1))
    l[machine_pos[0]] = "M"
    s[machine_pos[0]] = True
    machine_moves.append(machine_pos[0])
    Board()
    total_moves += 2
else:
    machine_pos=4
    machine_moves.append(machine_pos)
    print("\n\nMachine took the position of {0}".format(machine_pos+1))
    l[machine_pos] = "M"
    s[machine_pos] = True
    total_moves+=1
    Board()

### The game will run till the board has empty slots
while(total_moves!=9):
    print("\n\nIts Human Turn, Enter Your Position From Empty Slots:")
    human_pos=int(input())-1
    l[human_pos]="H"
    s[human_pos]=True
    human_moves.append(human_pos)
    Board()
    human+=1
    if(human>=3):
        comb = combinations(human_moves, 3)
        for i in list(comb):
            if(magic_square[i[0]]+magic_square[i[1]]+magic_square[i[2]]==15):
                print("\n\nHurray!!! You Won The Game :)")
                flag=1
                break
    if(flag==1):
        break
    total_moves+=1
    if(total_moves==9):
        print("\n\n It's a Tie...Thanks For Your Efforts")
        break
    machine_pos=generate_move()
    print("\n\nMachine took the position of {0}".format(machine_pos[0]+1))
    l[machine_pos[0]] = "M"
    s[machine_pos[0]] = True
    machine_moves.append(machine_pos[0])
    Board()
    if(machine_pos[1]==1):
        print("\n\nMachine Won The Game, Thanks For Playing :)")
        break
    total_moves +=1
else:
    print("\n\n It's a Tie...Thanks For Your Efforts")



