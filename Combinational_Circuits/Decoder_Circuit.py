class Decoder_2x4:
    '''
    Docstring for Decoder_2x4
    This is the class for generating a 2X4 decoder. The users are expected to instantiate this class preferably with the name 'decoder_2x4'
    Here.
    input_vec=The input vector of width 2
    output_vec=The output vector of width 4
    
    '''
    def __init__(self,input_vec):
        self.out_vec=[0]*4
        if (input_vec[0]==0):
            if (input_vec[1]==0):
                self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3]=1,0,0,0
            elif(input_vec[1]==1):
                self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3]=0,1,0,0
        elif (input_vec[0]==1):
            if (input_vec[1]==0):
                self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3]=0,0,1,0
            elif(input_vec[1]==1):
                self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3]=0,0,0,1
    def output(self):
        return self.out_vec

class Decoder_3x8:
    '''
    Docstring for Decoder_3x8
    This is the class for generating a 3X8 decoder. The users are expected to instantiate this class preferably with the name 'decoder_3x8'
    Here.
    input_vec=The input vector of width 3
    output_vec=The output vector of width 8
    
    '''
    def __init__(self,input_vec):
        self.out_vec=[0]*8
        if (input_vec[0]==0):
            if (input_vec[1]==0):
                if(input_vec[2]==0):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=1,0,0,0,0,0,0,0
                elif(input_vec[2]==1):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,1,0,0,0,0,0,0
            elif (input_vec[1]==1):
                if(input_vec[2]==0):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,1,0,0,0,0,0
                elif(input_vec[2]==1):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,0,1,0,0,0,0
        elif (input_vec[0]==1):
            if (input_vec[1]==0):
                if(input_vec[2]==0):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,0,0,1,0,0,0
                elif(input_vec[2]==1):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,0,0,0,1,0,0
            elif (input_vec[1]==1):
                if(input_vec[2]==0):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,0,0,0,0,1,0
                elif(input_vec[2]==1):
                    self.out_vec[0],self.out_vec[1],self.out_vec[2],self.out_vec[3],self.out_vec[4],self.out_vec[5],self.out_vec[6],self.out_vec[7]=0,0,0,0,0,0,0,1
        
    def output(self):
        return self.out_vec