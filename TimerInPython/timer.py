import time
import os

def countdown(WorkTime,RestTime,Iteration):
    FullTime=WorkTime*Iteration
    print('Timer started:','\n')

    while Iteration:
        workTime=WorkTime
        restTime=RestTime
        
        while workTime:
            mins, secs = divmod(FullTime, 60)
            timer1 = '{:02d}:{:02d}'.format(mins, secs)
            WorkMins, WorkSecs = divmod(workTime, 60)
            timer2 = '{:02d}:{:02d}'.format(WorkMins, WorkSecs)
            print('Work time letf :',timer1,'\t','remaining iteration ('+Iteration+') remaining time to rest :',timer2, end="\r")
            time.sleep(1)
            FullTime -= 1
            workTime -= 1     
            if(workTime==0):               
                os.startfile("Alarm1.mp3")

        while restTime:
            ReskMins, RestSecs = divmod(restTime, 60)
            timer2 = '{:02d}:{:02d}'.format(ReskMins, RestSecs)
            print('Rest time lift :',timer2,'                                                             ', end="\r")
            time.sleep(1)
            restTime -= 1
            if(restTime==0):
                os.startfile("RestTimeAlarm.mp3")
                
        if(Iteration==1):
            print('Timer IS Over , Have Agood Day <3','                                                             ', end="\r")       
              
        Iteration-=1
    
    print('\n'+('='* 40),'<=====>',('=' * 40),'\n') 


print('\n'+('=' * 31),'<> Intermittent Alarm <>','=' * 31) 
WorkTime=float(input('pls enter Work time in minutes : '))
WorkTime*=60
RestTime=float(input('pls enter rest time in minutes : '))
RestTime*=60
Iteration=int(input('pls enter iteration num: '))
print('=' * 40,'<=====>','=' * 40) 

countdown(int (WorkTime),int(RestTime),int(Iteration))