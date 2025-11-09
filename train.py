from ultralytics import YOLO

model = YOLO('yolo12n.pt')
results = model.train(
    data='/workspace/ultralytics-main/datasets/data.yaml',  # 修改为实际路径
    epochs=200,
    imgsz=640,
    batch=16,
    name='pepper disease'
)