from Combinational_Circuits import Multiplexer_Circuit as mc
class Barrel_Shifter_Left:
    '''
    Docstring for Barrel_Shifter_Left
    This is the class that we use to generate a 64 bit barrel shifter which shifts the numbers to left by a specificed amount. Users are expected to instantiate this preferably with the name 'barrel_shifter_left'
    This is implemented using 6 layers of 2x1 multiplexers where each layer has 64 multiplexers.
    Here,
    in_vec=The input vector of width 64
    s=The select line vector of width 6
    output_list= The output vector of width 64
    '''
    def __init__(self, in_vec,s):
        #Initialized six layers of multiplexers (logn)
        mux_list0=[]
        mux_list1=[]
        mux_list2=[]
        mux_list3=[]
        mux_list4=[]
        self.mux_list5=[]
        
        #Bundled the layers into a single list named "layers"
        layers=[mux_list0,
                mux_list1,
                mux_list2,
                mux_list3,
                mux_list4,
                self.mux_list5]
        
        #Outer loop for simulating layers
        for i in range (0,6):
            offset=2**i #Variable for handling offset
            #Inner loop for simulating each mux (of the 64)in a layer
            for j in range (0,64):
                if i==0:
                    if j<offset:
                        layers[i].append(mc.Multiplexer2x1([in_vec[j],0],s[i]))
                    else:
                        layers[i].append(mc.Multiplexer2x1([in_vec[j],in_vec[j-offset]],s[i]))
                else:
                    if j<offset:
                        layers[i].append(mc.Multiplexer2x1([layers[i-1][j].output(),0],s[i]))
                    else:
                        layers[i].append(mc.Multiplexer2x1([layers[i-1][j].output(),layers[i-1][j-offset].output()],s[i]))
                
        
        
    def output(self):
        output_list=[0]*64
        for i in range (0,64):
            output_list[i]=self.mux_list5[i].output()
        return output_list
        

class Barrel_Shifter_Right:
    '''
    Docstring for Barrel_Shifter_Right
    This is the class that we use to generate a 64 bit barrel shifter which shifts the numbers to right by a specificed amount. Users are expected to instantiate this preferably with the name 'barrel_shifter_reft'
    This is implemented using 6 layers of 2x1 multiplexers where each layer has 64 multiplexers.
    Here,
    in_vec=The input vector of width 64
    s=The select line vector of width 6
    sb=signbit
    output_list= The output vector of width 64
    '''
    def __init__(self, in_vec,s,sb):
        #Initialized six layers of multiplexers (logn)
        mux_list0=[]
        mux_list1=[]
        mux_list2=[]
        mux_list3=[]
        mux_list4=[]
        self.mux_list5=[]
        
        #Bundled the layers into a single list named "layers"
        layers=[mux_list0,
                mux_list1,
                mux_list2,
                mux_list3,
                mux_list4,
                self.mux_list5]
        
        #Outer loop for simulating layers
        for i in range (0,6):
            offset=2**i #Variable for handling offset
            #Inner loop for simulating each mux (of the 64)in a layer
            for j in range (0,64):
                if i==0:
                    if j+offset>63:
                        layers[i].append(mc.Multiplexer2x1([in_vec[j],sb],s[i]))
                    else:
                        layers[i].append(mc.Multiplexer2x1([in_vec[j],in_vec[j+offset]],s[i]))
                else:
                    if j+offset>63:
                        layers[i].append(mc.Multiplexer2x1([layers[i-1][j].output(),sb],s[i]))
                    else:
                        layers[i].append(mc.Multiplexer2x1([layers[i-1][j].output(),layers[i-1][j+offset].output()],s[i]))
                
        
        
    def output(self):
        output_list=[0]*64
        for i in range (0,64):
            output_list[i]=self.mux_list5[i].output()
        return output_list
        
    