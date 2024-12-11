### RPi OPENCV實作範例

更新軟體包及安裝opencv相關driver及套件：
```
sudo apt-get update
sudo apt-get install libopencv-dev
sudo apt-get install python3-opencv
```

人臉辨識時，需要下載的haarcascade特徵檔案：
```
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
```

將本地的檔案複製到遠端：
```
scp -r rpiOpenCV pi@192.168.1.118:/home/pi
```
為了驗証 camera 是不是可以用的，可以安裝 guvcview 的軟體試看看。
```
sudo apt-get install guvcview
```
### 使用 RPi 的內建 motion 功能

更新軟體包
```
sudo apt-get update
```
安裝 motion
```
sudo apt-get install motion
```
編輯 motion config
```
sudo nano /etc/motion/motion.conf
```
設定參數：
```
# on：啟動後自動在後台執行，而不會佔用當前的終端。
# off：即時顯示log，適合用於調試。
daemon = on

# 開啟串流與網頁管理功能
stream_localhost off
webcontrol_localhost off

# 照片放置資料夾路徑
Target_dir /var/lib/motion

# 解析度
width 320
height 240

# jpg品質
Output_pictures on
quality 90

# 每秒最高的frame數
framerate 4

# 雜訊門檻值(愈低代表愈抗雜訊)
noise_level 64

# 偵測變動像素門檻值(愈低愈敏感)
threshold 3000

# 關閉影片輸出
ffmpeg_output_movies off

# 標示畫面中有變動的部份
locate_motion_mode on

# 用紅色方框標示
locate_motion_style redbox
```
啟動/停止服務
```
sudo motion
service motion stop
service motion status
```