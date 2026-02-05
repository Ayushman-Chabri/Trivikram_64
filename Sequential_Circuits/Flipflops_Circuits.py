from Basic_Gates import Logic_Gate_module as lgm
from Physics_Of_The_Project import Clock


class D_Flipflop:
    '''
    Docstring for D_Flipflop
    This is the class for creating a D flipflop. The users are expected to instantiate this class preferably using the name 'd_flipflop'
    Here-:
    self.q_state= The output q of the d latch
    self.qbar_state= The inverse of the output q of the d latch
    d=control input
    e= The enable input
    __init__ method= Initializes the d latch object with a known state. q=0 and q'=1. Sets e=0
    update(d,clk) method= Updates the values of q and q' based on s and r depending on whether clk is equal to 1 or not
    output() method= Used for outputting the values of q and q'
    '''
    def __init__(self):
        self.q_state=0
        self.qbar_state=1
        self.last_clock_stage=0
    def update(self,d,clk):
        s=0
        r=0
        rising_edge=(self.last_clock_stage==0)and(clk==1)
        if(rising_edge):
            s=d
            r=lgm.Not_Class(s).output()
            if (s==0):
                if(r==1):
                    self.q_state=0
                    self.qbar_state=1
            else:
                if(r==0):
                    self.q_state=1
                    self.qbar_state=0
            self.last_clock_stage=clk
    def output(self):
        return self.q_state, self.qbar_state