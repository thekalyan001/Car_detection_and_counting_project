import cv2
import numpy as np

# capture frames from a video
video = cv2.VideoCapture("roadPP.mp4")


# loop runs if capturing has been initialized
while True:
    ret, frame= video.read()  #ret tells true or false if video finished

    #loading only the grayscale format and detecting the edges.
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow= np.array([18, 94, 140])
    up_yellow= np.array([48, 255, 255])
    mask= cv2.inRange(hsv, low_yellow, up_yellow)

    #Once we have the mask we find the edges, we use the hough transform method and the detection is done
    edges= cv2.Canny(mask,75, 150)

    #we have above a white image with black lines.
    #On the edges we apply the lines detection using hough transform:
    lines= cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50) #edges,rho,theta in redian, threShold
    if lines is not None: #if we try to draw line but there is no line
    	for line in lines:
    		x1 ,y1, x2, y2= line[0]
    		cv2.line(frame, (x1, y1), (x2, y2), (0,255,0),5) # x1y1 x2y2 color(green,blue,green) ,thickness


    cv2.imshow("frame", mask)
    cv2.imshow("Edges", edges)

    #if video finish then afgain load from 0
#     if not ret:
#         video = cv2.VideoCapture("road_car_view.mp4")
#         continue
        
    cv2.imshow("frame", frame)
    
    key=cv2.waitKey(25)
    
    if key==27:
        break
video.release()
cv2.destroyAllWindows() 

'''
HoughLinesp(parameter)
edges: Output of the edge detector.
lines: A vector to store the coordinates of the start and end of the line.
rho: The resolution parameter \rho in pixels.
theta: The resolution of the parameter \theta in radians.
threshold: The minimum number of intersecting points to detect a line.
'''