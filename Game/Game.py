import pandas as pd
import os
from tkinter import *
from tkinter import ttk   
import random as rd
import time
import math
import sys
import warnings
import numpy as np
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

df=pd.read_csv('Users.csv')
PK=pd.read_csv('Pokemon.csv')
MV=pd.read_csv('Moves.csv')
SE=pd.read_csv('Super effective.csv')
N=pd.read_csv('Nature.csv')

#clear screen
def clear():
    os.system('cls')

def typed(words):
    for char in words:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

#health
def do_health(ch,h,you):
    dc = int(h/20)            # Get the number to divide by to convert ch to dashes (being 10)
    cd = int(ch/dc)              # Convert ch to dash count: 80/10 => 8 dashes
    rh = 20 - cd       # Get the ch remaining to fill as space => 12 spaces

    hds = '-' * cd                  # Convert 8 to 8 dashes as a string:   "--------"
    rhds = ' ' * rh             # Convert 12 to 12 spaces as a string: "            "
    percent = str(int((ch/h)*100)) + "%"     # Get the percent as a whole number:   40%
    if you==False:
        if ch>0:
            print("\t\t\t\t\t\t\t\t|" +hds + rhds + "| "+percent)  # Print out textbased healthbar
        elif ch<0:
            print("\t\t\t\t\t\t\t\t|" +hds + rhds + "| "+'0%')
    elif you==True:
        if ch>0:
            print("|" +hds + rhds + "| "+percent)
        elif ch<0:
            print("|" +hds + rhds + "| "+'0%')

