from Basic_Gates import Logic_Gate_module as lgm
class SR_Latch:
    '''
    Docstring for SR_Latch
    This is the class for creating a SR latch. The users are expected to instantiate this class preferably using the name 'sr_latch'
    Here-:
    self.q_state= The output q of the SR latch
    self.qbar_state= The inverse of the output q of the SR latch
    s= The set input
    r= The reset input
    __init__ method= Initializes the sr latch object with a known state. q=0 and q'=1
    update(s,r) method= Updates the values of q and q' based on s and r
    output() method= Used for outputting the values of q and q'
    '''
def __init__(self):
    self.q_state=0
    self.qbar_state=1
def update(self,s,r):
    if (s==0):
        if(r==0):
            self.q_state=self.q_state
            self.qbar_state=self.qbar_state
        else:
            self.q_state=0
            self.qbar_state=1
    else:
        if(r==0):
            self.q_state=1
            self.qbar_state=0
        else:
            raise ValueError("s and r both cannot be 1 at the same time.")
def output(self):
    return self.q_state, self.qbar_state

class Gated_SR_Latch:
    '''
    Docstring for Gated_SR_Latch
    This is the class for creating a  gated SR latch. The users are expected to instantiate this class preferably using the name 'gated_sr_latch'
    Here-:
    self.q_state= The output q of the SR latch
    self.qbar_state= The inverse of the output q of the SR latch
    s= The set input
    r= The reset input
    e= The enable input
    __init__ method= Initializes the sr latch object with a known state. q=0 and q'=1. Sets e=0
    update(s,r,e) method= Updates the values of q and q' based on s and r depending on whether e is equal to 1 or not
    output() method= Used for outputting the values of q and q'
    '''
    def __init__(self):
        self.q_state=0
        self.qbar_state=1
        self.e=0
    def update(self,s,r,e):
        if(e==0):
            pass
        else:
            if (s==0):
                if(r==0):
                    self.q_state=self.q_state
                    self.qbar_state=self.qbar_state
                else:
                    self.q_state=0
                    self.qbar_state=1
            else:
                if(r==0):
                    self.q_state=1
                    self.qbar_state=0
                else:
                    raise ValueError("s and r both cannot be 1 at the same time.")
    def output(self):
        return self.q_state, self.qbar_state

class D_Latch:
    '''
    Docstring for D_Latch
    This is the class for creating a D latch. The users are expected to instantiate this class preferably using the name 'd_latch'
    Here-:
    self.q_state= The output q of the d latch
    self.qbar_state= The inverse of the output q of the d latch
    d=control input
    e= The enable input
    __init__ method= Initializes the d latch object with a known state. q=0 and q'=1. Sets e=0
    update(d,e) method= Updates the values of q and q' based on s and r depending on whether e is equal to 1 or not
    output() method= Used for outputting the values of q and q'
    '''
    def __init__(self):
        self.q_state=0
        self.qbar_state=1
        self.e=0
    def update(self,d,e):
        s=d
        r=lgm.Not_Class(s).output()
        
        if(e==0):
            pass
        else:
            if (s==0):
                if(r==1):
                    self.q_state=0
                    self.qbar_state=1
            else:
                if(r==0):
                    self.q_state=1
                    self.qbar_state=0
    def output(self):
        return self.q_state, self.qbar_state
        