from os import linesep
import cv2
import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
#from svg.path import parse_path
from svgpathtools import *
from xml.dom import minidom
import math
import websockets
import asyncio
import lensdistort
import distortionfix
import glob


################################WARNING -------- ONLY JPG FILES WHEN THIS CODE IS RUNNING SHOULD BE THE ONES OF YOUR CHESSBOARD EMPTY AND FILLED , CODE WILL TRY TO SCAN EVERYTHING THATS JPG TO GET A BETTER ESTIMATION
async def listener(string):
    url = "ws://25.52.61.231:49152"
    async with websockets.connect(url) as ws:
        print("Connected")
            
        msg = string
        await ws.send(msg)
        print(msg)
        



def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    #print("current ang",ang)
    return ang + 360 if ang < 0 else ang

def dotfinder(file0,file1,heig,leng,offx,offy,percube):
    
    if file0==-15:  
        fl0="distort"
    else:
        fl0=file0

        
    if file1==-15:  
        fl1="distort1"
    else:
        fl1=file1
        
    percube=(int)(percube)
    if percube==-15:  
        perbox=70
    else:
        perbox=percube

    heig=(int)(heig)
    if heig==-15:  
        areaheight=15*perbox
        heig=16
    else:
        areaheight=(heig-2)*perbox
        heig=heig-1
        
    leng=(int)(leng)        
    if leng==-15:  
        arealength=13*perbox
        leng=14
    else:
        arealength=(leng-2)*perbox
        leng=leng-1
        
    offx=(int)(offx)           
    if offx==-15:  
        offsetXincubes=3
    else:
        offsetXincubes=offx
            
    offy=(int)(offy)          
    if offy==-15:  
        offsetYincubes=1
    else:
        offsetYincubes=offy

        
    distortionfix.fixer(fl0,fl1)

    print(heig,leng)
    lensdistort.fixshape(heig,leng)
    # Read image.
    img = cv2.imread('caliResultFinal1.png', cv2.IMREAD_COLOR)
    #img=cv2.flip(img,0)
    nimg = cv2.imread('caliResultFinal1.png', cv2.IMREAD_UNCHANGED)
    #nimg=cv2.flip(nimg,0)
    # Convert to grayscale.
    gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #TEST REC START
    ret,thresh = cv2.threshold(gray1,127,255,1) 
     
    contours,h = cv2.findContours(thresh,1,2) 
     
    for cnt in contours: 
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) 
        #print (len(approx)) 
        if len(approx)==4:
            x=0
            #print ("square" )
            #cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    #REC END 

    cv2.imshow('img',img) 

    #cv2.destroyAllWindows()


    gray= cv2.Canny(img,75,100)
    #cv2.imshow('imgur',gray)

    #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    ##cv2.imshow("DetCircle", gray)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (5, 5))
    #cv2.imshow("DCircle", gray_blurred)
      
    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray, 
                       cv2.HOUGH_GRADIENT, 1, 20, param1 = 30,
                   param2 = 18, minRadius = 7, maxRadius = 15)
    #cv2.imshow("Detected Circle", img)
    #print("Amount detected",len(detected_circles[0]))
    # Draw circles that are detected.
    akeep=0
    bkeep=0
    i=0
    arrkeep=[]
    if detected_circles is not None:
      
        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))
        ct=0
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            x=[a,b]
            arrkeep.append(x)
            # Draw the circumference of the circle.
            cv2.circle(img, (a, b), r, (0, 60*ct, 0), 2)
            cv2.putText(img,(str)(r),(a,b),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            ct+=1
            #if i!=0:
                #cv2.line(img,(akeep,bkeep),(a,b),(255,0,0),5)
            i+=1
            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(img, (a, b), 10, (0, 0, 255), 3)
            akeep=a
            bkeep=b

            cv2.waitKey(0)
    """
    cv2.imshow("Detected Circle", img)
    # Read image.
    drawing = svg2rlg("B_ornek-01.svg")
    paths, attributes = svg2paths('B_ornek-02.svg')
    renderPDF.drawToFile(drawing, "file.pdf")
    renderPM.drawToFile(drawing, "file.jpg", fmt="JPG")
    imgsvg = cv2.imread('file.jpg', cv2.IMREAD_COLOR)


    a=1
    #imgsvg=cv2.flip(imgsvg,0)

    #imgsvg=cv2.flip(imgsvg,1)

      
    # Convert to grayscale.
    gray1 = cv2.cvtColor(imgsvg, cv2.COLOR_BGR2GRAY)

    #TEST REC START
    ret,thresh = cv2.threshold(gray1,127,255,1) 
     
    contours,h = cv2.findContours(thresh,1,2) 
     
    for cnt in contours: 
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True) 
        #print (len(approx)) 
        if len(approx)==4: 
            #print ("square" )
            cv2.drawContours(imgsvg,[cnt],0,(0,0,255),-1)
    #REC END 

    cv2.imshow('imgsvg',imgsvg) 



    #arrtr=[[199,370],[135,294],[15,258],[50,165],[135,126],[192,126],[199,144],[247,126],[279,147],[311,212],[355,193],[418,188],[448,254],[448,309],[382,348],[465,346],[496,382],[512,393],[564,408],[573,438],[542,466],[486,437],[438,490],[373,495],[337,539],[298,579],[195,607],[114,612],[73,513],[89,446],[75,404],[54,341],[95,309],[147,317],[199,370]]
    arrtr=[]
    for i in range(len(paths[0])):
        x=str(paths[0][i][0])
        start = x.find("(") + len("(")
        end = x.find("+")
        substringx = x[start:end]
        substringx=int(float(substringx))
        start = x.find("+") + len("+")
        end = x.find("j")
        #if "." in x:
            #end = x.find(".")
        substringy = x[start:end]
        substringy=int(float(substringy))
        print (substringy)
        arrtr.append([substringx,substringy])
    #print(arrtr)
    gray= cv2.Canny(imgsvg,75,100)
    #cv2.imshow("DetCircle", gray)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (5, 5))

    #print(imgsvg)
    for i in  range(1,len(arrtr)):
        cv2.line(imgsvg,(arrtr[i-1][0],arrtr[i-1][1]),(arrtr[i][0],arrtr[i][1]),(i*(255/len(arrtr)),0,0),5)
    cv2.line(imgsvg,(arrtr[len(arrtr)-1][0],arrtr[len(arrtr)-1][1]),(arrtr[0][0],arrtr[0][1]),(i*(255/len(arrtr)),0,0),5)

    #parse_path("M199,370c-10-16-64-76-64-76L15,258l35-93l85-39h57l7,18l48-18l32,21l32,65c0,0,40-17,44-19s58-14,63-5s28,63,30,66s5,52,0,55s-66,39-66,39l83-2l31,36l16,10.9c0,0,52,4.1,52,15.1s8,26,9,30s-25,33-31,28s-56-29-56-29l-48,53c0,0-65,2-65,5s-36,44-36,44l-39.4,40L195,607l-81,5c0,0-42-96-41-99s16-67,16-67l-14-42c0,0-26-57-21-63s41-32,41-32l52,8L199,370z")

    print(paths)
    print(paths[4].start)

    circs=[]

    f = open("B_ornek-02.svg", "r")
    lines = f.readlines()

    for l in lines:
        if "circle" in l:
            start = l.find('cx="') + len('cx="')
            end = l.find('" cy=')
            substringx = l[start:end]
            substringx=int(float(substringx))
            start = l.find('cy="') + len('cy="')
            end = l.find('" r=')
            #if "." in l:
                #end = l.find(".")
            substringy = l[start:end]
            substringy=int(float(substringy))
            print (substringy)
            circs.append([substringx,substringy])

    for c in circs:
        cv2.circle(imgsvg, ( int(c[0]), int(c[1]) ), 15, (0, 255, 0), 3)


    cv2.imshow("Detected Circle", imgsvg)"""
    
    nmg = cv2.resize(img, (960, 540))  
    cv2.imshow('imga',nmg) 

    min=0
    max=9999999
    minind=0
    maxind=0
    for i in range(len(arrkeep)):
        if (arrkeep[i][0]+arrkeep[i][1])>min:
            min=(arrkeep[i][0]+arrkeep[i][1])
            maxind=i
        if (arrkeep[i][0]+arrkeep[i][1])<max:
            max=(arrkeep[i][0]+arrkeep[i][1])
            minind=i

    """
    min2=0
    max2=9999999
    min2ind=0
    max2ind=0
    for i in range(len(circs)):
        if (circs[i][0]+circs[i][1])>min2:
            min2=(circs[i][0]+circs[i][1])
            max2ind=i
        if (circs[i][0]+circs[i][1])<max2:
            max2=(circs[i][0]+circs[i][1])
            min2ind=i


    print (circs[min2ind],circs[max2ind])
    print("CIRC on svg",circs)

    testang=circs[2]
    #testang[0]=0
    print("hand circs0",circs[0],"circs2",circs[1],"testang",testang)
    print("hand angle svg",360-getAngle(circs[0],circs[1],(0,circs[1][1])))

    lenssvg=[]
    for i in range(len(circs)):
        for j in range(i+1,len(circs)):
           lenssvg.append(((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1])))
    lenssvg.sort()
    print (lenssvg)



    for i in range(len(circs)):
        ctt=0
        ctb=0
        ctr=0
        for j in range(len(circs)):
            if (i!=j):
                if(((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[0] or ((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[1]):
                    ctb+=1
            if (i!=j):
                if(((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[2] or ((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[1]):
                    ctt+=1
            if (i!=j):
                if(((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[0] or((circs[i][0]-circs[j][0])*(circs[i][0]-circs[j][0]))+((circs[i][1]-circs[j][1])*(circs[i][1]-circs[j][1]))==lenssvg[2]):
                    ctr+=1
                    
        if(ctb==2):
            print("THIS BOTTOM",circs[i])
            cbot=circs[i]
        if(ctt==2):
            print("THIS TOP",circs[i])
            ctop=circs[i]
        if(ctr==2):
            print("THIS RIGHT",circs[i])
            crig=circs[i]
            

    print("auto angle svg",360-getAngle(ctop,cbot,(0,cbot[1])))

    a=(arrkeep[0][0]-arrkeep[0][0])*(arrkeep[1][0]-arrkeep[1][0])+(arrkeep[0][0]-arrkeep[0][0])*(arrkeep[1][0]-arrkeep[1][0])
    """

    #print (arrkeep[minind],arrkeep[maxind])
    #print("CIRCS on read",arrkeep)


    #testang1=arrkeep[2]
    #testang1[0]=0
    #print("angle read",360-getAngle(np.array(arrkeep[1], dtype=np.float64),np.array(arrkeep[2], dtype=np.float64),np.array((0,arrkeep[2][1]), dtype=np.float64)))
    #print(math.radians(360-getAngle(arrkeep[1],arrkeep[3],testang1)))

    ###PUTS LENGTHS BETWEEN POINTS IN ARRAY AND SORTS THEM 
    arrkeep=np.array(arrkeep, dtype=np.float64)
    lensim=[]
    for i in range(len(arrkeep)):
        for j in range(i+1,len(arrkeep)):
           lensim.append(((arrkeep[i][0]-arrkeep[j][0])*(arrkeep[i][0]-arrkeep[j][0]))+((arrkeep[i][1]-arrkeep[j][1])*(arrkeep[i][1]-arrkeep[j][1])))
    lensim.sort()
    """
    print (lensim)
    print("arkeep",arrkeep)
    print("nimg0",sum(nimg[int(arrkeep[0][1]),int(arrkeep[0][0])]))
    print("nimg1",sum(nimg[int(arrkeep[1][1]),int(arrkeep[1][0])]))
    print("nimg2",sum(nimg[int(arrkeep[2][1]),int(arrkeep[2][0])]))"""
    #PICKS THE RING FROM CIRCLES BY FINDING WHICH ONE IS EMPTY---HIGHEST PIXEL SUM ==CLOSEST TO WHITE
    keep=0
    print(arrkeep)
    for i in range(1,len(arrkeep)):
        if(sum(nimg[int(arrkeep[i][1]),int(arrkeep[i][0])])>sum(nimg[int(arrkeep[keep][1]),int(arrkeep[keep][0])])):
            keep=i
        else:
            continue
    
    #print(keep)
    atop=arrkeep[keep]

    #print("THIS TOP",atop)
    #print(range(len(arrkeep)))
    for i in range(len(arrkeep)):
        #print("COLOR",nimg[int(arrkeep[i][1]),int(arrkeep[i][0])])  
        cv2.circle(nimg, (int(arrkeep[i][0]), int(arrkeep[i][1])), 1, (0, 255, 0), 3)
        ctb=0
        ctr=0
        if i==keep:
            ctb+=1
        for j in range(len(arrkeep)):
            #if (i!=j):
                #if(((arrkeep[i][0]-arrkeep[j][0])*(arrkeep[i][0]-arrkeep[j][0]))+((arrkeep[i][1]-arrkeep[j][1])*(arrkeep[i][1]-arrkeep[j][1]))==lensim[2] and i!=keep ):
                    #ctb+=1
            if (i!=j):
                if(((arrkeep[i][0]-arrkeep[j][0])*(arrkeep[i][0]-arrkeep[j][0]))+((arrkeep[i][1]-arrkeep[j][1])*(arrkeep[i][1]-arrkeep[j][1]))==lensim[0] and i!=keep):
                    ctr+=1
                    
        if(ctb==0):
            #print("THIS BOTTOM",arrkeep[i])
            abot=arrkeep[i]
        if(ctr==1):
            #print("THIS RIGHT",arrkeep[i])
            arig=arrkeep[i]


            
    cv2.circle(nimg,(int(atop[0]), int(atop[1])), 5, (0, 255, 255), 5)
    cv2.circle(nimg,(int(arig[0]), int(arig[1])), 5, (0, 255, 255), 5)
    nmg = cv2.resize(nimg, (960, 540))  
    cv2.imshow("test", nmg)
    #print("auto angle image",90+getAngle(atop,abot,(0,abot[1])))

    
    #print("last spot Y X",len(img)-1,len(img[len(img)-1])-1)
    #print("last spot Y X test",(len(img)),len(img[len(img)-1]))


    ##kağıt 210*297 

    print(perbox,heig,leng,offsetXincubes,offsetYincubes)

    Yheight=(len(img))
    #print("YHE",Yheight)
    Xlen=len(img[len(img)-1])
    REDmovelen=(atop[0]*arealength)/Xlen
    REDmoveheight=((Yheight-atop[1])*areaheight)/Yheight


    #print("For top left circle(MARKED) move ",REDmovelen+perbox,"mm to right and move",REDmoveheight+perbox,"mm to up")

    RIGmovelen=(arig[0]*arealength)/Xlen
    RIGmoveheight=((Yheight-arig[1])*areaheight)/Yheight
    #print("For top right circle(BLACK) move ",RIGmovelen+perbox,"mm to right and move",RIGmoveheight+perbox,"mm to up")


    checktopx=int((REDmovelen*Xlen)/arealength)
    checktopy=(REDmoveheight*Yheight)/areaheight
    checktopy=int(abs((Yheight-checktopy)))

    #print("checktopx",checktopx,"checktopy",checktopy)


    checkrigx=int((RIGmovelen*Xlen)/arealength)
    checkrigy=(RIGmoveheight*Yheight)/areaheight
    checkrigy=int(abs((Yheight-checkrigy)))



    #cv2. destroyAllWindows() 
    str1="X"+str(int(REDmovelen+perbox-(offsetXincubes*perbox)))+" Y"+str(int(REDmoveheight+perbox-(offsetYincubes*perbox)))
    str2="X"+str(int(RIGmovelen+perbox-(offsetXincubes*perbox)))+" Y"+str(int(RIGmoveheight+perbox-(offsetYincubes*perbox)))
    #print("checkrigx",checkrigx,"checkrigy",checkrigy)
    print(str1)
    print(str2)
    #asyncio.get_event_loop().run_until_complete(listener(str1))
    #asyncio.get_event_loop().run_until_complete(listener(str2))

    #cv2.circle(img,(int(arrkeep[i][0]), int(arrkeep[i][1])), 1, (0, 255, 0), 3)



if __name__ == "__main__":
    dotfinder("distort","distort1",-15,-15,-15,-15,-15)










