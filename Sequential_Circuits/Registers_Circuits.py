import Flipflops_Circuits as ff

class Register_64:
    '''
    A 64-bit PIPO Register with Load/Hold capability.
    '''
    def __init__(self): # Removed unused 'clk' argument
        self.reg_list = []
        for i in range(0, 64):
            self.reg_list.append(ff.D_Flipflop())

    def output(self):
        output_list = []
        for i in range(0, 64):
            output_list.append(self.reg_list[i].q_state)
        return output_list

    def update(self, in_vec, write_enable, clk):
        # 1. Get the current data (Feedback Loop)
        current_data = self.output()
        
        # 2. Loop through all 64 bits
        for i in range(0, 64):
            
            # --- MUX LOGIC (Inline) ---
            if write_enable == 1:
                # Load Mode: Accept new input
                bit_to_store = in_vec[i]
            else:
                # Hold Mode: Refresh old data
                bit_to_store = current_data[i]
            
            # --- CLOCK TRIGGER ---
            # Update the Flip-Flop with the chosen bit
            self.reg_list[i].update(bit_to_store, clk)
            
            