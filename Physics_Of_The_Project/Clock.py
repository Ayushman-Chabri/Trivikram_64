class Clock:
    '''
    Docstring for Clock
    This the Clock class which would be used to simulate the clock of the computer.
    frequency-: A parameter passed as input at the time of initialization determining the frequency of the clock
    period-: A parameter which determines the length of a single clock cycle.
    running-: A boolean parameter which determines whether the program is being executed currently. This acts as the terminating case for the clock object
    state-: This determines the binary state of the clock(whether it is 0 or 1)
    _thread-: A private method to execute threading(Pythonic way of executing parallel processing). This enables the clock to run simultaneously but separately from the main program, replicating the actual clock in computers.
    
    start_clk-: A method which is used to start the clock. This can be used at the starting of an instruction cycle to set the clock ticking. This contains a thread targeted at the toggle_loop.
    stop -: This is another method used to stop the clock after the execution of the complete set of instructions
    toggle_loop-: A method which is used to tick the clock on and off repeatedly in an infinite loop until turned off.This sets the clock to 1 for time=period/2 and then to 0 for time=period/2 repeatedly.
    read-: A method which is used to read the current clock value. It's a helper function required for debugging.
    '''
    import time
    import threading
    def __init__(self, frequency):
        self.frequency=frequency
        self.period=1/frequency
        self.running=False
        self.state=0
        self._thread=None
    def start_clk(self):
        if not self.running:
            self.running=True
            self._thread=Clock.threading.Thread(target=self.toggle_loop)
            self._thread.start()
            #The following line may be removed or edited in the final product
            print(f"Clock started at speed {self.period}")
    def stop(self):
        if self.running:
            self.running=False
            if self._thread:
                self._thread.join()
            #The following line may be removed or edited in the final product
            print("Clock halted")
    def toggle_loop(self):
        while self.running:
            self.state=1
            Clock.time.sleep(self.period/2)
            self.state=0
            Clock.time.sleep(self.period/2)
    def read(self):
        return self.state
    