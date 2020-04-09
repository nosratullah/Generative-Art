t = 0.0
def setup():
    size(500,500)
    
    
def draw():
    background(0)
    global t
    
    translate(width/2, height/2)
    strok = 0.9
    
    for i in range(30):
        #stroke(random(200,255), random(200,255), random(200,255))
        stroke(255)
        strokeWeight(strok)
        line(x1(t + i), y1(t + i), x2(t + i), y2(t + i))
        point(x1(t + i), x2(t + i))
        point(y1(t + i), y2(t + i))
        if ( i < 15 ):
            strok += 0.1
        else:
            strok -= 0.1
        
    for i in range(30):
        #stroke(random(200,255), random(200,255), random(200,255))
        stroke(255)
        strokeWeight(strok)
        #line(y1(t + i), y2(t + i), x2(t + i), x1(t + i))
        point(x2(t + i), y2(t + i))
        point(x2(t + i), y1(t + i))
        if ( i < 15 ):
            strok += 0.1
        else:
            strok -= 0.1
        
        
    t += 0.6
    
def x1(t):
    return  tan(t / 10) * 100 + sin (t/20) * 50 + random(0,1)

def y1(t):
    return cos(t / 10) * 100 + cos( t/ 15) * 20 + random(0,1)

def x2(t):
    return tan(t / 10) * 100 + sin (t/20) * 30 + random(0,1)

def y2(t):
    return sin(t / 20) * 100 + cos(t / 12) * 20 + random(0,1)
