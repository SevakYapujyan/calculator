


# # ss = "1+21-23*14/15+14+22+43*2*11*32+1*10"
# #ss = '1*((12*21/4+22+11)*12*2*2)*((3*4)*44)*2*(7*3)'
# # ss = "16/((8/(2*2))*(8/(4/(2*2))))"
# #ss = input("------------------------------->>>"")
# ss = input("------------------------>>>>>>>>>>>>")
((2*4)+(6/2)+(2-(8-10)*(12+(14/(16+18)))))-20


def hanum(sts):
    ss = sts
    index1 = 0
    operand = ss.find("-")

    index2 = len(ss)-1



    print(operand,"operandna hanumi")
    if operand != 0:
        ll_index2 = []
        for i in range(operand+2,len(ss)):
            if ss[i] =="*":
                ll_index2.append(i)
            elif ss[i] =="/":
                ll_index2.append(i)
            elif ss[i] =="+":
                ll_index2.append(i)
            elif ss[i] =="-":
                ll_index2.append(i)
        if ll_index2 != []:
            ll_index2.sort()
            print(ll_index2)
            index2 = ll_index2[0] 
            index2 = index2-1
        else:
            index2 = len(ss)-1
        print(index1,"1 kna")
        print(index2,"2 na")
        a = str(int(ss[index1:operand]) - int(ss[operand+1:index2+1]))
        print(a,"es ana")
        ss = ss[:index1] + a + ss[index2+1:]
        print(ss)

        if ss.find("-") != -1:
            print(ss," esi ss na hanumi mej fraluc")
            hanum(ss)

    
    print(ss,",ss na hanum ic durs galuc")###############################
    return ss
        




def gumarum(sts):
    ss = sts
    index1 = 0
    operand = ss.find("+")
    print(operand,"operandna 1 dirqum printi")

    for i in range(len(ss[:operand])):
        
        if ss[i] =="-":
            index1 = i
    
    index2 = len(ss)-1
    
    print(operand,"operandna")
    ll_index2 = []
    for i in range(operand+2,len(ss)):
        if ss[i] =="*":
            ll_index2.append(i)
        elif ss[i] =="/":
            ll_index2.append(i)
        elif ss[i] =="+":
            ll_index2.append(i)
        elif ss[i] =="-":
            ll_index2.append(i)
    if ll_index2 != []:
        ll_index2.sort()
        print(ll_index2)
        index2 = ll_index2[0] 
        index2 = index2-1
    else:
        index2 = len(ss)-1
    print(index1,"1 kna")
    print(index2,"2 na")
    a = str(int(ss[index1:operand]) + int(ss[operand+1:index2+1]))
    print(a,"es ana")
    ss = ss[:index1] + a + ss[index2+1:]
    print(ss,"ss na gumarumi mej a i tak")

    if ss.find("+") != -1:
        print(ss," esi ss na gumarum mej fraluc")
        gumarum(ss)

    print(ss,",ss na gumarum iiiiic durs galuc xxxxx")
    return ss








