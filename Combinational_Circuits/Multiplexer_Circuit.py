from Basic_Gates import Logic_Gate_module as lgm
class Multiplexer2x1:
    '''
    Docstring for Multiplexer
    This is the class for the 2x1 multiplexer(MUX) circuit. Users are expected to instantiate this class preferably with the name 'mux2x1'
    input_vec=The vector of width 2 used for providing the input
    sel=The select line
    out= The output
    '''
    def __init__(self, input_vec,sel):
        if sel==0:
            self.out=input_vec[0]
        elif sel==1:
            self.out=input_vec[1]
    def output(self):
        return self.out
    
class Multiplexer4x1:
    '''
    Docstring for Multiplexer
    This is the class for the 4x1 multiplexer(MUX) circuit. Users are expected to instantiate this class preferably with the name 'mux4x1'
    input_vec=The vector of width 4 used for providing the input
    sel_vec=The select line vector
    out= The output
    '''
    def __init__(self, input_vec,sel_vec):
        if sel_vec[0]==0:
            if sel_vec[1]==0:
                self.out=input_vec[0]
            elif sel_vec[1]==1:
                self.out=input_vec[1]
        elif sel_vec[0]==1:
            if sel_vec[1]==0:
                self.out=input_vec[2]
            elif sel_vec[1]==1:
                self.out=input_vec[3]
    def output(self):
        return self.out

class Multiplexer8x1:
    '''
    Docstring for Multiplexer
    This is the class for the 8x1 multiplexer(MUX) circuit. Users are expected to instantiate this class preferably with the name 'mux8x1'
    input_vec=The vector of width 8 used for providing the input
    sel_vec=The select line vector
    out= The output
    '''
    def __init__(self, input_vec,sel_vec):
        if sel_vec[0]==0:
            if sel_vec[1]==0:
                if sel_vec[2]==0:
                    self.out=input_vec[0]
                elif sel_vec[2]==1:
                    self.out=input_vec[1]
            elif sel_vec[1]==1:
                if sel_vec[2]==0:
                    self.out=input_vec[2]
                elif sel_vec[2]==1:
                    self.out=input_vec[3]
        elif sel_vec[0]==1:
            if sel_vec[1]==0:
                if sel_vec[2]==0:
                    self.out=input_vec[4]
                elif sel_vec[2]==1:
                    self.out=input_vec[5]
            elif sel_vec[1]==1:
                if sel_vec[2]==0:
                    self.out=input_vec[6]
                elif sel_vec[2]==1:
                    self.out=input_vec[7]
    def output(self):
        return self.out

class Bus_Mux2x1:
    '''
    Docstring for Bus_Mux2x1
    This is the class for the 2x1 bus multiplexer(MUX) circuit. Users are expected to instantiate this class preferably with the name 'bus_mux2x1'
    input1_vec=The vector of width 64 used for providing the first input
    input2_vec=The vector of width 64 used for providing the second input
    sel=The select line
    out_vec= The output vector
    '''
    def __init__(self,input1_vec,input2_vec,sel):
        if (sel==0):
            self.out_vec=input1_vec
        elif (sel==1):
            self.out_vec=input2_vec
    def update(self,input1_vec,input2_vec,sel):
        if (sel==0):
            self.out_vec=input1_vec
        elif (sel==1):
            self.out_vec=input2_vec
    def output(self):
        return self.out_vec 