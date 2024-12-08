### RPi OPENCV實作範例

安裝需要的套件
```
sudo apt-get update
sudo apt-get install libopencv-dev
sudo apt-get install python3-opencv
```

人臉辨識時，需要下載的haarcascade特徵檔案
```
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml


wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
```

將本地的檔案複製到遠端
```
scp -r rpiOpenCV pi@192.168.1.118:/home/pi
```