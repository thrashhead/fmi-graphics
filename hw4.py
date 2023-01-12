def get_rectangle_line_intersections(xmin, ymin, xmax, ymax, x1, y1, x2, y2):
    p,q,t=dict(),dict(),dict()
    p[0]=-(x2-x1)
    p[1]=x2-x1
    p[2]=-(y2-y1)
    p[3]=y2-y1
    q[0]=x1-xmin
    q[1]=xmax-x1
    q[2]=y1-ymin
    q[3]=ymax-y1
    t2=1
    t1=0
    count_parallel=0
    for i in range(0,4): 
        if(p[i]>0):
            t[i]=q[i]/p[i]
            t2=min(t2,t[i])
        elif(p[i]<0):
            t[i]=q[i]/p[i]
            t1=max(t1,t[i])
        # p[i]=0 and q[i]<0
        elif(q[i] < 0):
            return False, None
        # p[i]=0 and q[i]>=0
        else:
            count_parallel+=1
    print("Line parallel to:",count_parallel,"Edges")
    if(t1==0 and t2==0):
        return -1
    if (t1<t2):
        xx1=x1+t1*p[1]
        xx2=x1+t2*p[1]
        yy1=y1+t1*p[3]
        yy2=y1+t2*p[3]
        return True, [xx1,yy1,xx2,yy2]
    else:
        return False, None