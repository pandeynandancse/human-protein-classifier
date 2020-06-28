from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn


import torch.nn.functional as F

# Define a flask app
app = Flask(__name__)

MODEL_PATH = 'models/model_resnet.pth'


labels = {
    0: 'Mitochondria',
    1: 'Nuclear bodies',
    2: 'Nucleoli',
    3: 'Golgi apparatus',
    4: 'Nucleoplasm',
    5: 'Nucleoli fibrillar center',
    6: 'Cytosol',
    7: 'Plasma membrane',
    8: 'Centrosome',
    9: 'Nuclear speckles'
}


class AdaptiveConcatPool2d(nn.Module):
    def __init__(self, sz=1):
        super().__init__()
        self.adavgp = nn.AdaptiveAvgPool2d(sz)
        self.adamaxp = nn.AdaptiveMaxPool2d(sz)
        
    def forward(self, x):
        x = torch.cat([self.adavgp(x), self.adamaxp(x)], 1)
        x = x.view(x.size(0),-1)
        return x



class CustomClassifier(nn.Module):
    def __init__(self, in_features, intermed_bn= 512, out_features=10, dout=0.25):
        super().__init__()
        self.fc_bn0 = nn.BatchNorm1d(in_features)
        self.dropout0 = nn.Dropout(dout)
        self.fc0 = nn.Linear(in_features, intermed_bn, bias=True)
        self.fc_bn1 = nn.BatchNorm1d(intermed_bn, momentum=0.01)
        self.dropout1 = nn.Dropout(dout * 2)
        self.fc1 = nn.Linear(intermed_bn, out_features, bias=True)
        
    def forward(self, x):
        x = self.fc_bn0(x)
        x = self.dropout0(x)
        x = F.relu(self.fc0(x))
        x = self.fc_bn1(x)
        x = self.dropout1(x)
        x = self.fc1(x)
        return x



model = models.resnet18(pretrained=True)
model.avgpool = AdaptiveConcatPool2d()
model.fc = CustomClassifier(in_features=model.fc.in_features*2, out_features=10)
model.load_state_dict(torch.load(MODEL_PATH,map_location=torch.device('cpu')))



data_transforms = transforms.Compose([
        transforms.RandomCrop(512, padding=8, padding_mode='reflect'),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.0793, 0.0530, 0.0545], std=[0.1290, 0.0886, 0.1376])
        ])



def pred_single(img_path, return_label=True):
    with torch.no_grad():
        model.eval()
        print(img_path)
        img = Image.open(img_path)
        img = data_transforms(img)
        bs_img = img.unsqueeze(0)
        #bs_img = bs_img.to(device)
        preds = torch.sigmoid(model(bs_img))
        prediction = preds[0]
        return prediction


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')



def decode_labels(target, thresh=0.5, return_label=True):
    result = []
    for i, tgt in enumerate(target):
        if tgt > thresh:
            result.append(str(i) + ":" + labels[i] + " ")           
    return result


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = pred_single(file_path, model)
        result = decode_labels(preds)
        result = result[0] + "" + result[1]
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True,threaded=False)

