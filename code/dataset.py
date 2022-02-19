import torch
from PIL import Image

import argparse
import glob

class RGBDDataset(torch.utils.data.Dataset):
    def __init__(self, args: argparse.ArgumentParser, transform=None):
        #self.path = args.path
        #self.depth_path = self.path + "dataset/depth"
        #self.rgb_path = self.path + "dataset/color"
        
        #self.depth_img_list = glob.glob(self.depth_path + "/*.png")
        #self.rgb_img_list = glob.glob(self.rgb_path + "/*.jpg")
        self.depth_img_list = glob.glob("../dataset/depth"+ "/*.png")
        self.rgb_img_list = glob.glob("../dataset/color"+ "/*.jpg")
        
        self.transform = transform
        
    def __len__(self):
        return len(self.depth_img_list)
    
    def __getitem__(self, idx):
        depth_path = self.depth_img_list[idx]
        rgb_path = self.rgb_img_list[idx]
        
        depth_img = Image.open(depth_path)
        rgb_img = Image.open(rgb_path)
        
        #depth = torch.FloatTensor(depth_img)
        #rgb = torch.FloatTensor(rgb_img)
        
        if self.transform is not None:
            depth = self.transform(depth_img)
            rgb = self.transform(rgb_img)
        else: 
            depth = depth_img 
            rgb = rgb_img
        
        return depth, rgb
