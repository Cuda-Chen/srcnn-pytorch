#

from PIL import Image
from torchvision import transforms

img = "lenna.bmp"

input_img = Image.open(img)
print(input_img.size)

pil_to_tensor = transforms.ToTensor()(input_img).unsqueeze_(0)
print(pil_to_tensor.shape) 

tensor_to_pil = transforms.ToPILImage()(pil_to_tensor.squeeze_(0))
print(tensor_to_pil.size)
