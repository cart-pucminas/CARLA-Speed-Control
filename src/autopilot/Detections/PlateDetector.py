import torch 

class PlateDetector:
    def __init__(self, model_path):
        # self.model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/tom/projects/tcc/AdversarialAutoDrive/src/Plate_Detector/model/best.pt')
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

    def detect(self, image_path):
        results = self.model(image_path)
        return results
        
