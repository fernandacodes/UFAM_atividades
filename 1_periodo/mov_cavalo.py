def possivel(x1,y1,x2,y2):
    def mov1(x1,y1,x2,y2):
        return y2 == y1+2 and x2 == x1 + 1
    def mov2(x1,y1,x2,y2):
        return y2 == y1+2  and x2 == x1 - 1
    def mov3(x1,y1,x2,y2):
        return y2 == y1-1 and x2 == x1 - 2
    def mov4(x1,y1,x2,y2):
        return y2 == y1-1 and x2 == x1 + 2
    def mov5(x1,y1,x2,y2):
        return y2 == y1-2 and x2 == x1 - 1
    def mov6(x1,y1,x2,y2):
        return y2 == y1-2 and x2 == x1 + 1
    def mov7(x1,y1,x2,y2):
        return y2 == y1+1 and x2 == x1 + 2
    def mov8(x1,y1,x2,y2):
        return y2 == y1+1 and x2 == x1 - 2
    if x1 < 8 and x2 < 8 and y1 < 8 and y2 < 8 and x1 >= 0 and x2 >= 0 and y2 >= 0:
        return mov1(x1,y1,x2,y2) or mov2(x1,y1,x2,y2) or mov3(x1,y1,x2,y2) or mov4(x1,y1,x2,y2) or mov5(x1,y1,x2,y2) or mov6(x1,y1,x2,y2) or mov7(x1,y1,x2,y2) or mov8(x1,y1,x2,y2)


#possivel(4,5,6,1)
#False
#possivel(3,3,2,1)
#True