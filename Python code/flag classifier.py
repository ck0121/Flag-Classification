# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:31:58 2020

@author: ck
"""

import torchvision
from torchvision import transforms

train_data_path = "D:\Blander Flag\Flag-Classifiction\Training_Data"

transforms = transforms.Compose([
        transforms.Resize(64),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
        ])

train_data = torchvision.datasets.ImageFolder(root=train_data_path,transform=transforms)

val_data_path = "D:\Blander Flag\Flag-Classifiction\Validation_Data"
val_data = torchvision.datasets.ImageFolder(root=val_data_path,
                                            transform=transforms)

test_data_path = "D:\Blander Flag\Flag-Classifiction\Test_Data"
test_data = torchvision.datasets.ImageFolder(root=test_data_path,
                                             transform=transforms)

batch_size=64
train_data_loader = data.DataLoader(train_data, batch_size=batch_size)
val_data_loader = data.DataLoader(val_data, batch_size=batch_size)
test_data_loader = data.DataLoader(test_data, batch_size=batch_size)


class SimpleNet(nn.Module):
    
    
def __init__(self):
    super(Net, self).__init__()
    self.fc1 = nn.Linear(12288, 84)
    self.fc2 = nn.Linear(84, 50)
    self.fc3 = nn.Linear(50,2)
    
def forward(self):
    x = x.view(-1, 12288)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = F.softmax(self.fc3(x))
    return x

simplenet =SimpleNet()


def forward(self):
    # Convert to 1D vector
    x = x.view(-1, 12288)
    x = F.relu(self.fc1(x))
    x = F.relu(self.fc2(x))
    x = self.fc3(x)
    return x
    
for epoch in range(epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        input, target = batch
        output = model(input)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
    
model.to(device)


def train(model, optimizer, loss_fn, train_loader, val_loader,
          epochs=20, device="cpu"):
    for epoch in range(epochs):
        training_loss = 0.0
        valid_loss = 0.0
        model.train()
        for batch in train_loader:
            optimizer.zero_grad()
            inputs, target = batch
            inputs = inputs.to(device)
            target = targets.to(device)
            output = model(inputs)
            loss = loss_fn(output, target)
            loss.backward()
            optimizer.step()
            training_loss += loss.data.item()
        training_loss /= len(train_iterator)
        
        model.eval()
        num_correct = 0
        num_example = 0
        for batch in val_loader:
            inputs, targets = batch
            inputs = inputs.to(device)
            output = model(inputs)
            targets = targets.to(device)
            loss = loss_fn(output,targets)
            valid_loss += loss.data.item()
            correct = torch.eq(torch.max(F.softmax(output), dim=1)[1],
                                                            target).view(-1)
            num_correct += torch.sum(correct).item()
            num_examples += correct.shape[0]
        valid_loss /= len(valid_iterator)
        
        print('Epoch: {}, Training Loss: {:.2f}, Validation Loss:{:.2f},accuracy = {:.2f}'.
              format(epoch, training_loss, valid_loss, num_correct / num_examples))
        
        
train(simplenet, optimizer, torch.nn.CrossEntropyLoss(),
      train_data_loader, test_data_loader,device)


from PIL import Image

labels = ['America','Canada','Delaware']

img = Image.open(FILENAME)
img = transforms(img)
img = img.unsqueeze(0)

prediction = simplenet(img)
prediction = prediction.argmax()
print(labels[prediction])





        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    