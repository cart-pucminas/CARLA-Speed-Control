import cv2
import torch


class DetectionProcessor:
    @staticmethod
    def process(agent, hud, view):
        """Process detections and update the agent behavior and HUD."""
        results = agent.plate_detector(view)
        detections = results.xyxy[0].cpu().numpy()

        for detection in detections:
            if detection[4] > 0.85:  # Confidence threshold
                x1, y1, x2, y2 = map(int, detection[:4])
                cv2.rectangle(view, (x1, y1), (x2, y2), (255, 0, 0), 2)

                cropped = view[y1:y2, x1:x2]
                plates_class = agent.plate_classify(cropped)

                for result in plates_class:
                    if len(result.cpu().boxes.cls) > 0:
                        cls, confidence = DetectionProcessor._get_highest_confidence(result)
                        DetectionProcessor._update_agent_behavior(agent, hud, cls, confidence, (x1, y1), view, result)

    @staticmethod
    def _get_highest_confidence(result):
        """Get the class and confidence of the highest-scoring detection."""
        max_conf_idx = torch.argmax(result.cpu().boxes.conf).item()
        cls = int(result.cpu().boxes.cls[max_conf_idx])
        confidence = float(result.cpu().boxes.conf[max_conf_idx])
        return cls, confidence

    @staticmethod
    def _update_agent_behavior(agent, hud, cls, confidence, coords, view, result):
        """Update agent speed and HUD based on detections."""
        if cls in [1, 2, 3, 4, 5, 6]:
            velocity_map = {1: 30, 2: 60, 3: 90, 4: 30, 5: 40, 6: 60}
            agent.set_speed(velocity_map[cls])

        label = result.names[cls]
        label_text = f"{label} ({confidence:.2f})"
        x1, y1 = coords

        cv2.putText(view, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2, cv2.LINE_AA)

        hud.analysis.update_traffic_signs(label)
