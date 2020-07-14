# human-protein-classifier

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Directory Tree](#directory-tree)
  * [Installation](#installation)
  * [Run](#run)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Contribution](#contribution)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [Credits](#credits)


## Demo
![](https://i.imgur.com/IYAGMTh.png)



## Overview
This is a simple multi label image classification application developed using pytorch. The trained model can be downloaded and stored inside models folder with name model_resnet.pth that takes image as an input via file upload and then model predicts protiens present in the image.


## Directory Tree 
```
├── models
|    ├── model_resnet.pth
├── static
|    ├── css
|    ├── js
|    ├── images
├── templates
|    ├── base.html
|    ├── result.html
├── uploads
├── Dockerfile
├── Procfile
├── README.md
├── activation.bat
├── app.py
├── requirements.txt

```

## Installation
1. Windows user can double click on activation.bat file to install required package
2. Linux User type following command in commnand line
a) First create a virtual environment 
```bash
python3.7 -m virtualenv venv
```
b) Move to venv directory and activate environment
```bash
cd venv
. bin/activate
```
c) Clone this project 
```bash
git clone https://github.com/pandeynandancse/human-protein-classifier.git
```

d) Move into cloned directory
```bash
cd human-protein-classifier
```
e) Now install all requirements
```bash
pip install -r requirements.txt
```
## Run
1. After successfull installation windows user can directly open this link : https://127.0.0.1:5000
2. After successful installation open type
```bash
python app.py
 ```
and then open link : https://127.0.0.1:5000

## To Do
1. More Interactive and stylish
2. Multi Image prediction at same time



## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/pandeynandancse/human-protein-classifier/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/pandeynandancse/human-protein-classifier/issues/new). Please include sample queries and their corresponding results.


## Contribution
If you'd like to do some contribution, feel free to do so by opening a pull request [here](https://github.com/pandeynandancse/human-protein-classifier/pulls). Please include sample queries and their corresponding results.




## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://www.vectorlogo.zone/logos/pytorch/pytorch-ar21.svg" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) 




## Team
[![Nandan Pandey](https://qph.fs.quoracdn.net/main-thumb-189737418-200-jmwzsixdznlgemnejuecomukeluqkgzd.jpeg)](https://pandeynandancse.github.io) |
-|
[Nandan Pandey](https://pandeynandancse.github.io) |)



## Credits
1. Special thanks to Kris Naik sir, front end source code has been taken from one of his project.
2. Special thanks to Akash NS sir,Founder of jovian.ml and Instructor of the course ZERO-to-GANs using pytorch , who hosted related dataset on [Kaggle](https://www.kaggle.com/c/jovian-pytorch-z2g) and organized in-class competition..
