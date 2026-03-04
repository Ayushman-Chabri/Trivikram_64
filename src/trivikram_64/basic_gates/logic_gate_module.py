'''
Here,
in1= First input
in2= Second input
out=output
insert()-: This method accepts the inputs and stores the output in the instance variable 'out'
output()=Method to return the output
'''
class Not_Class:
    '''
    Docstring for Not_CLass
    This is the class for the NOT gate. 
    This class must be instantiated preferably as an object with the name 'not_gate' whenever the operation of an inverter is required.
    '''
        
    def insert(self,in1):
        if in1==0:
            self.out=1
        elif in1==1:
            self.out=0
    def output(self):
        return self.out 

class And_Class:
    '''
    Docstring for And_Class
    This is the class for the AND Gate. 
    This class must be instantiated preferably as an object with the name 'and_gate' whenever the operation of an AND gate is required.
    '''      
    def insert(self,in1,in2):
        if in1==0:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=0
        elif in1==1:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=1   
    def output(self):
        return self.out

class Or_Class:
    '''
    Docstring for Or_Class
    This is the class for the OR Gate. 
    This class must be instantiated preferably as an object with the name 'or_gate' whenever the operation of an OR gate is required.
    '''
    def insert(self, in1, in2):
        if in1==0:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=1
        elif in1==1:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=1
    def output(self):
        return self.out

class Nand_Class:
    '''
    Docstring for Nand_Class
    This is the class for the NAND Gate. 
    This class must be instantiated preferably as an object with the name 'nand_gate' whenever the operation of a NAND gate is required.
    '''
    def insert(self, in1, in2):
        if in1==0:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=1
        elif in1==1:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=0
    def output(self):
        return self.out
    
class Nor_Class:
    '''
    Docstring for Nor_Class
    This is the class for the NOR Gate. 
    This class must be instantiated preferably as an object with the name 'nor_gate' whenever the operation of a NOR gate is required.
    '''
    def insert(self, in1, in2):
        if in1==0:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=0
        elif in1==1:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=0
    def output(self):
        return self.out

class Xor_Class:
    '''
    Docstring for Xor_Class
    This is the class for the XOR Gate. 
    This class must be instantiated preferably as an object with the name 'xor_gate' whenever the operation of a XOR gate is required.
    '''
    
    def insert(self, in1, in2):
        if in1==0:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=1
        elif in1==1:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=0
    def output(self):
        return self.out

class Xnor_Class:
    '''
    Docstring for Xnor_Class
    This is the class for the XNOR Gate. 
    This class must be instantiated preferably as an object with the name 'xnor_gate' whenever the operation of a XNOR gate is required.
    '''
    def insert(self, in1, in2):
        if in1==0:
            if in2==0:
                self.out=1
            elif in2==1:
                self.out=0
        elif in1==1:
            if in2==0:
                self.out=0
            elif in2==1:
                self.out=1
    def output(self):
        return self.out