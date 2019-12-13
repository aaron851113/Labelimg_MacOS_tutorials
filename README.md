# Labelimg_MacOS_tutorials

> 深度學習初探 - HW1 - Labelimg MacOS tutorials

### 0. Reference 
- Labelimg : https://github.com/tzutalin/labelImg
- Download hw file in e3<br />
    ![](https://i.imgur.com/usQ2Mss.png)
- Windows系統的同學，直接點開 [**LabelImgWindows_v1.8.0**] -> [**labelImg.exe**]
- open [**新增 Microsoft....dox**]
- MacOS的同學請參考以下步驟

### 1. environment
- MacOS 10.14
- python 3 (3.5~3.7)
    ```
    $ pip install msgpack
    $ pip install labelImg
    ```
    <br />
    ![](https://i.imgur.com/CSD27yV.png)
    ```
    $ labelImg
    ```
    <br />
    ![](https://i.imgur.com/vLxZJZ3.png)
- 桌面建立一個label的file<br />
    ![](https://i.imgur.com/4bPZLPc.png)

    
### 2. Test labelImg
- [改變存放目錄] -> [選取到上一個step創建的label file]<br />
    ![](https://i.imgur.com/P65cJM4.png)<br />
    ![](https://i.imgur.com/oEWoGAM.png)
- [開啟檔案] / [開啟目錄]<br />
    ![](https://i.imgur.com/8Qmie2o.png)
- [調整圖片顯示大小]<br />
    ![](https://i.imgur.com/PC7zP3V.png)
- [右鍵] -> [創建區塊]<br />
    ![](https://i.imgur.com/PC1w1hm.png)
- create label<br />
    ![](https://i.imgur.com/r55lrj4.png)
    ![](https://i.imgur.com/uEtI2IJ.png)
- [儲存]<br />
    ![](https://i.imgur.com/3e2Dc38.png)


### 3. Video to image
![](https://i.imgur.com/usQ2Mss.png)<br />
- [Video] -> [label 影片分配名單.xlsx] -> 查看自己的影片代號
- Create a File [video_to_picture]
- modify **main_video2image.py**
```
import numpy as np
import cv2
import time 

video_path='114_TidingBlvd1-Gangqian-PSh_20191025_0700-1000_0013_0752-1252.avi'

interval=15 
video_capture = cv2.VideoCapture('video/'+video_path)
sucess=1
c=0

while(sucess):
    sucess, frame = video_capture.read()
    if (c%interval==0):
        savefigure_name = 'video_to_picture/'+video_path.split('.')[0]+'_'+str(c) + '.jpg'
        cv2.imwrite(savefigure_name, frame)
    c+=1
  
video_capture.release()

```
- compile
