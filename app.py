# -*- coding: utf-8 -*-
"""
Created on 17 August 2021

@author: Muzammil

"""
# Importing Libraries
from scipy.spatial import distance as dist


import numpy as np
import os
import cv2





from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'




@app.route('/', methods=['POST'])
def analyze():
  ## here are three methods for requesting the data you can use
        #as your requirment 
    file1 = request.files['query_img']
    text1 = request.form['txt']
    
    file1 = request.files['image'].read() ## byte file
    npimg = np.fromstring(file1, np.uint8)
    image = cv2.imdecode(npimg,cv2.IMREAD_COLOR)

    
    return jsonify(dicw)

    #return objects

if __name__=="__main__":
    app.run("127.0.0.1")


