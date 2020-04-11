step = 30
shift = 0
def setup():
    size(1920,1200)

def draw():
    global step,shift
    background(29,29,29)
    #noFill()
    #strokeWeight(10)
    #square(100,100,800)
    for x in range(shift,width-shift,step):
        for y in range(shift,height-shift,step):
            
            if (random(1) > 0.5):
                stroke(255)
                strokeWeight(2)
                line(x, y, x + step, y + step)
            else:
                stroke(255)
                strokeWeight(2)
                line(x+step, y, x, y + step)
    
    if ( frameCount < 20):
        saveFrame('export/png_##.png')
    else:
        noLoop()
