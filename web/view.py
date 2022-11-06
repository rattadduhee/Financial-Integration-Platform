from audioop import avg
from statistics import mean
from django.shortcuts import render, redirect
from .models import WebUser, WebConsume, WebSaving, WebCard, WebApartment, StockInteg, StockChart, StockAct
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from web.forms import UserForm
from rest_framework.response import Response
from rest_framework.views import APIView
from time import mktime, strptime, strftime
import numpy as np
from django.core import serializers
from datetime import datetime
# from .models import Myuser
import pandas as pd
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'../templates/index.html')

def home(request):
    return render(request,'../templates/Home.html')

def login(request):
    return render(request,'../templates/로그인.html')

def 소비(request):
    user_id = request.user.id
    my_info = WebConsume.objects.filter(username=user_id)
    return render(request,'../templates/마이_개인소비성향.html', {'my_info':my_info})


def 적금카드(request):
    user_age = request.user.age
    save_info = WebSaving.objects.filter(age=user_age)
    card_info = WebCard.objects.filter(age=user_age)
    return render(request,'../templates/적금카드.html', {'age':user_age,'save_info':save_info, 'card_info':card_info})

def 주거(request):
    hope_address = request.user.hope_address.split(" ")
    best = WebApartment.objects.filter(price__lte = int(request.user.available_asset),dong = hope_address[2]).values()

    #가용자산범위 안의 희망 동 추출
    if not best:
        best = WebApartment.objects.filter(price__lte = int(request.user.available_asset)).values()
        best = best.order_by("-pyeong",'price')
        temp = []
        for i in range(5):
            if best[i] not in temp:
                temp.append(best[i])
            if len(temp) == 3:
                break
        best_1 = temp[0]
        best_2 = temp[1]
        best_3 = temp[2]

    elif request.user.child == '있음':
        best = best.order_by("-pyeong",'price')
        temp = []
        for i in range(5):
            if best[i] not in temp:
                temp.append(best[i])
            if len(temp) == 3:
                break
        best_1 = temp[0]
        best_2 = temp[1]
        best_3 = temp[2]
    else :
        best = best.order_by("-pyeong",'price')
        temp = []
        for i in range(5):
            if best[i] not in temp:
                temp.append(best[i])
            if len(temp) == 3:
                break
        best_1 = temp[0]
        best_2 = temp[1]
        best_3 = temp[2]
    return render(request,'../templates/부동산_맞춤주거지역.html', {'best_1':best_1, 'best_2':best_2, 'best_3':best_3})


@csrf_exempt
def 실거래가(request):    
    if request.method == 'POST':
        apt = request.POST['keyword']
        apt_data = pd.DataFrame(WebApartment.objects.filter(apt_name__contains = apt).values())
        apt_list = WebApartment.objects.filter(apt_name__contains = apt,cont_year__lte = 2023).values().order_by('-cont_year')[:10]
        msg=''
        size = sorted(apt_data['pyeong'].unique())
        year = dict()
        price= dict()
        for i in size:
            year[f'{i}평'] = sorted(list(set(map(int,apt_data[apt_data['pyeong']==i]['cont_year'].values))))
            price[f'{i}평'] = list(np.round(apt_data[apt_data['pyeong']==i].groupby('cont_year').mean()['price'],-3).astype('int').values/10000)

        if not apt_list:
            apt_list = WebApartment.objects.filter(apt_name__contains = apt).values()[:10]
            msg = '최근 5년간 거래내역이 없어요. 예측가로 안내해드릴게요.'
        return render(request, '../templates/부동산_실거래가조회.html', {'apt':apt,'apt_list':apt_list,'apt_data':apt_data,'msg':msg,'price':price,'years':year})

    else:
        return render(request, '../templates/부동산_실거래가조회.html')


def 부동산(request):
    return render(request,'../templates/부동산.html')
def 설명회(request):
    return render(request,'../templates/설명회정보.html')

