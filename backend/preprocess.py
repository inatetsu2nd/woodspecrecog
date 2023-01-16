import cv2
import numpy as np

def pil2cv(pil_image):
#    ''' PIL型 -> OpenCV型 '''
        cv_image = np.array(pil_image, dtype=np.uint8)
        if cv_image.ndim == 2:  # モノクロ
            pass
        elif cv_image.shape[2] == 3:  # カラー
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)
        elif cv_image.shape[2] == 4:  # 透過
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGBA2BGRA)
        return cv_image/255

def preprocess(img):
  cv_img = pil2cv(img)
  h, w, _ = cv_img.shape
  if h<=w:
    cv_img = cv_img[:, 0: h]
  else:
    cv_img = cv_img[0 : w, :]

  color_img=cv_img[:,:,[2,1,0]]

  resized_img = cv2.resize(color_img, (640, 640))

  patches = []
  for i in range(10):
    for j in range(10):
        patches.append(resized_img[64*i:64*(i+1), 64*j:64*(j+1)])
  patches= np.array(patches)
  return patches