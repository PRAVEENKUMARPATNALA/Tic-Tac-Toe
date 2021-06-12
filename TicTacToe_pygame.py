import pygame as pg
from itertools import combinations
import sys

pg.init()
clock=pg.time.Clock()
screen_size=(800,400)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption("Praveen's Tic Tac Toe")
icon = pg.image.load('game_icon.png')
pg.display.set_icon(icon)
font=pg.font.SysFont('timesnewroman',40)
text_font=pg.font.SysFont('timesnewroman',20)
input_rect=pg.Rect(15,350,140,32)

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
machine_pos=[0,0]
word=""

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

def draw_background():
    screen.fill(pg.Color("lightblue"))
    pg.draw.rect(screen, pg.Color("black"),pg.Rect(15,15,270,270),5)
    i=1
    while((i*90)<270):
        line_width=5
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(i * 90 + 15, 15), pg.Vector2(i * 90 + 15, 285), line_width)
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, i * 90 + 15), pg.Vector2(285, i * 90 + 15), line_width)
        i+=1

def draw_numbers():
    for i in range(3):
        output=l[i]
        n_text=font.render(str(output),True,pg.Color('black'))
        screen.blit(n_text,pg.Vector2(i*90+47,42))
    k=0
    for i in range(3,6,1):
        output=l[i]
        n_text=font.render(str(output),True,pg.Color('black'))
        screen.blit(n_text,pg.Vector2(k*90+47,1*90+42))
        k+=1
    k=0
    for i in range(6,9,1):
        output=l[i]
        n_text=font.render(str(output),True,pg.Color('black'))
        screen.blit(n_text,pg.Vector2(k*90+47,2*90+42))
        k+=1

def inpt(show_text):
    word=""
    n_text = text_font.render(show_text, True, pg.Color('black'))
    screen.blit(n_text, pg.Vector2(15, 310))
    pg.draw.rect(screen, pg.Color("darkgreen"), input_rect, 2)
    pg.display.flip()
    done = True
    while done:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    done=False
                elif event.key == pg.K_BACKSPACE:
                    text_surface = text_font.render(word, True, pg.Color("lightblue"))
                    screen.blit(text_surface, pg.Vector2(20, 352))
                    word = word[:-1]
                else:
                    word+=event.unicode
            text_surface = text_font.render(word, True, pg.Color("black"))
            screen.blit(text_surface, pg.Vector2(20, 352))
            pg.display.flip()
    return word

def show(show_text):
    n_text = text_font.render(show_text, True, pg.Color('black'))
    screen.blit(n_text, pg.Vector2(15, 310))
    pg.display.flip()

### This function run as a loop until the game completes
def game_loop(previous_generate):
    global total_moves,human,flag,machine_pos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    if(previous_generate==False):
        machine_pos = generate_move()
        l[machine_pos[0]] = "M"
        s[machine_pos[0]] = True
        machine_moves.append(machine_pos[0])
        if (machine_pos[1] == 1):
            return "Machine Won The Game, Thanks For Playing :)"
        total_moves += 1
    draw_background()
    draw_numbers()
    while(1):
        word=inpt("Machine took the position of '{0}' Its Human Turn, Enter Your Position From Empty Slots:".format(machine_pos[0]+1))
        if(word.isdigit()==False):
            text_surface = text_font.render(word, True, pg.Color("lightblue"))
            screen.blit(text_surface, pg.Vector2(20, 352))
            return True
        human_pos = int(word) - 1
        if(human_pos in human_moves or human_pos in machine_moves or human_pos<0 or human_pos>8):
            text_surface = text_font.render(word, True, pg.Color("lightblue"))
            screen.blit(text_surface, pg.Vector2(20, 352))
            return True
        else:
            break
    l[human_pos] = "H"
    s[human_pos] = True
    human_moves.append(human_pos)
    human += 1
    if (human >= 3):
        comb = combinations(human_moves, 3)
        for i in list(comb):
            if (magic_square[i[0]] + magic_square[i[1]] + magic_square[i[2]] == 15):
                return "Hurray!!! You Won The Game :)"
    total_moves += 1
    if (total_moves >= 9):
        return "It's a Tie...Thanks For Your Efforts"
    pg.display.flip()
    clock.tick(1000)
    return False


### The execution of file starts from here
word1=""
while(word1.lower()!="yes" and word1.lower()!="no"):
    draw_background()
    draw_numbers()
    word1=inpt("If you want to start the game, enter 'yes' else enter 'no'")
    text_surface = text_font.render(word1, True, pg.Color("black"))
    screen.blit(text_surface, pg.Vector2(20, 352))
    input_rect.w = max(100, text_surface.get_width() + 10)
    screen.fill("lightblue")


while(1):
    if(word1.lower()=="yes"):
        draw_background()
        draw_numbers()
        word=inpt("Enter your position to start")
        text_surface = text_font.render(word, True, pg.Color("black"))
        screen.blit(text_surface, pg.Vector2(20, 352))
        input_rect.w = max(100, text_surface.get_width() + 10)
        if(word.isdigit()==False):
            continue
        human_pos = int(word) - 1
        if(human_pos<0 or human_pos>8):
            continue
        l[human_pos] = "H"
        s[human_pos] = True
        human_moves.append(human_pos)
        pg.display.flip()
        human += 1
        total_moves+=1
        break
    elif(word1.lower()=="no"):
        break

previous_generate=False
while(total_moves<9):
    win=game_loop(previous_generate)
    if(win==False or win==True):
        previous_generate=win
    elif(win!=None):
        draw_background()
        draw_numbers()
        show(win)
        break
else:
    draw_background()
    draw_numbers()
    show("It's a Tie...Thanks For Your Efforts")
done = True
while (done):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()