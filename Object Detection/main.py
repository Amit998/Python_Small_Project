import numpy as np
import cv2


image_path="images/000001.jpg"

prototxt_path="models/MobileNetSSD_deploy.prototxt"
model_path="models/MobileNetSSD_deploy.caffemodel"


min_confidence=0.1



classNames = { 0: 'background',
    1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
    5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
    10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse',
    14: 'motorbike', 15: 'person', 16: 'pottedplant',
    17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor' }





np.random.seed(54321)
colors=np.random.uniform(0,255,size=(len(classNames),3))

net=cv2.dnn.readNetFromCaffe(prototxt_path, model_path)



image=cv2.imread(image_path)
height,width=image.shape[0],image.shape[1]
blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007,(300,300),130)


net.setInput(blob)

detected_objects=net.forward()
# print(detected_objects[0][0][0])


for i in range(detected_objects.shape[2]):
    confidence=detected_objects[0][0][i][2]

    if confidence > min_confidence:
        class_index=int(detected_objects[0,0,i,1])

        upper_left_x=int(detected_objects[0,0,i,3]*width)
        upper_left_y=int(detected_objects[0,0,i,4]*height)
        lower_right_x=int(detected_objects[0,0,i,5]*width)
        lower_right_y=int(detected_objects[0,0,i,6]*height)


        prediction_text=f"{classNames[class_index]}:{confidence:2.f}%"
        cv2.rectangle(image,(upper_left_x,upper_left_y),(lower_right_x,lower_right_y),colors[class_index])
        cv2.putText(image,prediction_text,(upper_left_x,upper_left_y,upper_left_y-15 if upper_left_y > 30 else upper_left_y+15),cv2.FONT_HERSHEY_SIMPLEX,0.6,colors[class_index])


cv2.imshow("Detected Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


