# 동영상을 이미지(프레임)로 나누어 저장
# mov01.avi 동영상의 프레임수가 401 이므로 401장의 이미지가 저장


import cv2

mov01 = cv2.VideoCapture("mov/mov01.avi")  # 동영상 불러오기
imageNum = 0

while(mov01.isOpened()):
    ret, frame = mov01.read()  # mov01에 저장된 동영상을 프레임 단위로 처리하여 불러오기
    if ret == True:
        cv2.imshow("mov01 frame", frame)
        filepath = f"snapshot/snapshot_{imageNum}.jpg"  # 이미지가 저장될 경로 지정
        cv2.imwrite(filepath, frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # 키보드의 q 가 클릭되면 종료
            break
    imageNum = imageNum + 1

mov01.release()
cv2.destroyAllWindows()  # 창 닫기