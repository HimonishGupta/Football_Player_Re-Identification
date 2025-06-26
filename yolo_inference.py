from ultralytics import YOLO

model=YOLO('models/best.pt')

result=model.predict(source="input_videos/15sec_input_720p.mp4",save=True)

result=model.track(source="input_videos/15sec_input_720p.mp4",save=True)