import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

# 配置 MediaPipe Hands
with mp_hands.Hands(static_image_mode=False,
                    max_num_hands=2,  # 最多檢測兩隻手
                    min_detection_confidence=0.5,  # 檢測置信度閾值
                    min_tracking_confidence=0.5) as hands:  # 跟蹤置信度閾值

    if not cap.isOpened():
        print("無法開啟攝像頭")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("無法接收幀")
            break

        img = cv2.resize(img, (520, 300))  # 調整圖像大小
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR轉RGB
        results = hands.process(img_rgb)  # 手部檢測

        # 如果檢測到手部，進行標記
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
        else:
            print("未檢測到手部")  # 如果未檢測到手部，打印提示信息

        cv2.imshow('手勢識別', img)  # 顯示結果
        if cv2.waitKey(5) & 0xFF == ord('q'):  # 按 'q' 退出
            break

cap.release()
cv2.destroyAllWindows()
