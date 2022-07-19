from levels import levels
from playground import window, canvas, walls, keys, doors, exits, players, createLevel, lavas
currentLevel = 0
createLevel(levels[currentLevel])

def playerMove(event):
    global currentLevel
    player = players[0]
    key = event.keysym
    x = 0
    y = 0
    if key == 'Up':
        y -= 5
    if key == 'Down':
        y += 5
    if key == 'Right':
        x += 5
    if key == 'Left':
        x -= 5
    canvas.move(player,x,y)
    for wall in walls:
        x1,y1,x2,y2 = canvas.coords(wall)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.move(player,-x,-y)
    for key in keys:
        x1,y1,x2,y2 = canvas.coords(key)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            canvas.delete(key)
            keys.remove(key)
    for door in doors:
        if len(keys) == 0:
            canvas.itemconfig(door, fill='green', outline='green')
        x1,y1,x2,y2 = canvas.coords(door)
        if player in canvas.find_overlapping(x1,y1,x2,y2):
            if canvas.itemcget(door, 'fill') == 'red':
                canvas.move(player, -x, -y)
    for exit in exits:
        x1, y1, x2, y2 = canvas.coords(exit)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete("all")
            currentLevel += 1
            if currentLevel < len(levels):
                createLevel(levels[currentLevel])
            else:
                canvas.delete('all')
                canvas.create_text(225, 225, text='You Won The Game',fill='green',width=300,font='Alkaline 20')
                canvas.unbind_all('<Key>')
                return
    for lava in lavas:
        x1, y1, x2, y2 = canvas.coords(lava)
        if player in canvas.find_overlapping(x1, y1, x2, y2):
            canvas.delete('all')
            createLevel(levels[currentLevel])

canvas.bind_all('<Key>', playerMove)

window.mainloop()