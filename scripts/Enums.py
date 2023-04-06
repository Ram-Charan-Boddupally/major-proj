from enum import Enum

class DetectionType(Enum):
    VechileDetection = 0
    VoilationDetection = 1
    HealmetDetection = 2
    NumberPlateDetection = 3

class ModelPaths:
    CustomTrainedModel = "../weights/yolov5m.pt"
    VoilationDetection = "../weights/Voilation-detection-model.pt"
    HealmetDetection = "../weights/Healmet-detection-model.pt"
    NumberPlateDetection = "../weights/NumberPlateDetectionModel.pt"