def bajanum(sts):
    ss = sts
    index1 = 0
    operand = ss.find("/")


    for i in range(len(ss[:operand])):

        if ss[i] =="+":
            index1 = i
        elif ss[i] =="-":
            index1 = i

    index2 = len(ss)-1
    
    print(operand,"operandna")
    ll_index2 = []
    for i in range(operand+2,len(ss)):
        if ss[i] =="*":
            ll_index2.append(i)
        elif ss[i] =="/":
            ll_index2.append(i)
        elif ss[i] =="+":
            ll_index2.append(i)
        elif ss[i] =="-":
            ll_index2.append(i)
    if ll_index2 != []:
        ll_index2.sort()
        print(ll_index2)
        index2 = ll_index2[0] 
        index2 = index2-1
    else:
        index2 = len(ss)-1
    print(index1,"1 kna")
    print(index2,"2 na")
    a = str(int(ss[index1:operand])//int(ss[operand+1:index2+1]))
    print(a,"es ana")
    ss = ss[:index1] + a + ss[index2+1:]
    print(ss)

    if ss.find("/") != -1:
        print(ss," esi ss na baji mej fraluc")
        bajanum(ss)


    print(ss,",ss na baj ic durs galuc")
    return ss
        



def bazmapatkum(ss):

    index1 = 0
        
    operand = ss.find("*")
    for i in range(len(ss[:operand])):
        

        if ss[i] =="+":
            index1 = i
        elif ss[i] =="-":
            index1 = i
        elif ss[i] == "/":
            index1 = i
    
    index2 = len(ss)-1
    
    print(operand,"operandna")
    ll_index2 = []
    for i in range(operand+2,len(ss)):
        if ss[i] =="*":
            ll_index2.append(i)
        elif ss[i] =="/":
            ll_index2.append(i)
        elif ss[i] =="+":
            ll_index2.append(i)
        elif ss[i] =="-":
            ll_index2.append(i)
    if ll_index2 != []:
        ll_index2.sort()
        print(ll_index2)
        index2 = ll_index2[0] 
        index2 = index2-1
    else:
        index2 = len(ss)-1
    print(index1,"1 kna")
    print(index2,"2 na")
    a = str(int(ss[index1:operand])*int(ss[operand+1:index2+1]))
    print(a,"es ana")
    ss = ss[:index1] + a + ss[index2+1:]
    print(ss)

    if ss.find("*") != -1:
        print(ss," esi ss na bazi mej fraluc")
        baz_ss = bazmapatkum(ss)
        a == True
    

    print(ss,"sa ss na bazmapatkumic durs galuc")
    return ss


def karavarich(sts):
    ss = sts
    if ss[1:].find("*") !=-1:
        print(ss,"ss @ bazin tal karavarichum ")
        ret_baz = bazmapatkum(ss)
        ss = ret_baz
        print(ss,"ret_baz")
    if ss[1:].find("/") !=-1:
        print(ss,"ss na baj in trvox karavarichum")
        ret_baj = bajanum(ss)
        ss = ret_baj
        print(ss,"ret_baj na ")
    if ss[1:].find("+") !=-1:
        ret_gum = gumarum(ss)
        ss = ret_gum
        print(ss,"ret_gumna")
    if ss[1:].find("-") !=-1:
        ret_han = hanum(ss)
        ss = ret_han
        print(ss,"ret_han")
    
    print(ss,"ss na karavarichi veradarcnox")
    return ss





def esim (ss):

    def go_to(sout):
   
        aa = karavarich(sout)
        print("------>>>>>>>>>>-------------------->>>>>>>>>>>>>>>",aa)
        


    index2 = ss.find(")")
    if index2 == -1:
        go_to(ss)
        
      

    def nerdrvac_esim(sout,index2):
        for j in range(len(sout[:index2])):
            if sout[j]== "(":
                index1 = j

        sts = sout[index1+1:index2]
        print(sts,",sts @ vor@ trvuma karavarichin")


        veradarc_1 = karavarich(sts)

        print(veradarc_1,",esi veradarcna")
        
        
        sout = str(sout[:index1]) + veradarc_1 + str(sout[index2+1:])

        print(sout,"sa sout na ")
        if sout.find("(") == -1:
            if sout.find("*") !=-1:
                go_to(sout)
            elif sout.find("/") !=-1:
                go_to(sout)
            elif sout.find("+") !=-1:
                go_to(sout)
            elif sout.find("-") !=-1:
                go_to(sout)
            else:
                print("----------------------->>>>>>>>>>>>",sout)

        elif sout.find(")") != -1:

            index2 = sout.find(")")
            nerdrvac_esim(sout,index2)


    return nerdrvac_esim(ss,index2) 
ss = input("------------------------>>>>>>>>>>>>:")


print(esim(ss))




                                                            




