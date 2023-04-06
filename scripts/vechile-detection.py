import yolov5
import cv2

import os.path
from Enums import DetectionType, ModelPaths
import argparse

# Load video file
def detectObjectInVideo(model, videoName):
    videoFilePath = "..\\videos"
    videoFilePath = os.path.join(os.getcwd(),videoFilePath, videoName)
    # Open the video file
    if not os.path.exists(videoFilePath):
        print("path does not exists")
        return
    
    cap = cv2.VideoCapture(videoFilePath)

    # Loop through the frames of the video
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display the frame
        results = model(frame)
        for result in results.xyxy[0]:
            x1, y1, x2, y2, confidence, class_idx = result.tolist()
            class_name = model.names[int(class_idx)]
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, f'{class_name} {confidence:.2f}', (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)
        
        # Wait for a key press and exit if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources
    cap.release()
    cv2.destroyAllWindows()


def getYoloModel(modelType):
    model = None

    if modelType == DetectionType.VechileDetection:
        model = yolov5.load(model_path=ModelPaths.CustomTrainedModel)
        print("model")
        model.classes = [0, 1, 2, 3, 5, 7, ] # person, bicycle, car, motorcycle, bus, truck -> coco dataset values

    elif modelType == DetectionType.VoilationDetection:
        model = yolov5.load(model_path=ModelPaths.VoilationDetection)

    elif modelType == DetectionType.HealmetDetection:
        model = yolov5.load(model_path=ModelPaths.HealmetDetection)

    elif modelType == DetectionType.NumberPlateDetection:
        model = yolov5.load(model_path=ModelPaths.NumberPlateDetection)

    if(model != None):
        # configuring common parameters 
        model.conf = 0.25  # NMS confidence threshold
        model.iou = 0.45  # NMS IoU threshold
        model.agnostic = False  # NMS class-agnostic
        model.multi_label = False  # NMS multiple labels per box
        model.max_det = 1000  # maximum number of detections per image

    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=int, required=True, help="-0 detect all vechiles \n"+
                        "-1 Detect voilated vechiles \n2.Healmet Detection \n3.Lisence  Plate Detection")
    
    parser.add_argument("--path", type=str, required=True, help="upload video into video file and provide the path")

    args = parser.parse_args()

    # print(type(args.type), type(args.path))
    if(args.type != 3):
        model = getYoloModel(DetectionType(args.type))
        print(type(model))
        if model != None:
            detectObjectInVideo(model=model, videoName=args.path)
    # else:
    #     pass