#game play
def game():
    if ps=='1v1':
        global move
        non=['Nidoran♀','Nidoran♂','Meowstic♀','Indeedee♀','Meowstic♂','Indeedee♂']
        if not oppk[0] in non or PK['legendary'].loc[PK['Pokemon']==oppk[0]]=='TRUE':
            opgen=rd.randint(0,1)
            if opgen==0:
                opgen='\u2640'
            elif opgen==1:
                opgen='\u2642'
        else:
            opgen=''
        if not pp in non or PK['legendary'].loc[PK['Pokemon']==pp]=='TRUE':
            plgen=rd.randint(0,1)
            if plgen==0:
                plgen='\u2640'
            elif plgen==1:
                plgen='\u2642'
        else:
            plgen=''
        stats(oppk[0])
        oph=h_p
        opch=oph
        opsp=sp
        opatk=atk
        opde=de
        opsa=sa
        opsd=sd
            
        stats(pp)
        plh=h_p
        plch=plh
        plsp=sp
        platk=atk
        plde=de
        plsa=sa
        plsd=sd
        op_status=''
        pl_status=''
        pl_moves=[]
        op_moves=[]
        m_p=MV['move'].loc[MV['type']==PK['Type I'].loc[PK['Pokemon']==pp].tolist()[0]].tolist()
        _=MV['move'].loc[MV['type']==PK['Type II'].loc[PK['Pokemon']==pp].tolist()[0]].tolist()
        m_p=m_p+_
        m_o=MV['move'].loc[MV['type']==PK['Type I'].loc[PK['Pokemon']==oppk[0]].tolist()[0]].tolist()
        __=MV['move'].loc[MV['type']==PK['Type II'].loc[PK['Pokemon']==oppk[0]].tolist()[0]].tolist()
        m_o=m_o+__
        for i in range(0,4):
            pl_moves.append(m_p[rd.randint(0,len(m_p)-1)])
            op_moves.append(m_o[rd.randint(0,len(m_o)-1)])
        opstatmod=['0','0','0','0','0','0','0']
        plstatmod=['0','0','0','0','0','0','0']
        while True:
            clear()
            print('\t\t\t\t\t\t\t\t '+oppk[0]+opgen+op_status)
            do_health(opch,oph,False)
            print(' '+pp+plgen+pl_status)
            do_health(plch,plh,True)
            if opch<=0 or plch<=0:
                    break

            print('1.'+pl_moves[0]+'\n2.'+pl_moves[1]+'\n3.'+pl_moves[2]+'\n4.'+pl_moves[3])
            kill=input()
            if kill=='1':
                move_pl=pl_moves[0]
            elif kill=='2':
                move_pl=pl_moves[1]
            elif kill=='3':
                move_pl=pl_moves[2]
            elif kill=='4':
                move_pl=pl_moves[3]

            if plsp>=opsp:
                typed('\n'+pp+' used '+move_pl+'.')
                if rd.randint(1,100)<=MV['accuracy'].loc[MV['move']==move_pl].tolist()[0]*100:
                    run('r',move_pl)
                    opch-=damage
                elif str(MV['accuracy'].loc[MV['move']==move_pl].tolist()[0])=='nan':
                    run('r',move_pl)
                    opch-=damage
                else:
                    typed('\nThe attack missed.')

                clear()
                print('\t\t\t\t\t\t\t\t '+oppk[0]+opgen+op_status)
                do_health(opch,oph,False)
                print(' '+pp+plgen+pl_status)
                do_health(plch,plh,True)

                if opch<=0:
                    break

                move_op=op_moves[rd.randint(0,3)]
                typed('\n'+oppk[0]+' used '+move_op+'.')
                if rd.randint(1,100)<=MV['accuracy'].loc[MV['move']==move_op].tolist()[0]*100:
                    run('r',move_op)
                    plch-=damage
                elif str(MV['accuracy'].loc[MV['move']==move_op].tolist()[0])=='nan':
                    run('r',move_op)
                    plch-=damage
                else:
                    typed('\nThe attack missed.')

            elif opsp>=plsp:
                move_op=op_moves[rd.randint(0,3)]
                typed('\n'+oppk[0]+' used '+move_op+'.')
                if rd.randint(1,100)<=MV['accuracy'].loc[MV['move']==move_op].tolist()[0]*100:
                    run('r',move_op)
                    plch-=damage
                elif str(MV['accuracy'].loc[MV['move']==move_op].tolist()[0])=='nan':
                    run('r',move_op)
                    plch-=damage
                else:
                    typed('\nThe attack missed.')
                
                clear()
                print('\t\t\t\t\t\t\t\t '+oppk[0]+opgen+op_status)
                do_health(opch,oph,False)
                print(' '+pp+plgen+pl_status)
                do_health(plch,plh,True)

                if plch<=0:
                    break
                
                typed('\n'+pp+' used '+move_pl+'.')
                if rd.randint(1,100)<=MV['accuracy'].loc[MV['move']==move_pl].tolist()[0]*100:
                    run('r',move_pl)
                    opch-=damage
                elif str(MV['accuracy'].loc[MV['move']==move_pl].tolist()[0])=='nan':
                    run('r',move_pl)
                    opch-=damage
                else:
                    typed('\nThe attack missed.')
                
        if plch>0:
            typed("\nOpponent's "+oppk[0]+' fainted.')
            typed('\n\t\t\t\t\t\tYou Won !!!')
            df['W'].loc[df.index[df['User']==un]]=df['W'].loc[df.index[df['User']==un]].tolist()[0]+1
            df.to_csv('Users.csv',index=False)
        if opch>0:
            typed("\nYour "+pp+' fainted.')
            typed('\n\t\t\t\t\t\tYou Lose !!!')
            df['L'].loc[df.index[df['User']==un]]=df['L'].loc[df.index[df['User']==un]].tolist()[0]+1
            df.to_csv('Users.csv',index=False)
        time.sleep(3)

def stats(pkmn):
    pk_i=PK.index[PK['Pokemon']==pkmn]
    pk=PK['Pokemon'].loc[pk_i]
    #LVL
    lvl=50
    #BSs
    base=[]
    for i in ['HP','Atk','Def','SpA','SpD','Spe']:
        base.append(PK[['HP','Atk','Def','SpA','SpD','Spe']].loc[pk_i][i])
    #IVs
    IV=[]
    for i in ['HP','Atk','Def','SpA','SpD','Spe']:
        iv=rd.randint(0,31)
        IV.append(iv)
    #EVs
    EV=[]
    for i in ['HP','Atk','Def','SpA','SpD','Spe']:
        if sum(EV)<510:
            ev=rd.randint(0,252)
            EV.append(ev)
        if sum(EV)>510:
            EV.remove(EV[-1])
    EV.append(510-sum(EV))
    #Natue
    n=N['Nature'].tolist()
    _N_=N[['Atk','Def','SpA','SpD','Spe']].loc[N.index[N['Nature']==n[rd.randint(0,24)]]]

    global h_p,atk,de,sa,sd,sp
    #HP
    h_p=math.floor(1/2*(2*int(base[0])+IV[0]+math.floor(EV[0]/4)))+lvl+10

    stats=[h_p]
    #Others
    for i in ['Atk','Def','SpA','SpD','Spe']:
        stat=math.floor((math.floor(1/2*(2*int(base[0])+IV[0]+math.floor(EV[0]/4)))+5)*_N_[i])
        stats.append(stat)
    h_p=stats[0]
    atk=stats[1]
    de=stats[2]
    sa=stats[3]
    sd=stats[4]
    sp=stats[5]

