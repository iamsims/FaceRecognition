import urllib.request
import numpy as np
import cv2
from DETECT import detect_face

def capture(url):
    imgResp=urllib.request.urlopen(url)
    image=imgResp.read()
    imgNp=np.array(bytearray(image),dtype=np.uint8)
    img_shot=cv2.imdecode(imgNp,-1)
   # cv2.imshow("cropped", img_shot)
   # cv2.waitKey(0)
   # cv2.destroyAllWindows()
    padding=10
    print('Before the function call to detect')
    x1,y1,x2,y2=detect_face(img_shot)
    
    print('After the function call to detect')
    if (x1==0 and y1==0 and x2==0 and y2==0):
        print('No face at all')    
        return 

    x1-=padding
    y1-=padding
    x2+=padding
    y2+=padding

    shot_cropped_img = img_shot[y1:y2, x1:x2]
    cv2.imshow("cropped", shot_cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    shot_gray_cropped_img = np.mean(shot_cropped_img, axis=2)
    final_img = cv2.resize(shot_gray_cropped_img, (92, 112), interpolation = cv2.INTER_NEAREST)

    return final_img
