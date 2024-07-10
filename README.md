![insideout1](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/e9bb9d37-8f11-4230-adf6-fbdfc9a5e130)

## Project 소개

- 영화 ‘Inside Out1’ 캐릭터 감정을 분석하는 프로젝트이다
- 인간의 감정 인식에 대한 연구는 널리 이루어졌으나, animation 캐릭터의 감정 인식에 대한 연구는 제한적이며, animation 중에서도 감정을 다루는 영화의 캐릭터의 감정을 분석하였다
- 캐릭터 ‘기쁨이’ 😀 는 항상 기쁠까?
캐릭터 ‘슬픔이’ 🥲 는 항상 슬플까?
캐릭터 ‘버럭이’ 🤬 는 항상 화날까?
- Slide : [DNN을 활용한 INSIDEOUT Character emotion 분석](https://drive.google.com/file/d/1TMiEGXGWE4zp4NMQVnZ72c0IvUS8h94x/view?usp=drive_link)

## Contributors

![insideout2](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/f8ef3259-9ed6-432b-9fac-8576ff227b53)

BITamin 12기 김재원, 김채원, 문승민, 이서현, 황영서

## Reference Paper

Paper :

[Understanding cartoon emotion using integrated deep neural network on large dataset](https://link.springer.com/article/10.1007/s00521-021-06003-9)

Paper Review : 

[[Paper Review  For Project] Understanding cartoon emotion using integrated deep neural network on large dataset](https://velog.io/@youngseoh6/Semi-Paper-Review-Understanding-cartoon-emotion-using-integrated-deep-neural-networkon-large-dataset)

## Image Data 수집

- 영화 ‘Inside Out 1’ 에서 OpenCV를 활용하여 4프레임 단위로 이미지 8000장 수집
- 영화 캐릭터와 관련 없는 장면 Image Filtering 하여 약 3000장으로 진행

## Experiments

### 1) Character Segmentation with YoloV8

- roboflow를 활용하여,  character segmentaion 하기 위해 labeling ( annotation, resize, augmnetation  진행 )

![insideout3](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/847e49c7-90d8-4a9f-acb3-0d44f366c15b)

- 총 약 6000장의 이미지로 YOLOV8 모델 학습하여 bounding box 와 segmenation mask 생성

![insideout4](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/688a3755-906e-4984-b8bd-ee3a7426f420)

- YOLOV8 모델 학습 결과

![insideout5](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/d54e7d9e-002a-43ae-b199-679e368fe291)

### 2) Emotion Classification

- YOLOV8의 wieght 파일을 활용하여, findContours 하여 캐릭터들의 face extraction 하고,  face crop 진행

- roboflow를 활용하여,  emotion classification 하기 위해 labeling

![insideout6](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/9baaaf20-6915-4b77-95f3-7f990e6db3de)

- transfer learning pretrained classification model
  BaseModel을 정해두고, 조건들을 변경해가며 실험 진행

  [transfer learning pretrained clasification model Experiment 과정](https://fearless-gourd-ac8.notion.site/Insideout-emotion-classification-experiments-05d2e6a91d71456c8c9bb678dcc6933f)

  최종적으로, 
   1. HyperPrameter 
     - batch size : 32 , epochs : 30 
   2. Augmentation Method
     - autoagumentation
   3. Optimzier & Scheduler
    - SGD & StepLR
   4. Transfer Learning Model Architecture 
    - ResNet50 

**→ Test loss :	0.9067, Accuracy 76.98 %**

## Results

![insideout7](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/e53d64b9-38bd-4e62-86ba-a6cc0f523c55)

![insideout8](https://github.com/youngseoh/Insideout_emotionclassification/assets/100707876/75a88c47-ba6d-4078-9e37-7bce645f8e6e)
