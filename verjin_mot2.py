

ss = '1*((2*2)*1112)*((3+4)/44)*2*(7*3)'
num_str_2 = ""
def bazmapatkum (st):
    for i in range(len(st)):    
        if st[i] == "*":
            ll = int(st[:i]) * int(st[i+1:])    
            print(ll)
            return ll 


def bajanum (st):
    for i in range(len(st)):
        if st[i] == "/":
            ll = int(st[:i]) / int(st[i+1:])
            print(ll)
            return ll

def gumarum(st):
    for i in range(len(st)):
        if st[i] == "+":
            ll = int(st[:i]) + int(st[i+1:])    
            print(ll)
            return ll

def hanum(st):
    for i in range(len(st)):
        if st[i] == "-":
            ll = int(st[:i])-int(st[i+1:])
            print(ll)
            return ll

def decode(sout,index1,index2):
    
    st = sout[index1+1:index2]
    print(st,",es st na")
    for i in st:
        
        if i == "*": 
            return bazmapatkum(st)
        elif i == "/":
            return bajanum(st)
        elif i == "+":
            return gumarum(st)
        elif i == "-":
            return hanum(st)
        else:
            
            print("decode @ chashxatec")


def esim (ss):
     
    index2 = ss.find(")")
    

    def nerdrvac_esim(sout,index2):
        for j in range(len(sout[:index2])):
            if sout[j]== "(":
                index1 = j
            
        
        out_dec = str(decode(sout,index1,index2))
        print(out_dec,"es out_decna")
        sout = str(sout[:index1])+out_dec+str(sout[index2+1:])
        print(sout,",es soutna")
        if sout.find("(") == -1:
            global num_str_2
            num_str_2 = sout
            return sout
        index2 = sout.find(")")
        nerdrvac_esim(sout,index2)
        
    return nerdrvac_esim(ss,index2) 


print(esim(ss),"ss i skzbnaka ")
print(num_str_2)#dzeeeeeeeec

                    