from django.shortcuts import render, redirect
import random
import json

# Create your views here.
def index(request):
    nums = {
         1:"one",
        2: "two",
         3:"three",
         4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10 :"ten",
    }
    data = []
    with open("./data.json", "r",encoding="utf-8") as f:
        data = json.load(f)

    Ndata = random.sample(data, len(data))
    quotes = []
    for e in Ndata:
        if len(e["quote"]) <= 91 and len(quotes) < 10:
            e["id"] = len(quotes) + 1
            e["num"] = nums[e["id"]]
            if e["id"] == 10:
                e["next"] = nums[1]
            else:
                e["next"] = nums[int(e["id"]) + 1]
            quotes.append(e)
        elif len(e["quote"]) <= 91 and len(quotes) >= 10:
            break
        else:
            pass

    items = [
        {"id": 1, "num": "one", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" ,"next": "two"},
        {"id": 2, "num": "two", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt", "next": "three"},
        {"id": 3, "num": "three", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "four"},
        {"id": 4, "num": "four", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt"   , "next": "five"},
        {"id": 5, "num": "five", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "six"},
        {"id": 6, "num": "six", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "seven"},
        {"id": 7, "num": "seven", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "eight"},
        {"id": 8, "num": "eight", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt"  , "next": "nine"},
        {"id": 9, "num": "nine", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "ten"},
        {"id": 10, "num": "ten", "text": " Develop a passion for learning. If you do, you will never cease to grow.", "author": "Dojo Tshirt" , "next": "one"},
    ]
    return render(request, "index.html", context={"items": quotes})



