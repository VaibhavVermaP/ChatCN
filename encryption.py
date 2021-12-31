
import random
class RSA:
    def __init__(self,p=None,q=None):
        if p==None and q==None:
            rlist = '''
    101    103    107    109    113 
    127    131    137    139    149    151    157    163    167    173 
    179    181    191    193    197    199    211    223    227    229 
    233    239    241    251    257    263    269    271    277    281 
    283    293    307    311    313    317    331    337    347    349 
    353    359    367    373    379    383    389    397    401    409 
    419    421    431    433    439    443    449    457    461    463 
    467    479    487    491    499    503    509    521    523    541 
    547    557    563    569    571    577    587    593    599    601 
    607    613    617    619    631    641    643    647    653    659 
    661    673    677    683    691    701    709    719    727    733 
    739    743    751    757    761    769    773    787    797    809 
    811    821    823    827    829    839    853    857    859    863 
    877    881    883    887    907    911    919    929    937    941 
    947    953    967    971    977    983    991    997

            '''
            rlist = rlist.split()
            p = int(random.choice(rlist))
            q = int(random.choice(rlist))

        self.p = int(p)
        self.q = int(q)
        self.checkpq()

        self.n = self.p * self.q

        self.r= (self.p-1)*(self.q-1)

        self.gete()
        self.get_keys()

        

    def prime_check(self,a):
        if(a==2):
            return True
        elif((a<2) or ((a%2)==0)):
            return False
        elif(a>2):
            for i in range(2,a):
                if not(a%i):
                    return False
        return True
    
    def checkpq(self):
        check_p = self.prime_check(self.p)
        check_q = self.prime_check(self.q)
        while(((check_p==False)or(check_q==False))):
            self.p = int(input("Enter a prime number for p: "))
            self.q = int(input("Enter a prime number for q: "))
            check_p = self.prime_check(self.p)
            check_q = self.prime_check(self.q)

     
    def egcd(self,i):
        r = self.r
        while(r!=0):
            i,r=r,i%r

        return i
     
    def eugcd(self):
        for i in range(1,self.r):
            while(self.e!=0):
                self.a,self.b=self.r//self.e,self.r%self.e
                if(self.b!=0):
                    print("%d = %d*(%d) + %d"%(self.r,self.a,self.e,self.b))
                self.r=self.e
                self.e=self.b
                
     

    def eea(self,a,b):
        if(a%b==0):
            return(b,0,1)
        else:
            gcd,s,t = self.eea(b,a%b)
            s = s-((a//b) * t)
            return(gcd,t,s)
     
    
    def mult_inv(self):
        gcd,s,_=self.eea(self.e,self.r)
        if(gcd!=1):
            return None
        else:
            return s%self.r

    def gete(self): 
        for i in range(1,1000):
            if(self.egcd(i)==1):
                self.e=i

    def get_keys(self): 
        self.d = self.mult_inv()
        self.public = (self.e,self.n)
        self.private = (self.d,self.n)

        
    def encrypt(self,n_text,public = None):
        if public == None:
            public = self.public
        e,n=public
        cipher = [(ord(char) ** e) % n for char in n_text]
        return cipher
         
     
    

    def decrypt(self,c_text,private = None):
        
        if private == None:
            private = self.private
        d,n=private
        c_text=list(map(int,c_text.split(',')))
        plain = [chr((char ** d) % n) for char in c_text]
        return ''.join(plain)
        
     