def run(lr,move):
    #index
    m_i=MV.index[MV['move']==move]
    op_i=PK.index[PK['Pokemon']==oppk[0]]
    pl_i=PK.index[PK['Pokemon']==pp]
    global damage

    stats(pp)
    #A/D of player pokemon
    HP_pl=float(h_p)
    D_pl=float(de)
    A_pl=float(atk)
    SA_pl=float(sa)
    SD_pl=float(sd)

    stats(oppk[0])
    #A/D of opponent pokemon
    HP_op=float(h_p)
    D_op=float(de)
    A_op=float(atk)
    SA_op=float(sa)
    SD_op=float(sd)
    
    #CRITICAL input
    if rd.randint(0,10000)<=625:
        crit=1.5
    else:
        crit=1

    #POWER input
    power=float(MV['power'].loc[m_i])

    #RANDOM input
    random=float(rd.randint(85,101)/100)

    #STAB input
    if lr=='r':
        if MV['type'].loc[m_i].tolist()[0]==PK['Type I'].loc[op_i].tolist()[0] or MV['type'].loc[m_i].tolist()[0]==PK['Type II'].loc[op_i].tolist()[0]:
            stab=1.5
        else:
            stab=1
    else:
        if MV['type'].loc[m_i].tolist()[0]==PK['Type I'].loc[pl_i].tolist()[0] or MV['type'].loc[m_i].tolist()[0]==PK['Type II'].loc[pl_i].tolist()[0]:
            stab=1.5
        else:
            stab=1
                
    #TYPE input
    SE_t_i=0
    while not (SE['types'].loc[SE_t_i]==MV['type'].loc[m_i]).tolist()[0]==True:
        SE_t_i+=1
    if lr=='r':
        if str(PK['Type II'].loc[pl_i].tolist()[0])=='nan':
            Type=float(SE[PK['Type I'].loc[pl_i]].loc[SE_t_i].tolist()[0])
        else:
            Type=float(SE[PK['Type I'].loc[pl_i]].loc[SE_t_i].tolist()[0]*SE[PK['Type II'].loc[pl_i]].loc[SE_t_i].tolist()[0])
    else:
        if str(PK['Type II'].loc[op_i].tolist()[0])=='nan':
            Type=float(SE[PK['Type I'].loc[op_i]].loc[SE_t_i].tolist()[0])
        else:
            Type=float(SE[PK['Type I'].loc[op_i]].loc[SE_t_i].tolist()[0]*SE[PK['Type II'].loc[op_i]].loc[SE_t_i].tolist()[0])
            
    #DAMAGE
    if (MV['category'].loc[m_i]=='STATUS').tolist()[0]==True:
        damage=0

    elif str(MV['power'].loc[m_i].tolist()[0])=='nan':
        damage=0

    else:
        if (MV['category'].loc[m_i]=='PHYSICAL').tolist()[0]==True:
            if lr=='r':
                damage=(((40*power*(A_op/D_pl))/50)+2)*crit*stab*Type*random
            else:
                damage=(((40*power*(A_pl/D_op))/50)+2)*crit*stab*Type*random
        elif (MV['category'].loc[m_i]=='SPECIAL').tolist()[0]==True:
            if lr=='r':
                damage=(((40*power*(SA_op/SD_pl))/50)+2)*crit*stab*Type*random
            else:
                damage=(((40*power*(SA_pl/SD_op))/50)+2)*crit*stab*Type*random
        else:
            damage=round(damage)

def se(lr,move):
    if lr=='r':
        _i=PK.index[PK['Pokemon']==oppk[0]]
    elif lr=='l':
        _i=PK.index[PK['Pokemon']==pp]

    if str(PK['Type II'].loc[_i].tolist()[0])=='nan':
        dam=float(SE[PK['Type I'].loc[_i].tolist()[0]].loc[MV['type'].loc[MV['move']==move].tolist()[0]].tolist()[0])
        if dam>1.0:
            typed(' The attack was super effective!')
        elif dam<1.0 and dam>0:
            typed(' The attack was resisted.')
        elif dam==0.0:
            typed(' The attack delt no damage.')
    else:
        dam=float(SE[PK['Type II'].loc[_i].tolist()[0]].loc[MV['type'].loc[MV['move']==move].tolist()[0]].tolist()[0])*float(SE[PK['Type II'].loc[_i].tolist()[0]].loc[MV['type'].loc[MV['move']==move].tolist()[0]].tolist()[0])
        if dam>1.0:
            typed(' The attack was super effective!')
        elif dam<1.0 and dam>0:
            typed(' The attack was resisted.')
        elif dam==0.0:
            typed(' The attack delt no damage.')

