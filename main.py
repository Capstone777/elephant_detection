from ultralytics import YOLO
import cv2
import os

# Load YOLO model
model = YOLO("elephant_model.pt")  

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Direct input image path
input_path = "input/1.jpg"  #input image path
output_path = os.path.join(output_dir, f"detected_{os.path.basename(input_path)}")

# Read image
image = cv2.imread(input_path)

# Run YOLO detection
results = model(image)[0]

# Draw detections
for box in results.boxes:
    cls_id = int(box.cls)
    label = model.names[cls_id]
    conf = float(box.conf[0])
    x1, y1, x2, y2 = map(int, box.xyxy[0])

    # Bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Label text
    text = f"{label} {conf:.2f}"
    (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(image, (x1, y1 - h - 4), (x1 + w, y1), (0, 255, 0), -1)
    cv2.putText(image, text, (x1, y1 - 2), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (0, 0, 0), 1, cv2.LINE_AA)

# Save to output folder
cv2.imwrite(output_path, image)
print(f"Saved: {output_path}")
print("Elephant detected")
