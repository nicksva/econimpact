from flask import Flask,redirect,url_for,render_template
from matplotlib.figure import Figure
import base64
from io import BytesIO
from pitoniskuili.fafa import firsty,secondy,thirdy,fifthy,firstx,secondx,thirdx,fourthx,fifthx,graph1,graph2,graph5,graph3,graph4,fourthy,fifthy

app = Flask(__name__) 

examp=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
p=0
q=0
FirstY=[]
while p < firsty.__len__():
    if(graph1[q]!=0):
        FirstY.append(firsty[p]+' '+'2019')
    q=q+1
    if(graph1[q]!=0):
        FirstY.append(firsty[p]+' '+'2020')
    q=q+1
    if(graph1[q]!=0):
        FirstY.append(firsty[p]+' '+'2021')
    q=q+1
    p=p+1
v=0
Graph1=[]
while v<graph1.__len__():
    if(graph1[v]!=0):
        Graph1.append(graph1[v])
    v=v+1
p=0
q=0
SecondY=[]
while p < secondy.__len__():
    if(graph2[q]!=0):
        SecondY.append(secondy[p]+' '+'2019')
    q=q+1
    if(graph2[q]!=0):
        SecondY.append(secondy[p]+' '+'2020')
    q=q+1
    if(graph2[q]!=0):
        SecondY.append(secondy[p]+' '+'2021')
    q=q+1
    p=p+1
v=0
Graph2=[]
while v<graph2.__len__():
    if(graph2[v]!=0):
        Graph2.append(graph2[v])
    v=v+1
p=0
q=0
ThirdY=[]
while p < thirdy.__len__():
    if(graph3[q]!=0):
        ThirdY.append(thirdy[p]+' '+'2019')
    q=q+1
    if(graph3[q]!=0):
        ThirdY.append(thirdy[p]+' '+'2020')
    q=q+1
    if(graph3[q]!=0):
        ThirdY.append(thirdy[p]+' '+'2021')
    q=q+1
    p=p+1
v=0
Graph3=[]
while v<graph3.__len__():
    if(graph3[v]!=0):
        Graph3.append(graph3[v])
    v=v+1
p=0
q=0
FourthY=[]
while p < fourthy.__len__():
    if(graph4[q]!=0):
        FourthY.append(fourthy[p]+' '+'2019')
    q=q+1
    if(graph4[q]!=0):
        FourthY.append(fourthy[p]+' '+'2020')
    q=q+1
    if(graph4[q]!=0):
        FourthY.append(fourthy[p]+' '+'2021')
    q=q+1
    p=p+1
v=0
Graph4=[]
while v<graph5.__len__():
    if(graph4[v]!=0.0):
        Graph4.append(graph4[v])
    v=v+1
p=0
q=0
FifthY=[]
while p < fifthy.__len__():
    if(graph5[q]!=0):
        FifthY.append(fifthy[p]+' '+'2019')
    q=q+1
    if(graph5[q]!=0):
        FifthY.append(fifthy[p]+' '+'2020')
    q=q+1
    if(graph5[q]!=0):
        FifthY.append(fifthy[p]+' '+'2021')
    q=q+1
    p=p+1
v=0
Graph5=[]
while v<graph5.__len__():
    if(graph5[v]!=0.0):
        Graph5.append(graph5[v])
    v=v+1
@app.route("/")
def home():
    return render_template("hyperpoop.html")
@app.route("/EU-GDP-Growth")
def first(name=None):
    fig1 = Figure()
    ax1 = fig1.subplots()
    ax1.plot(FirstY,Graph1)
    fig1.autofmt_xdate(rotation=45)
    buf = BytesIO()
    fig1.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("hyperpoop.html",name=f'data:image/png;base64,{data}')
@app.route("/Grocery-Store-Pharmacy")
def second():
    fig2 = Figure()
    ax2 = fig2.subplots()
    ax2.plot(SecondY,Graph2)
    buf = BytesIO()
    fig2.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("hyperpoop.html",name=f'data:image/png;base64,{data}')
@app.route("/Local-Business")
def third():
    fig3 = Figure()
    ax3 = fig3.subplots()
    ax3.plot(ThirdY,Graph3)
    buf = BytesIO()
    fig3.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("hyperpoop.html",name=f'data:image/png;base64,{data}')
@app.route("/US-Monthly-GDP")
def fourth():
    fig4 = Figure()
    ax4 = fig4.subplots()
    ax4.plot(FourthY,Graph4)
    fig4.autofmt_xdate(rotation=45)
    buf = BytesIO()
    fig4.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("hyperpoop.html",name=f'data:image/png;base64,{data}')
@app.route("/US-Unemployment-Rates")
def fifth():
    fig5 = Figure()
    ax5 = fig5.subplots()
    ax5.plot(FifthY,Graph5)
    fig5.autofmt_xdate(rotation=45)
    buf = BytesIO()
    fig5.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return render_template("hyperpoop.html",name=f'data:image/png;base64,{data}')
@app.route("/badrijani")
def badrijani():
    return '<img src="https://upload.wikimedia.org/wikipedia/commons/f/fb/Aubergine.jpg" alt="Italian Trulli">'
if (__name__=="__main__"):
    app.run()