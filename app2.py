
# git add .
# git commit -m "."
# git push

from flask import Flask,  render_template, request, session                    
import json, random, math
app = Flask(__name__)
app.secret_key='NewGame2022'
with open("/home/40504590/secondProject/json/question.json") as quest:
    data= json.load(quest)
bank=None
questionLevel=0
help50to50=None
rate=None
numberEasy=len(data["easy"])-1
numberMedium=len(data["medium"])-1
numberHard=len(data["hard"])-1
moneyPoint=0


@app.route('/')
def index():
    session['bank']=0
    session['help50to50']=1
    session['rate']=1
    session['question'] = 1
    ea=random.randint(0, numberHard)
    (session['a1'])=ea
    ma=random.randint(0, numberHard)
    (session['a2'])=ma
    ha=random.randint(0, numberHard)
    (session['a2'])=ha
   
    return render_template('first.html')


ea=random.randint(0, numberEasy)
ma=random.randint(0, numberMedium)
ha=random.randint(0, numberHard)  
eb=ea+1
ec=eb+1
ed=ec+1
ee=ed+1
if ea==numberEasy:
    eb=0
    ec=eb+1
    ed=ec+1
    ee=ed+1

if eb==numberEasy:
    ec=0
    ed=ec+1
    ee=ed+1

if ec==numberEasy:
    ed=0
    ee=ed+1

if ed==numberEasy:
    ee=0

mb=ma+1
mc=mb+1
md=mc+1
me=md+1
if ma==numberMedium:
    mb=0
    mc=mb+1
    md=mc+1
    me=md+1

if mb==numberMedium:
    mc=0
    md=mc+1
    me=md+1

if mc==numberMedium:
    md=0
    me=md+1

if md==numberMedium:
    me=0

hb=ha+1
hc=hb+1
hd=hc+1
he=hd+1
if ha==numberHard:
    hb=0
    hc=hb+1
    hd=hc+1
    he=hd+1

if hb==numberHard:
    hc=0
    hd=hc+1
    he=hd+1

if hc==numberHard:
    hd=0
    he=hd+1

if hd==numberHard:
    he=0

firstStage={
        "1":{
            "question":data['easy'][ea]['question'],
            "correct":data['easy'][ea]['correctAnswer'],
            "answer":data['easy'][ea]['answer'],
            "correctText":data['easy'][ea]['correct'],
            "help1":data['easy'][ea]['50/50'],
            "help2": data['easy'][ea]['procent'] 
            },
        "2":{
            "question":data['easy'][eb]['question'],
            "correct":data['easy'][eb]['correctAnswer'],
            "answer":data['easy'][eb]['answer'],
            "correctText":data['easy'][eb]['correct'],
            "help1":data['easy'][eb]['50/50'],
            "help2": data['easy'][eb]['procent'] 
            },
        "3":{
            "question":data['easy'][ec]['question'],
            "correct":data['easy'][ec]['correctAnswer'],
            "answer":data['easy'][ec]['answer'],
            "correctText":data['easy'][ec]['correct'],
            "help1":data['easy'][ec]['50/50'],
            "help2": data['easy'][ec]['procent'] 
            },
        "4":{
            "question":data['easy'][ed]['question'],
            "correct":data['easy'][ed]['correctAnswer'],
            "answer":data['easy'][ed]['answer'],
            "correctText":data['easy'][ed]['correct'],
            "help1":data['easy'][ed]['50/50'],
            "help2": data['easy'][ed]['procent'] 
            },
        "5":{
            "question":data['easy'][ee]['question'],
            "correct":data['easy'][ee]['correctAnswer'],
            "answer":data['easy'][ee]['answer'],
            "correctText":data['easy'][ee]['correct'],
            "help1":data['easy'][ee]['50/50'],
            "help2": data['easy'][ee]['procent'] 
            },
        "6":{
            "question":data['medium'][ma]['question'],
            "correct":data['medium'][ma]['correctAnswer'],
            "answer":data['medium'][ma]['answer'],
            "correctText":data['medium'][ma]['correct'],
            "help1":data['medium'][ma]['50/50'],
            "help2": data['medium'][ma]['procent'] 
            },
        "7":{
            "question":data['medium'][mb]['question'],
            "correct":data['medium'][mb]['correctAnswer'],
            "answer":data['medium'][mb]['answer'],
            "correctText":data['medium'][mb]['correct'],
            "help1":data['medium'][mb]['50/50'],
            "help2": data['medium'][mb]['procent'] 
            },
        "8":{
            "question":data['medium'][mc]['question'],
            "correct":data['medium'][mc]['correctAnswer'],
            "answer":data['medium'][mc]['answer'],
            "correctText":data['medium'][mc]['correct'],
            "help1":data['medium'][mc]['50/50'],
            "help2": data['medium'][mc]['procent'] 
            },
        "9":{
            "question":data['medium'][md]['question'],
            "correct":data['medium'][md]['correctAnswer'],
            "answer":data['medium'][md]['answer'],
            "correctText":data['medium'][md]['correct'],
            "help1":data['medium'][md]['50/50'],
            "help2": data['medium'][md]['procent'] 
            },
        "10":{
            "question":data['medium'][me]['question'],
            "correct":data['medium'][me]['correctAnswer'],
            "answer":data['medium'][me]['answer'],
            "correctText":data['medium'][me]['correct'],
            "help1":data['medium'][me]['50/50'],
            "help2": data['medium'][me]['procent'] 
            },
        "11":{
            "question":data['hard'][ha]['question'],
            "correct":data['hard'][ha]['correctAnswer'],
            "answer":data['hard'][ha]['answer'],
            "correctText":data['hard'][ha]['correct'],
            "help1":data['hard'][ha]['50/50'],
            "help2": data['hard'][ha]['procent'] 
            },
        "12":{
            "question":data['hard'][hb]['question'],
            "correct":data['hard'][hb]['correctAnswer'],
            "answer":data['hard'][hb]['answer'],
            "correctText":data['hard'][hb]['correct'],
            "help1":data['hard'][hb]['50/50'],
            "help2": data['hard'][hb]['procent'] 
            },
        "13":{
            "question":data['hard'][hc]['question'],
            "correct":data['hard'][hc]['correctAnswer'],
            "answer":data['hard'][hc]['answer'],
            "correctText":data['hard'][hc]['correct'],
            "help1":data['hard'][hc]['50/50'],
            "help2": data['hard'][hc]['procent'] 
            },
        "14":{
            "question":data['hard'][hd]['question'],
            "correct":data['hard'][hd]['correctAnswer'],
            "answer":data['hard'][hd]['answer'],
            "correctText":data['hard'][hd]['correct'],
            "help1":data['hard'][hd]['50/50'],
            "help2": data['hard'][hd]['procent'] 
            },
        "15":{
            "question":data['hard'][he]['question'],
            "correct":data['hard'][he]['correctAnswer'],
            "answer":data['hard'][he]['answer'],
            "correctText":data['hard'][he]['correct'],
            "help1":data['hard'][he]['50/50'],
            "help2": data['hard'][he]['procent'] 
            }
            }

