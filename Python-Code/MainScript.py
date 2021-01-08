#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:12:34 2021

@author: leick

Main script for executing all code at once
"""
import os

#input directory of your Code
codedir="/home/leick/Documents/AndreaGanna/Code/endpoint-liability/Python-Code"
endpointPath="/home/leick/Documents/AndreaGanna/Data/newFake/fake_endpoints_sub.csv"
pillPath="/home/leick/Documents/AndreaGanna/Data/newFake/fake_cum_pills_sub.csv"
#tree pic will be saved here
picPath=codedir
#If you want a binary prediction set True alse False
binary= True


os.chdir(codedir)

#imports preped Data from DataPrep
import DataPrep as dataPrep
learnData=dataPrep.dataPrep(endpointPath, pillPath, binary)

#shortcut for already calculated Table
#learnData=pd.read_csv("/home/leick/Documents/AndreaGanna/Data/newFake/2020-12-07-con_endpoint_drug_table_small.csv")


#imports trained modell from ML-DecTree
import MLDecTree as xgbTree
#sets the endpoint of interest
endpoint="I9_STR_EXH"
delCol=["I9_STR_SAH","I9_SEQULAE", "I9_STR", "IX_CIRCULATORY"]
#discards coloumns with high correlation to endpoint
corrValue=0.995
#final dataprep and modell training
accuracy, treeModell, corrDropList=xgbTree.MLdecTree(learnData, picPath, endpoint, delCol, corrValue, binary)


