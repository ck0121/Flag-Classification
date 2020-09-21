# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:31:58 2020

@author: ck
"""






import torch

import torch.nn as nn

import torch. optim as optim

import torch. utils. data

import torch. nn. functional as F

import torchvision

from torchvision import transforms

from PIL import Image, ImageFile

 

ImageFile.LOAD_TRUNCATED_IMAGES=True

 

def check_image(path):
    print(path);
    try:

        im = Image.open(path)

        return True

    except:

        return False

   

img_transforms = transforms.Compose([

        transforms.Resize((64,64)),

        transforms.ToTensor(),

        transforms.Normalize(mean=[0.485, 0.456, 0.406],

                             std=[0.229, 0.224, 0.225])

        ])

 

train_data_path = "./Data_Sets/Training_Data"

train_data = torchvision.datasets.ImageFolder(root=train_data_path,transform=img_transforms, is_valid_file=check_image)

 

val_data_path = "./Data_Sets/Validation_Data"

val_data = torchvision.datasets.ImageFolder(root=val_data_path,transform=img_transforms, is_valid_file=check_image)

 

test_data_path = "./Data_Sets/Test_Data"

test_data = torchvision.datasets.ImageFolder(root=test_data_path,transform=img_transforms, is_valid_file=check_image)

 

print('---------------  OK ----------------------  1')

 

batch_size=64

 

train_data_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size)
print("***** total number of images in 'Training_Data is  %4d' % len(train_data)")
val_data_loader  = torch.utils.data.DataLoader(val_data, batch_size=batch_size)

test_data_loader  = torch.utils.data.DataLoader(test_data, batch_size=batch_size)

 

print('---------------  OK ----------------------  2')

 

class SimpleNet(nn.Module):

 

    def __init__(self):

        super(SimpleNet, self).__init__()

        self.fc1 = nn.Linear(12288, 84)

        self.fc2 = nn.Linear(84, 50)

        self.fc3 = nn.Linear(50,3)

   

    def forward(self, x):

        x = x.view(-1, 12288)

        x = F.relu(self.fc1(x))

        x = F.relu(self.fc2(x))

        x = self.fc3(x)

        return x

   

simplenet = SimpleNet()

 

print('---------------  OK ----------------------  3')

 

optimizer = optim.Adam(simplenet.parameters(), lr=0.001)

 

print('---------------  OK ----------------------  4')

 

if torch.cuda.is_available():

    device = torch.device("cuda")

else:

    device = torch.device("cpu")

 

print('---------------  OK ----------------------  5')

 

simplenet.to(device)

 

print('---------------  OK ----------------------  6')

 

def train(model, optimizer, loss_fn, train_loader, val_loader, epochs=20, device="cpu"):

    for epoch in range(epochs):

        training_loss = 0.0

        valid_loss = 0.0

        model.train()

        for batch in train_loader:

            optimizer.zero_grad()

            inputs, targets = batch

            inputs = inputs.to(device)

            targets = targets.to(device)

            output = model(inputs)

            loss = loss_fn(output, targets)

            loss.backward()

            optimizer.step()

            training_loss += loss.data.item() * inputs.size(0)

        training_loss /= len(train_loader.dataset)

       

        model.eval()

        num_correct = 0

        num_examples = 0

        for batch in val_loader:

            inputs, targets = batch

            inputs = inputs.to(device)

            output = model(inputs)

            targets = targets.to(device)

            loss = loss_fn(output,targets)

            valid_loss += loss.data.item() * inputs.size(0)

            correct = torch.eq(torch.max(F.softmax(output, dim=1), dim=1)[1], targets)

            num_correct += torch.sum(correct).item()

            num_examples += correct.shape[0]

        valid_loss /= len(val_loader.dataset)

 

        print('Epoch: {}, Training Loss: {:.2f}, Validation Loss: {:.2f}, accuracy = {:.2f}'.format(epoch, training_loss,

        valid_loss, num_correct / num_examples))

       

print('---------------  OK ----------------------  7')

       

train(simplenet, optimizer,torch.nn.CrossEntropyLoss(), train_data_loader,val_data_loader, epochs=5, device=device)

 

print('---------------  OK ----------------------  8')

 

labels = ['America','Canada']

 

 

img = Image.open("./Validation_Data/America/0288.JPG")  # ????????????????????????????????

 

print('-------------------------------------------------------')

print(img)

 

img = img_transforms(img).to(device)

 

prediction = F.softmax(simplenet(img), dim=1)

prediction = prediction.argmax()

print(labels[prediction])

 

 

torch.save(simplenet, "/tmp/simplenet")

simplenet = torch.load("/tmp/simplenet")

 

torch.save(simplenet.state_dict(), "/tmp/simplenet")   

simplenet = SimpleNet()

simplenet_state_dict = torch.load("/tmp/simplenet")

simplenet.load_state_dict(simplenet_state_dict)