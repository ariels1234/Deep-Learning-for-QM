from torch.utils.data import Dataset, DataLoader
import torch
import numpy as np
from torchvision import datasets, transforms
from PIL import Image
import glob

class CustomDataset(Dataset):

    def __init__(self, path, n_classes=100, transform=False):
        
        self.transform = transform
        
        self.filelist = glob.glob(path+'/*.npy') 
       
        labels = np.zeros(len(self.filelist))


        for class_i in range(n_classes):
          files_that_are_of_this_class = ['serial='+str(class_i) in x for x in self.filelist]
          labels[ files_that_are_of_this_class ] = class_i
        
        self.labels = torch.LongTensor(labels)


    def __len__(self):
       
        return len(self.filelist)

    def __getitem__(self, idx):
        
        vector = np.load(self.filelist[idx])  
        
        x = vector
        x = torch.tensor(x)
        # x = transforms.ToTensor()(x)
        x = x.repeat(3,1) 
        y = self.labels[idx] 

        return x, y