@app.route('/create/')
def createUser():
    return render_template('createuser.html')


@app.route('/help2/')
def help_rate():
    p=int(session['question'])
    bank=int(session['bank'])
    help2=(session['rate'])
    help1=(session['help50to50'])
    if help2 == 1:
        help2=0
        session['rate']=help2
        answer1=firstStage[str(p)]["answer"][0]
        answer2=firstStage[str(p)]["answer"][1]
        answer3=firstStage[str(p)]["answer"][2]
        answer4=firstStage[str(p)]["answer"][3]
        rate1=firstStage[str(p)]["help2"][0]
        rate2=firstStage[str(p)]["help2"][1]
        rate3=firstStage[str(p)]["help2"][2]
        rate4=firstStage[str(p)]["help2"][3]
        return render_template('quest.html', question=firstStage[str(p)]["question"],  answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,rate1=rate1,rate2=rate2,rate3=rate3,rate4=rate4,p=p,bank=bank,ctrl1=0,ctrl2=0, ctrl3=0,ctrl4=1,cetrextra_info="You use answer rate")
    else:
        help2=0
        session['rate']=help2
        return render_template('quest.html', question=firstStage[str(p)]["question"], answer=firstStage[str(p)]["answer"],p=p,bank=bank,ctrl1=help1,ctrl2=help2,ctrl3=1,ctrl4=0, rate=0, cetrextra_info=" Sorry but you lose your rate chance. ")


@app.route('/help1/')
def help_50to50():
    helpFirst=int(session['help50to50'])
    p=int(session['question'])
    bank=int(session['bank'])
    help2=(session['rate'])
    help1=(session['help50to50'])
    if helpFirst == 1:
        helpFirst=0
        session['help50to50']=helpFirst
        return render_template('quest.html', question=firstStage[str(p)]["question"], answer=firstStage[str(p)]["help1"],  p=p,bank=bank,ctrl1=0,ctrl2=0,ctrl3=1,ctrl4=0, extra_info="You use 50/50" )
    else:
        helpFirst=0
        session['help50to50']=helpFirst
        return render_template('quest.html', question=firstStage[str(p)]["question"], answer=firstStage[str(p)]["answer"],p=p,bank=bank,ctrl1=0,ctrl2=0,ctrl3=1,ctrl4=0,extra_info="Soory but you lose your 50/50 chance")

@app.route('/quest/')
def question():
    p=int(session['question'])
    bank=int(session['bank'])
    help1=(session['help50to50'])
    help2=(session['rate'])

    answer= request.args.get(str('answer'), None)
    if answer is not None:
        correct=firstStage[str(p)]["correctText"]
        print(" A number p is "+ str(p)+" Check addresse "+ str(firstStage[str(p)])+" correct " + str(correct) + " answer " + str(answer))
        if str(answer) == str(correct):
            p+=1
            session['question']=p
            if bank==0:
                bank=250
                (session['bank'])=bank
            else:
                bank=bank*2
                session['bank']=bank
            if p > len(firstStage):
                return render_template('About.html')
            else:
                return render_template('quest.html', question=firstStage[str(p)]["question"], answer=firstStage[str(p)]["answer"], bank=bank, p=p,ctrl1=help1,ctrl2=help2,ctrl3=1,ctrl4=0, rate=0)
        else:
            if p>5:
                if p>10:
                    bank=100000
                    session['bank']=bank
                    return render_template('fail.html', answer=answer, question=firstStage[str(p)]["question"], bank=bank, correct=correct)

                bank=5000
                session['bank']=bank
                return render_template('fail.html', answer=answer, question=firstStage[str(p)]["question"], bank=bank, correct=correct)
            else:
                bank=0
                session['bank']=bank
                return render_template('fail.html', answer=answer, question=firstStage[str(p)]["question"], bank=bank, correct=correct)
    else:
        return render_template('quest.html', question=firstStage[str(p)]["question"], answer=firstStage[str(p)]["answer"],p=p,bank=bank,ctrl1=help1,ctrl2=help2,ctrl3=1,ctrl4=0, rate=0)


@app.route("/success/")
def success():
    return render_template('success.html')
    

if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)