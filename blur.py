import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.transforms import transforms  
from torchvision.utils import save_image
import cv2

class CNN(nn.Module):
    def __init__(self):  # Use double underscores here
        super(CNN, self).__init__()  # Corrected super() call

        self.conv1 = nn.Conv2d(3, 128, kernel_size=5, padding=1)
        self.conv2 = nn.Conv2d(128, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 3, kernel_size=1, padding=1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))

        return x
    
def deblur(filename):
    device = 'cpu'
    model = CNN().to(device).eval()
    model.load_state_dict(torch.load('model_1.3.pth', map_location=device))
    def save_decoded_image(img, name):
        img = img.view(img.size(0), 3, 224, 224)
        save_image(img, name)

    transform = transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
])

    image = cv2.imread(f"static/input/{filename}")
    orig_image = image.copy()
    orig_image = cv2.resize(orig_image, (224, 224))
    cv2.imwrite("resized.jpg", orig_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        save_decoded_image(outputs.cpu().data, name="output.jpg")
    
    i = cv2.imread("output.jpg")
    deblurred = cv2.resize(i, (350,350))
    cv2.imwrite("static/output/deblurred.jpg", deblurred)
