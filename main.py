from re import X
import cv2
import pickle
import time
import modules.videoPlayer as player   
import modules.selectAds as ads   
import modules.ageAndGender as  redefine 
from collections import Counter

loaded_model = pickle.load(open("./model/finalized_model.sav", 'rb'))


faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"


faceNet=cv2.dnn.readNet(faceModel, faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-14)', '(15-24)', '(25-37)', '(38-47)', '(48-59)', '(60-100)']
genderList = ['Male', 'Female']

predAge = 0
predGender = 0
prediction = [0]
padding=20

def faceBox(faceNet,frame):
    frameHeight=frame.shape[0]
    frameWidth=frame.shape[1]
    blob=cv2.dnn.blobFromImage(frame, 1.0, (300,300), [104,117,123], swapRB=False)
    faceNet.setInput(blob)
    detection=faceNet.forward()
    bboxs=[]
    for i in range(detection.shape[2]):
        confidence=detection[0,0,i,2]
        if confidence>0.7:
            x1=int(detection[0,0,i,3]*frameWidth)
            y1=int(detection[0,0,i,4]*frameHeight)
            x2=int(detection[0,0,i,5]*frameWidth)
            y2=int(detection[0,0,i,6]*frameHeight)
            bboxs.append([x1,y1,x2,y2])
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 1)
    return frame, bboxs

             
while True:
    start = time.time()         
    elapsed = 0   
    flag = True
    video =cv2.VideoCapture(0) 
    vals  = []
    
    
    while elapsed < 10:  
        ret,frame=video.read()
        frame, bboxs=faceBox(faceNet,frame)
        for bbox in bboxs:
            # face=frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]
            face = frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPred=genderNet.forward()
            gender=genderList[genderPred[0].argmax()]

            ageNet.setInput(blob)
            agePred=ageNet.forward()
            age=ageList[agePred[0].argmax()]
            
            predAge,predGender = redefine.ageAndGender(age,gender)   
            z=[[predGender,predAge]]
            prediction = loaded_model.predict(z)
            vals.append(prediction[0])

            label="{},{}".format(gender,age)
            cv2.rectangle(frame,(bbox[0], bbox[1]-30), (bbox[2], bbox[1]), (0,255,0),-1) 
            cv2.putText(frame, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2,cv2.LINE_AA)
            
        cv2.imshow("Age-Gender",frame)
        
        elapsed = time.time() - start #update the time elapsed

        k=cv2.waitKey(1)
        if k==ord('q'):
            flag = False
            break
    
    if flag == False:
        break
        
    
    video.release()
    cv2.destroyAllWindows()
    maxPredictions = Counter(vals).most_common(1)[0][0]
    ad = ads.selectAdds(maxPredictions)
    player.videoPlayer(ad)

