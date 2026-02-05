import Flipflops_Circuits as ff
from Registers_Circuits import Register_64
from Combinational_Circuits import Adder_Circuits as ac


class Program_Counter:
    '''
    Docstring for Program_Counter
    '''
    def __init__(self):
        self.reg=Register_64()
        for i in range(0,64):
            self.reg.reg_list[i].q_state=0
            self.reg.reg_list[i].qbar_state=1
            self.last_clock_stage=0
    def output(self,clk):
        rising_edge=(self.last_clock_stage==0)and(clk==1)
        if(rising_edge):
            output= self.reg.output_list
            Program_Counter.increment(output)
        self.last_clock_stage=clk
        
    def increment(self,clk,in1_vec=[0]*64,in2_vec=[0]*61 +[1]+[0]+[0]):
        in1_vec=self.reg.output_list
        rca=ac.RippleCarry_Adder(in1_vec,in2_vec,0)
        self.reg.update(rca.output_vec,1,clk)
        
    
        
    