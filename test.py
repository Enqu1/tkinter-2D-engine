import EnquX

wind = EnquX.engine()

dis = wind.display

dis.set_mode(800, 600, False, 30)

x, y = 0, 0

def input(event):
    global x,y

    if event.keysym == 'd':
        x += 1
    elif event.keysym == 'a':
        x -= 1
    if event.keysym == 's':
        y += 1
    elif event.keysym == 'w':
        y -= 1

def updateDisplay():
    dis.fill("#2ecc71")

    rect = wind.rect.Rect(x, y, 2, 2, colorRGB=(255, 255, 0))
    dis.drawRect(rect)

    dis.update()

def mainLoop():
    while dis.running:
        for event in wind.events.get():
            if event.type == "2":
                input(event)

        updateDisplay()

if __name__ == '__main__':
    mainLoop()