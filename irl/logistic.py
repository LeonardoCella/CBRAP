# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 13:20:59 2015

@author: lenovo
"""

import numpy as np
class logistic:
    def __init__(self,data):
        self.data=data
    
    
    def Frequency_cal():
        z_terminal=1
    
    def logistic_irl(self, alpha, niter):
        avg_recall=0
        for user in self.data.user2arms.keys():
           # print "Start training"
            times=self.data.user2arms[user].keys()
            times.sort()
           # print len(times)
            w=np.random.rand(self.data.nbfeatures-1)
            ntr=len(self.data.user2arms[user].keys())*2//3
          #  print ntr
            for iteration in xrange(niter):
                for index in xrange(ntr):
                    # print times[index]
                    #print (self.data.user2arms[user][times[index]])
                    tau=float(1)/(1-np.exp(-np.dot(w,self.data.user2arms[user][times[index]][:-1])))
                    w-=np.array(self.data.user2arms[user][times[index]][:-1])*(self.data.user2arms[user][times[index]][-1]-tau)
            recall=0
            true=0
           # print "Start testing"
            for index in xrange(ntr,len(self.data.user2arms[user])):
                #print times[index]
                if self.data.user2arms[user][times[index]][-1]==1:
                    true+=1
                    if float(1)/(1-np.exp(-np.dot(w,self.data.user2arms[user][times[index]][:-1])))>0.5:
                        recall+=1
            if true!=0:
                avg_recall+=float(recall)/true
        return float(avg_recall)/self.data.nbusers
                