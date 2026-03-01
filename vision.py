from ultralytics import YOLOWorld

model = YOLOWorld('yolov8s-world.pt')

def get_ingredients(image_path):
    
    global_vocabulary = [
        "bread", "pasta", "rice", "cheese", "egg", "meat", "chicken", 
        "fish", "broccoli", "tomato", "carrot", "apple", "banana", 
        "potato", "avocado", "bell pepper", "spinach", "lentils", "tofu"
    ]
    model.set_classes(global_vocabulary)
    
    results = model.predict(image_path, conf=0.25)
    
    detected = [model.names[int(c)].capitalize() for r in results for c in r.boxes.cls]
    return list(set(detected))