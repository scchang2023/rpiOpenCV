import cv2
import numpy as np
from deepface import DeepFace
import requests  # 導入 requests 庫
import time

cap = cv2.VideoCapture(0)

# 請將 YOUR_ACCESS_TOKEN 替換為您的 Line Notify Access Token
line_notify_token = 'Line Notify Access Token'
line_notify_api = 'https://notify-api.line.me/api/notify'

# 定義發送到 Line Notify 的函數
def send_to_line_notify(photo_path):
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': '有人微笑了！'}
    files = {'imageFile': open(photo_path, 'rb')}
    response = requests.post(line_notify_api, headers=headers, data=data, files=files)
    print(response.text)

if not cap.isOpened():
    print("無法開啟攝像頭")
    exit()

n = 0
happy = 0

while True:
    ret, img = cap.read()
    if not ret:
        print("無法接收幀")
        break
    
    # 嘗試情緒分析
    try:
        analysis_list = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        if isinstance(analysis_list, list) and len(analysis_list) > 0:
            emotion_analysis = analysis_list[0]
            happy_score = emotion_analysis['emotion']['happy']
            if happy_score > 0.8:
                happy = 1
            else:
                happy = 0
    except Exception as e:
        print(f"情緒分析錯誤: {e}")

    # 如果檢測到微笑或按下空格鍵
    if happy == 1 or cv2.waitKey(1) == 32:
        photo_path = f'photo-{n}.jpg'
        cv2.imwrite(photo_path, img)  # 保存圖片
        print(f'照片 {n} 已保存')
        send_to_line_notify(photo_path)  # 發送圖片到 Line Notify
        n += 1
        happy = 0
        time.sleep(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Camera', img)

cap.release()
cv2.destroyAllWindows()