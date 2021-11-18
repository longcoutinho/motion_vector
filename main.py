import cv2
import numpy as np
cap = cv2.VideoCapture('C:/video/akiyo_qcif.y4m')

if cap.isOpened() == False:
    print("Error")
k = 0;
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #cv2.imshow('Frame', frame)
        if (k == 100):
            cv2.imwrite('C:/image/image1.jpg', frame)
        if (k == 105):
            cv2.imwrite('C:/image/image2.jpg', frame)
        k = k + 1;
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

img1 = cv2.imread('C:/image/image1.jpg', 0)
img2 = cv2.imread('C:/image/image2.jpg', 0)

def dif(a, b):
    sum = 0
    for i in range(0, 16):
        for j in range(0, 16):
            sum += abs(int(a[i, j]) - int(b[i, j]))
    return sum

(h, w) = img1.shape
print(h, " ", w)
for i in range(0, h - 16 + 1, 2):
    for j in range(0, w - 16 + 1, 2):
        pre_block = img1[i:i + 16, j:j + 16]
        min_dif = 10000000
        min_row = 0
        min_col = 0
        for k in range(max(0, i - 8), min(h - 16 + 1, i + 16 + 8), 2):
            for l in range(max(0, j - 8), min(w - 16 + 1, j + 16 + 8), 2):
                cur_block = img2[k:k + 16, l:l + 16]
                match_score = dif(pre_block, cur_block)
                if match_score < min_dif:
                    min_dif = match_score
                    min_row = k
                    min_col = l
                else:
                    if match_score == min_dif:
                        if abs(k - i) + abs(l - j) < abs(min_row - i) + abs(min_col - j):
                            min_dif = match_score
                            min_row = k
                            min_col = l
        if i != min_row or j != min_col:
            cv2.arrowedLine(img2, (i + 8, j + 8) , (min_row + 8, min_col + 8), (255, 0, 0), 1)
            #print(i, j, min_row, min_col)
cv2.imshow("Pre Frame", img2)
cv2.waitKey(0)
#cv2.imshow(img2);


