from graphics import *
from random import *

"""
create_snp_heatmap will display a window heat map of data,
The maximum size for a map is 500 pixels wide, but given less than 500 data
points the window will scale down.
To view the labels click on any point.
When window is open any code after will not run until you close the window
"""

def create_snp_heatmap(snp_vector,labels):
    #create scale
    sort=sorted(snp_vector);
    maxValue=sort[-1]
    minValue=sort[0]
    scale=maxValue-minValue
    colorIncrement=(255*2)/scale
    toLabel=list()
    #window creation
    width=min(500,len(snp_vector))
    indent=int(width/25*3)
    height=width/5
    window = GraphWin('heat map',width+2*indent,height+height/3)
    
    clump=len(snp_vector)/width
    
    i=0
    while i<len(snp_vector):
        color=snp_vector[i]-minValue
        j=1
        i+=1
        while i%int(clump)!=0 and i<len(snp_vector):
            color+=snp_vector[i]-minValue
            i+=1
            j+=1
        color=color*colorIncrement/j #average value for a clump scaled to color range
        #set color
        r=min(color,255)
        g=255
        b=0
        color-=255
        if color>0:
            g=255-min(color,255)
            color-=255
        #draw line
        line=Line(Point(indent+i/clump,0),Point(indent+i/clump,height))
        lineColor=color_rgb(int(r),int(g),int(b))
        line.setOutline(lineColor)
        line.draw(window)
    while window.isOpen():
        #erase with rectangle
        rect=Rectangle(Point(0,height+1),Point(width+2*indent,height+height/3))
        rect.setFill('white')
        rect.setOutline('white')        
        x=window.checkMouse()
        if x is not None:
            x=x.getX();
            if x>indent and x<width+indent:
                x-=indent
                rect.draw(window)
                if len(snp_vector)<1000:
                    t=labels[int(x)]
                else:
                    t='['+str(labels[int(x*clump-clump)])+'-'+str(labels[int(x*clump)])+']'
                label=Text(Point(x+indent,int(height+width/40)),t)
                label.setSize(int(width/25))
                label.draw(window)        
            
            
 
