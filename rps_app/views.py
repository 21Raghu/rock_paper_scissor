import random
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Result
# Create your views here.
game = ['rock','paper','scissor']
class rock_paper_scession(APIView):
    def get(self,request):
        n,res_data = random.randint(0, 2),{}
        if (request.data['user']=='rock' and n==0) or (request.data['user']=='paper' and n==1) or \
                (request.data['user']=='scissor' and n==2):
            res_data["computer"]= game[n]
            res_data["result"]="Draw!!! try next..."
            p = Result(user=request.data['user'], comp=game[n],res = "Draw")
            p.save()
            return Response(res_data)
        elif (request.data['user']=='paper' and n==2) or (request.data['user']=='scissor' and n==0):
            res_data["computer"] = game[n]
            res_data["result"]="You loose | try next"
            p = Result(user=request.data['user'], comp=game[n],res = "User Loose")
            p.save()
            return Response(res_data)
        else:
            res_data["computer"] = game[n]
            res_data["result"]="Congratulation you won... :) "
            p = Result(user=request.data['user'], comp=game[n],res = "User Won")
            p.save()
            return Response(res_data)

# "Rock vs paper->paper wins
#  "Rock vs scissor->Rock wins
# "paper vs scissor->scissor wins \n")