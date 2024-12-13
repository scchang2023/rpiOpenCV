import cv2
import numpy as np
from deepface import DeepFace  # 载入 DeepFace

cap = cv2.VideoCapture(0)  # 讀取攝像頭

# 定義在畫面中放入文字的函數
def putText(source, text, x, y, scale=1.0, color=(255, 255, 255), thickness=2):
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(source, text, (x, y), fontFace, scale, color, thickness, cv2.LINE_AA)

n = 0  # 檔案名編號
happy = 0  # 是否有 happy 的變量

if not cap.isOpened():
    print("無法開啟攝像頭")
    exit()

while True:
    ret, img = cap.read()  # 讀取每一幀
    if not ret:
        print("無法接收幀")
        break
    
    # 嘗試情緒分析
    try:
        analysis_list = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)
        if isinstance(analysis_list, list) and len(analysis_list) > 0:
            emotion_analysis = analysis_list[0]  # 獲取列表中的第一個元素
            happy_score = emotion_analysis['emotion']['happy']
            print(f"Happy 分數: {happy_score}")  # 打印 happy 分數
            if happy_score > 0.5:  # 調整閾值以更好地檢測到微笑
                happy = 1
            else:
                happy = 0
    except Exception as e:
        print(f"情緒分析錯誤: {e}")

    # 如果檢測到微笑或按下空格鍵，則觸發拍照
    if happy == 1 or cv2.waitKey(1) == 32:
        cv2.imwrite(f'photo-{n}.jpg', img)  # 保存圖片
        print(f'照片 {n} 已保存')
        n += 1  # 更新檔案編號
        happy = 0  # 重置 happy 狀態

    if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下 'q' 退出
        break

    cv2.imshow('Camera', img)  # 顯示圖像

cap.release()
cv2.destroyAllWindows()
