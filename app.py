from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import csv
import logging
import api

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def homepage():
    return render_template("index.html")

@app.route("/review" , methods = ['POST' , 'GET'])
def index():
    if request.method == 'POST':
        searchString = request.form['content'].replace(" ","")
        api.read(searchString)
        p_name=api.Product_Name
        name=api.name
        rating=api.rating
        commentHead=api.commentHead
        custComment=api.custComment
        productLink=api.productLink
        Lenght=len(p_name) 

        return render_template('result.html',len=len(p_name),P_name=p_name,Name=name,rating=rating,commentHead=commentHead,Comment= custComment,productLink=productLink)

        

    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run()