def pl():
    clear()
    root = Tk()   
    root.geometry("300x50")    
    frame = Frame(root)    
    frame.pack()

    global oppk
    oppk=[]
    for i in range(0,6):
        oppk.append(PK['Pokemon'].loc[rd.randint(0,PK.shape[0])])
    print('Opponent is sending out '+oppk[0])
    
    L_pokemon = []
    for i in range(0,PK.shape[0]):
        L_pokemon.append(PK['Pokemon'].loc[i])

    global C_bt,C_pl
    C_pl= ttk.Combobox(frame, width = 20, values = L_pokemon)
    C_pl.set("Your pokemon...")
    C_pl.grid(column = 0, row = 0)

    C_bt= ttk.Combobox(frame, width = 20, values = ['1v1','3v3','6v6'])
    C_bt.set("Your battle settings...")
    C_bt.grid(column = 1, row = 0)

    button1 = Button(frame, width = 10, text = "Play", command=root.destroy)
    button1.grid(column = 1, row = 1)
    
    button1 = Button(frame, width = 10, text = "Set", command=Set)
    button1.grid(column = 0, row = 1)

    root.title('Play settings')
    root.mainloop()

    try:
        game()
    except NameError:
        print('Set value are invalid.')
        input()
        pl()
        

def Set():
    global pp,ps
    ps=C_bt.get()
    pp=C_pl.get()
    print(ps,pp)

#Login Function
def login():
        clear()
        ls=input('Login/Signup (s/l): ')
        clear()
        if ls=='s':
            un=input('Enter Username: ')
            p=input('Create Password: ')
            n=df.shape[0]
            df.at[n]=[un,p,'F',0,0,0] 
            df['Last']='F'
            df['Last'].loc[df.index[df['User']==un]]='T'
            df.to_csv('Users.csv',index=False)
        elif ls=='l':
            while True:
                un=input('Enter Username: ')
                p=input('Enter Password: ')
                if un in df['User'].tolist() and df['Password'].loc[df.index[df['User']==un]].tolist()[0]==p:
                    df['Last']='F'
                    df['Last'].loc[df.index[df['User']==un]]='T'
                    df.to_csv('Users.csv',index=False)
                    break
                else:
                    clear()
                    print('Invalid username or password')
        else:
            login()
