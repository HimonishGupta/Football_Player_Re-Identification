#  Football_Analysis – YOLO-based Football Match Tracker

This project analyzes football videos by detecting and tracking players and the ball using a **YOLOv11 model**. It produces visual output and saves data for further analytics like tracking positions and movements.

---


##  Features

-  Detects football players, referees, and ball using YOLOv8
-  Tracks each object using unique IDs across frames
-  Stores positional and detection data for each object
-  Outputs annotated video with bounding boxes and labels
-  Clean and modular code for future improvements

---

##  Setup Instructions

### 1. Create a virtual environment 

python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows


### 2.Install all required dependencies
pip install -r requirements.txt

### 3.Add your YOLOv8 model weights
Download or copy your trained YOLO model file (best.pt) and place it inside the models/ folder.

---

##  How to Run
#1. Add an input video
Place your .mp4 or .avi video file in the input_videos/ folder.
Example: input_videos/15sec_input_720p.mp4

#2. Run the main pipeline
python main.py

This will:

Load the YOLO model from models/best.pt

Run detection on the input video

Assign unique IDs to players and ball

Generate an annotated video in output_videos/output.avi

Save tracking data to tracker_stubs/player_detection.pkl

---

## Sample Output

🎞️ output_videos/output.avi — video with bounding boxes and IDs


---

## 🧩 Components Explained

| File/Folder              | Description                                               |
|--------------------------|-----------------------------------------------------------|
| `main.py`                | Main controller to run detection + tracking pipeline      |
| `yolo_inference.py`      | Contains detection logic using YOLOv8                     |
| `trackers/tracker.py`    | Assigns and maintains unique object IDs                   |
| `utils/bbox_utils.py`    | Bounding box helpers (IoU, drawing, conversion)           |
| `utils/video_utils.py`   | Frame reading/writing + FPS/codec handling                |
| `tracker_stubs/player_detection.pkl` | Pickled object data for external analysis       |
| `models/best.pt`         | Fine-tuned YOLOv8 weights used for object detection       |


---

##  Model Training (Optional)

If you'd like to fine-tune your own YOLOv11 model using your football dataset, you can use the Ultralytics CLI:


yolo task=detect mode=train model=yolov11m.pt data=data.yaml epochs=50 imgsz=640


Once trained, place the resulting best.pt file into the models/ directory.

---

##  Requirements

- Python ≥ 3.8  
- torch ≥ 2.0  
- torchvision  
- OpenCV  
- Ultralytics YOLOv8  
- tqdm  
- numpy  

To install everything:

pip install -r requirements.txt


---

