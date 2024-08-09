import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models

resize_train_mean = [0.5238798, 0.5212542, 0.5029558]
resize_train_std = [0.14364697, 0.1437464, 0.15269105]

transform = transforms.Compose([
    transforms.Resize((224,224)), 
    transforms.ToTensor(),
    transforms.Normalize(mean=resize_train_mean, std=resize_train_std)
])

image_path = r'/home/tony8181/Desktop/roy/captured_image.jpg'   
image = Image.open(image_path).convert('RGB')
image = transform(image).unsqueeze(0) 

resnet18 = models.resnet18()  
num_ftrs = resnet18.fc.in_features
resnet18.fc = torch.nn.Linear(num_ftrs, 3)  

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
resnet18 = resnet18.to(device)

resnet18.load_state_dict(torch.load(r'/home/tony8181/Desktop/roy/resnet_18.pth', map_location=device))
resnet18.eval()  

image = image.to(device)
with torch.no_grad():
    outputs = resnet18(image)
    _, predicted = torch.max(outputs, 1)

class_names = ['001_Clear', '002_Label', '003_Colored']  

predicted_class = class_names[predicted.item()]
print(f'Predicted class: {predicted_class}')