@csrf_exempt
def 주식(request):
    
    kb = StockInteg.objects.filter(name__contains='KB금융').order_by('date').last() # KB금융
    ss = StockInteg.objects.filter(name__contains='삼성전자').order_by('date').last() # 삼성전자
    nc = StockInteg.objects.filter(name__contains='엔씨소프트').order_by('date').last() # 엔씨소프트
    kko = StockInteg.objects.filter(name__contains='카카오').order_by('date').last() # 카카오
    lge = StockInteg.objects.filter(name__contains='LG전자').order_by('date').last() # LG전자
    naver = StockInteg.objects.filter(name__contains='네이버').order_by('date').last() # 네이버
    sk = StockInteg.objects.filter(name__contains='SK').order_by('date').last() # SK
    ct = StockInteg.objects.filter(name__contains='셀트리온').order_by('date').last() # 셀트리온
    lgc = StockInteg.objects.filter(name__contains='LG화학').order_by('date').last() # LG화학
    cj = StockInteg.objects.filter(name__contains='CJ제일제당').order_by('date').last() # CJ제일제당
    ssg = StockInteg.objects.filter(name__contains='신세계').order_by('date').last() # 신세계

    if request.method == 'POST':
        key = request.POST['keywords']
        date_list = StockInteg.objects.filter(name__contains= key).values()
        stocks = StockChart.objects.filter(name__contains= key).values().order_by('date')

        close_list = []
        open_list = []
        for stock in stocks:
            time_tuple = strptime(str(stock['date']), '%Y-%m-%d') 
            utc_now = mktime(time_tuple) * 1000           
            close_list.append([utc_now, stock['close']])
            open_list.append([utc_now, stock['open']])
        return render(request, '../templates/주식.html', {"stock":stocks,"key":key,"date_list_json":date_list, 'close': close_list,'open': open_list,"kb":kb,"ss":ss,"nc":nc,"kko":kko,"lge":lge,"naver":naver,"sk":sk,"ct":ct,"lgc":lgc,"cj":cj,"ssg":ssg})
    else:
        key = "KB금융"
        date_list = StockInteg.objects.filter(name__contains = key).values()
        stocks = StockChart.objects.filter(name__contains= key).values().order_by('date')

        close_list = []
        open_list = []
        for stock in stocks:
            time_tuple = strptime(str(stock['date']), '%Y-%m-%d') 
            utc_now = mktime(time_tuple) * 1000           
            close_list.append([utc_now, stock['close']])
            open_list.append([utc_now, stock['open']])
        return render(request, '../templates/주식.html', {"stock":stocks,"key":key,"date_list_json":date_list, 'close': close_list,'open': open_list,"kb":kb,"ss":ss,"nc":nc,"kko":kko, "lge":lge,"naver":naver,"sk":sk,"ct":ct,"lgc":lgc,"cj":cj,"ssg":ssg})

def 주식예측(request):
    key = request.GET["key"]
    act_list = StockAct.objects.filter(name__contains = key).values()
    return render(request,'../templates/주식예측.html',{"key":key,"act_list_json":act_list})


# 로그인
@csrf_exempt
def login(request):
    # login으로 POST 요청이 들어왔을 때, 로그인 절차를 밟는다.
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장한다.
        username = request.POST['username']
        password = request.POST['password']

        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        
        # 해당 user 객체가 존재한다면
        if user is not None:
            # 로그인 한다
            auth.login(request, user)
            return redirect('/')
        # 존재하지 않는다면
        else:
            # 딕셔너리에 에러메세지를 전달하고 다시 login.html 화면으로 돌아간다.
            return render(request, '../templates/로그인.html', {'error' : '아이디 또는 비밀번호가 일치하지 않습니다.'})
    # login으로 GET 요청이 들어왔을때, 로그인 화면을 띄워준다.
    else:
        return render(request, '../templates/로그인.html')

# 로그 아웃
def logout(request):
    # logout으로 POST 요청이 들어왔을 때, 로그아웃 절차를 밟는다.
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')

    # logout으로 GET 요청이 들어왔을 때, 로그인 화면을 띄워준다.
    return render(request, '../templates/로그인.html')


def 회원가입(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
          
            return redirect('login')
    else:
        form = UserForm()
    return render(request, '../templates/회원가입.html', {'form': form})
