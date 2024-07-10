import cv2

# 동영상 파일의 경로
video_path = "insideout5.mp4"

# 동영상 파일 열기
video = cv2.VideoCapture(video_path)

# 동영상의 프레임 수
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# 프레임을 이미지로 변환하고 파일로 저장
for i in range(frame_count):
    ret, frame = video.read()
    if not ret:
        break  # 프레임 읽기 실패시 중단
    if i % 4 == 0:  # 4 프레임마다 해당 프레임 처리
        image_path = f"insideout5image/{i}.jpg"
        cv2.imwrite(image_path, frame)
    for _ in range(3):  # 다음 3프레임 건너뛰기
        if not video.grab():
            break

# 동영상 파일 닫기
video.release()
