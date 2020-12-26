from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from search.documents import *
from fbprophet import Prophet
from pandas.core.frame import DataFrame
import pandas as pd # package for high-performance, easy-to-use data structures and data analysis // 数据处理库
import numpy as np # fundamental package for scientific computing with Python
#画图
# Create your views here.
def quary(request):
    if request.method == "GET":
        request.params = request.GET
        city = request.params["c"]
        province = request.params['p']
        type= request.params["type"]
        if type=="death":
            s=DeathDocument.search().query('match',city=city).query('match',province=province)
            datas=[]
            for l in s:
                data = {}
                data["X"] = l.Range
                data["Y"] = l.death
                datas.append(data)
            return JsonResponse({
             "result":datas
            })
        elif type=="confirmed":
            s = ConfirmedDocument.search().query('match', city=city).query('match', province=province)
            datas = []
            for l in s:
                data = {}
                data["X"] = l.Range
                data["Y"] = l.confirmed
                datas.append(data)
            return JsonResponse({
                "result": datas
            })
    else:
        return JsonResponse({
            "msg": "wrong method"
        })


def listcity(request):
    if request.method == "GET":
        request.params = request.GET
        state = request.params["state"]
        type = request.params["type"]
        if type == "confirmed":
            s = ConfirmedDocument.search().query('match', province=state)[0:1000]
            print(s)
            confirmed = []
            for l in s:
                data={}
                m=l.confirmed.replace("\n"," ")
                k=m.split(" ")
                data["city"] = l.city
                data["confirmed"] = k[len(k)-1][:-1]
                confirmed.append(data)
            return JsonResponse({
                    "msg": "200",
                    "data":confirmed
                })
        elif type == "death":
            s = DeathDocument.search().query('match', province=state)[0:1000]
            print(s)
            death = []
            for l in s:
                data={}
                m=l.death.replace("\n"," ")
                k=m.split(" ")
                data["city"] = l.city
                data["death"] = k[len(k)-1][:-1]
                death.append(data)
            return JsonResponse({
                    "msg": "200",
                    "data":death
                })
    else:
        return JsonResponse({
                "msg": "wrong method"
            })


def state(request):
    s = StatesDocument.search().query('match_all')[0:1000]
    data=[]
    for l in s:
        datas={}
        datas['province'] = l.province
        datas["	updateTime"] = l.updateTime
        datas["confirmed"] = l.confirmed
        datas["death"] = l.death
        datas["recovered"] = l.recovered
        datas["active"] = l.active
        datas["rate"] = l.rate
        data.append(datas)
    return JsonResponse({
        "msg": "200",
        "data":data
    })


def prodict(request):
    return JsonResponse({
        "confirmed":60
    })