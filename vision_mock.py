def mock_resnet_classify(image_path):
    image_path = image_path.lower()
    if "dog" in dog.jpeg:
        return "Dog"
    elif "cat" in cat.jpeg:
        return "Cat"
    elif "bird" in peacock.jpeg:
        return "Bird"
    else:
        return "Unknown"