import cv2
import numpy as np
image = cv2.imread('rubix1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayPlot = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
cv2.imshow('Original image',image)

# dimensions
height = gray.shape[0]
width = gray.shape[1]

# horizontal and vertical range
offset = 4
x_start = 0 + offset
x_end = width - offset
y_start = 0 + offset
y_end = height - offset

# threshold
t = 40
# pre-store incides 
idx_hs = np.array([[3,0,-3,0], [0,3,0,-3]]) # 1 5 9 13
idx_circle = np.array([[3,3,2,1,0,-1,-2,-3,-3,-3,-2,-1,0,1,2,3], \
	[0,1,2,3,3,3,2,1,0,-1,-2,-3,-3,-3,-2,-1]])

# iterate through all of pixels
for y in range (y_start,y_end):
	#print("y: " + str(y))
	for x in range(x_start,x_end): # indexes end-1
		i_p = gray[y][x]

		# high speed test
		i_1 = gray[y+idx_hs[0][0]][x+idx_hs[1][0]]
		i_5 = gray[y+idx_hs[0][1]][x+idx_hs[1][1]]
		i_9 = gray[y+idx_hs[0][2]][x+idx_hs[1][2]]
		i_13 = gray[y+idx_hs[0][3]][x+idx_hs[1][3]]  
		if int(i_1 > i_p + t)+int(i_5 > i_p + t)+int(i_9 > i_p + t)+int(i_13 > i_p + t) >=3 or \
		int(i_1 < i_p - t)+int(i_5 < i_p - t)+int(i_9 < i_p - t)+int(i_13 < i_p - t) >= 3:

			# slower test
			for p in range(16): # 0 through 15

				# intensity of first point in arc
				i_first = gray[y+idx_circle[0][p]][x+idx_circle[1][p]]
				# brighter
				if (i_first > i_p + t):
					intensity = 1
				# darker
				elif (i_first < i_p - t):
					intensity = 0
				# neither
				else: 
					continue 

				# do rest of points match
				foundArc = True
				for i in range(12):
					p_next = (p+i+1)%16
					i_next = gray[y+idx_circle[0][p_next]][x+idx_circle[1][p_next]]
					if (intensity == 1 and (i_next <= i_p + t)) or (intensity == 0 and (i_next >= i_p - t)):
						foundArc = False
						break
				# passed the test, 12 continuous
				if foundArc:
					cv2.circle(grayPlot,(x, y), 3, (255,0,0),1)
					break

			
cv2.imshow('Gray image with circles', grayPlot)  
cv2.waitKey(0)
cv2.destroyAllWindows()