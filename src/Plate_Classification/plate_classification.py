from ultralytics import YOLO

def train(self):
    """
    Train the model with YOLOv11
    """

    # Load a model
    model = YOLO("yolo11n.pt")

    # Train the model
    train_results = model.train(
        data="./Plate_Classification/dataset.yml",  # path to dataset YAML
        epochs=5,  # number of training epochs
        imgsz=640,  # training image size
    )

    # Evaluate model performance on the validation set
    metrics = model.val()

def classify(self, image):
    """
    Classify the image
    """
    # Load a model
    model = YOLO("yolo11n.pt")

    # Classify the image
    results = model(image)

    return results


train()