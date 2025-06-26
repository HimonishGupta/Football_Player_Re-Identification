football_analysis – YOLO-based Football Match Tracker
This project analyzes football videos by detecting and tracking players and the ball using a YOLOv8 model. It produces visual output and saves data for further analytics like tracking positions and movements.

📁 Folder Structure
bash
Copy
Edit
football_analysis/
│
├── input_videos/              # Raw input videos
│   └── 15sec_input_720p.mp4
│
├── models/                    # Pre-trained YOLO weights
│   ├── best.pt
│   └── yolo11m.pt
│
├── output_videos/            # Final annotated video output
│   └── output.avi
│
├── runs/detect/              # YOLO intermediate predictions
│   └── predict*/15sec_input_720p.avi
│
├── tracker_stubs/
│   └── player_detection.pkl   # Pickled tracking data
│
├── trackers/                 # Tracker logic
│   ├── __init__.py
│   └── tracker.py
│
├── utils/                    # Utility functions
│   ├── bbox_utils.py
│   └── video_utils.py
│
├── main.py                   # Pipeline entry point
├── yolo_inference.py         # YOLO detection logic
├── yolo11x.pt                # Extra model (if used)
└── requirements.txt
🚀 Features
⚽ Detects football players and the ball using YOLOv8

📍 Tracks objects across frames

🧠 Stores tracking data for post-game analysis

📼 Annotated video output with bounding boxes and IDs

📦 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/football_analysis.git
cd football_analysis
2. Create a virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate       # macOS/Linux
# OR
venv\Scripts\activate          # Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Download or add your YOLOv8 model weights
Add your trained best.pt file in the models/ directory.

▶️ How to Run
1. Place the input video
Place your .mp4 or .avi match video inside the input_videos/ folder.

2. Run the full pipeline
bash
Copy
Edit
python main.py
This will:

Load the model from models/best.pt

Read the video from input_videos/

Run inference using yolo_inference.py

Store annotated output to output_videos/output.avi

🖼️ Sample Output
output_videos/output.avi – includes bounding boxes and labels

runs/detect/ – contains intermediate predictions from YOLO

🧩 Components Explained
File	Description
main.py	Main execution script
yolo_inference.py	Loads model and performs detection
tracker.py	Associates object IDs across frames
bbox_utils.py	Bounding box helper functions
video_utils.py	Video I/O and frame annotation
player_detection.pkl	Pickled object detections

📈 Model Training (Optional)
If you want to train your own model, you can use the Ultralytics YOLOv8 CLI or script:

bash
Copy
Edit
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
✅ Requirements
Python ≥ 3.8

Ultralytics YOLOv8

OpenCV

NumPy

tqdm

torch, torchvision

Install via:

bash
Copy
Edit
pip install -r requirements.txt