while True:
    df=pd.read_csv('Users.csv')
    if 'T' in df['Last'].tolist():
        un=df['User'].loc[df['Last']=='T'].tolist()[0]
    else:
        login()
    clear()
    print('\t\t     Welcome '+un+' !!')
    print('---'*20)
    print('\t\t  WHAT YOU WANT TO DO?')
    print('---'*20)
    print('1.Play Game?')
    print('2.Login/Signup with diffent Username')
    print('3.Win-Lose Comparasion of Every Player')
    print('4.Your Win-Lose ratio.')
    print('5.Show the Base Statistic of specipic pokemon')
    print('6.Compare Base Stats of pokemons.')
    print('7.Add records in the databases.')
    print('8.Delete records from the databases.')
    print('9.Clear my player data. <your ID will be intact>')
    print('10.Delete ID...')
    choise=input('\n=>')
    if choise=='1':
        pl()
    if choise=='2':
        login()
    if choise=='3':
        users = df['User'].tolist()
        win = df['W'].tolist()
        los = df['L'].tolist()
        x=np.arange(len(users))
        fig, ax = plt.subplots()
        rects1 = ax.bar(x-0.1, win, 0.2, label='Wins')
        rects2 = ax.bar(x+0.1, los, 0.2, label='Loses')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_title('Win-Lose Comparasion of Every Player')
        ax.set_xticks(x)
        ax.set_xticklabels(users)
        ax.legend()

        ax.bar_label(rects1, padding=1)
        ax.bar_label(rects2, padding=1)

        fig.tight_layout()

        plt.show()
    if choise=='4':
        w_l = 'Wins','Loses'
        ratio = df['W'].loc[df['User']==un]
        r_=df['L'].loc[df['User']==un]
        ratio = (ratio.append(r_)).tolist()
        fig1, ax1 = plt.subplots()
        ax1.pie(ratio, labels=w_l, shadow=True)
        ax1.axis('equal')
        plt.legend()
        plt.show()

    if choise=='5':
        clear()
        root = Tk()   
        root.geometry("300x50")    
        frame = Frame(root)    
        frame.pack()

        def Select():
            clear()
            print(PK[['Pokemon','HP','Atk','Def','SpA','SpD','Spe','Total']].loc[PK['Pokemon']==C_pl.get()].to_string(index=False))

        L_pokemon = []
        for i in range(0,PK.shape[0]):
            L_pokemon.append(PK['Pokemon'].loc[i])
        
        C_pl= ttk.Combobox(frame, width = 20, values = L_pokemon)
        C_pl.set("Choose pokemon...")
        C_pl.grid(column = 0, row = 0)

        button1 = Button(frame, width = 10, text = "Select", command=Select)
        button1.grid(column = 0, row = 1)

        root.title('Search Settings')
        root.mainloop()

    if choise=='6':
        clear()
        root = Tk()   
        root.geometry("300x50")    
        frame = Frame(root)    
        frame.pack()

        def Plot(stat,color,label):
            x=np.array([*range(0,PK.shape[0],1)])+1
            y=PK[stat].tolist()
            plt.plot(x,y,'o',color= color,markersize=3, linewidth=4)
            plt.axes().plot(x,y)
            plt.xlabel('National Index of Pokemons')
            plt.ylabel(label)
            plt.show()
        def Showplt():
            if C_st.get()=='HP':
                Plot('HP','green','Health Points')
            if C_st.get()=='Attack':
                Plot('Atk','red','Attack')
            if C_st.get()=='Defence':
                Plot('Def','blue','Defence')
            if C_st.get()=='Sp.Attack':
                Plot('SpA','orange','Special Attack')
            if C_st.get()=='Sp.Defence':
                Plot('SpD','cyan','Special Defence')
            if C_st.get()=='Speed':
                Plot('Spe','yellow','Speed')
            if C_st.get()=='BSTotal':
                Plot('Total','black','Base Stat Total')
            
        L_stats = ['HP','Attack','Defence','Sp.Attack','Sp.Defence','Speed','BSTotal']
        
        C_st= ttk.Combobox(frame, width = 20, values = L_stats)
        C_st.set("Choose Statistic...")
        C_st.grid(column = 0, row = 0)

        button1 = Button(frame, width = 10, text = "Show", command=Showplt)
        button1.grid(column = 0, row = 1)

        root.title('Plot Settings')
        root.mainloop()

    if choise=='7':
        name=input("Enter Pokemon's name: ")
        nat=input("What's the National index: ")
        typei=input('Primary type of '+name+' :')
        typeii=input('Secondary type of '+name+' :')
        hp=input('Enter Health Points: ')
        a=input('Enter Attack: ')
        d=input('Enter Defence: ')
        sa=input('Enter Special Attack: ')
        sd=input('Enter Special Defence: ')
        sp=input('Enter Speed: ')
        legend=input('Is it '+name+' (y/n):')
        if legend=='y':
            legend=True
        elif legend=='n':
            legend=False
        n=PK.shape[0]
        PK.at[n]=[nat,name,0,hp,a,d,sa,sd,sp,'',legend]
        PK.to_csv('Pokemon.csv',index=False)
        typed('Done...')

    if choise=='8':
        while True:
            clear()
            delete=input("Delete record of which Pokemon?: ")
            if delete in PK['Pokemon'].tolist()[0]:
                PK.drop([PK.index[PK['Pokemon']==delete]]).to_csv('Pokemon.csv',index=False)
                typed('Done...')
                break
            elif not delete in PK['Pokemon'].tolist()[0]:
                print('Pokemon name might be wrong...')
                time.sleep(1.3)
        
    if choise=='9':
        if input('Your score is going to be deleted. Are you sure? (y/n): ')=='y':
            df['W'].loc[df.index[df['User']==un]]=0
            df['L'].loc[df.index[df['User']==un]]=0
            df.to_csv('Users.csv',index=False)
            typed('Done...')

    if choise=='10':
        clear()
        if input('Are you sure you want to delete your ID..? (y/n): ')=='y':
            un=df['User'].loc[df['Last']=='T'].tolist()[0]
            df.drop([df.index[df['User']==un].tolist()[0]]).to_csv('Users.csv',index=False)
            typed('Done...')
            time.sleep(1.5)
