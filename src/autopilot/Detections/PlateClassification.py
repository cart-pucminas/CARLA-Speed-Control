from ultralytics import YOLO


class PlateClassification:
    def __init__(self, model_path):
        # self.model = YOLO('/home/tom/projects/tcc/AdversarialAutoDrive/src/Plate_Classification/model/best.pt', verbose=False)
        self.model = YOLO(model_path, verbose=False)

    def detect(self, image_path):
        results = self.model.predict(image_path, verbose=False)
        return results