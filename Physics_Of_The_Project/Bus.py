class Bus_64:
    '''
    Docstring for Bus_64
    This class is made to model a 64 bit wide bus (i.e, 64 wires each carrying 1 bit)
    As soon as the class is instantiated, a 64 bit wide numpy array is created alongside
    
    The insert method is used for taking the input from a list and storing it into the bus. A list was used for inputs so that at the time of implementation data transfer remains simple.
    '''
    import numpy as np
    def __init__(self):
        self.bus=Bus_64.np.zeros(shape=64,dtype=int)
    def insert(self, list_bits):
        if len(list_bits)!=64: 
            raise ValueError(f"Trying to input {len(list_bits)} in a 64 bit bus")
        input_array=Bus_64.np.array(list_bits, dtype=int)
        self.bus=input_array
    def read(self):
        return self.bus