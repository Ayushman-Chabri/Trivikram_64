class Bus_64:
    '''
    Docstring for Bus_64
    This class is made to model a 64 bit wide bus (i.e, 64 wires each carrying 1 bit).
    The users can instantiate this class preferably with the name 'bus_64'
    As soon as the class is instantiated, a 64 bit wide array is created alongside
    
    The insert method is used for taking the input from a list and storing it into the bus. 
    A list was used for inputs so that at the time of implementation data transfer remains simple.
    
    Here-:
    __init__() -: 
    Description-:This method is the class constructor. As soon as the object is made,a list of 64 bits is created. 
    Parameters-: None
    Physical Analogy (if any)-: As soon as the object is created, the constructor is summoned. So as soon as the object is created, we can phsyically map it to the situation where 64 wires are created
    Further functions-: None
    Return type-: None
    
    insert(list_bits)-:
    Description-: This method is called to load the data into the bus.
    Parameters-: list_bits is list which provides the input values for the bus
    Physical analogy-: This is physically analogous to hooking up the wires with the starting points of the current
    Further operations-: A value error is raised if list_bit is not of length 64. Otherwise the data of list_bits is loaded into the object bus
    Return type-: None
    
    read()-:
    Description-: This is a function for debugging. This is used to inspect the data in the wire.
    Parameters-: None
    Physical Analogy-: N.A
    Further operations-: None
    Return type-: A list of length 64
    
    output()-:
    Description-: This method is called for offloading data from the bus.
    Parameters-: None
    Physical Analogy-: This is physically analogous to hooking up the wires with the output points
    Further operations-: None
    Return type-: A list of length 64
    '''
    def __init__(self):
        self.bus=[0]*64
    def insert(self, list_bits:list):
        if len(list_bits)!=64: 
            raise ValueError(f"Trying to input {len(list_bits)} in a 64 bit bus")
        self.bus=list_bits
    def output(self)->list:
        return self.bus
    
    #Function for Debugging
    def read(self)->list:
        return self.bus