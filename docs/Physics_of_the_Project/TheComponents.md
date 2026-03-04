**Goal and Intuition behind the Project-:**
As a reader, you must be well aware about the objectives of this project. The project aims to build a *virtual processor* from the very basics using the *Python language*. Though this approach might sound counterintuitive(like Python is a high level language used in fully developed processors to produce large scale applications, why and how could it be used to design a processor?) but this has a lot of advantages. 
First of all this removes the requirement of expensive tools and products and their associated complications like damages, lack of scalability, restrictions in redesigning and stuff. Secondly it also abstracts away the rigorous details of Physics that are more suited for a person from an electronics background.
Here we define the first few tools which we would use throughout our project.

**The Starting Toolkit-: (The atoms of the project)**

**The Wire-:** Since computers are electrical systems and electricity is best explained as a flow of electrons, we need to have definite pathways for their flow. These pathways are wires. In Python we would simulate wires using the *"="(assignment operator).*
*Eg-: A=B (Here A and B are two locations and the "=" sign is the wire which would take the contents stored in B to A.)*

**The Bus-:** A bundle of wires considered together is what we call a Bus. Here, the buses would be represented in the form of fundamental data structures like *arrays or lists.*
Refer to [Bus_64.svg](../../images/Bus_64.svg) for functional diagram
Refer to [Bus.py](../../src/trivikram_64/physics_of_the_project/Bus.py) for source code and class specific documentation

**The Current-:** Since the paths already exist, now the current must flow. Here the current would be the data which would flow.

**The Clock-:** The clock is a key component of computers often regarded as "the heart beat". Though this is a fundamental component, we won't see it till we reach sequential circuits. A deeper explanation would be provided there. The clock would be implemented using the clock class and the *sleep function*.
Refer to

**The Voltage-:** The voltage in computers determine whether a certain signal is to be termed as a 0 or 1 based on the configurations of the transistors used in the circuit of the computer. Since we aren't implementing it on physical hardware, here the number 1 would be considered as 1 and 0 would be considered as 0.

**Additional Constructs-:** Since we are following a *64 bit archietcture* (the term will be explained soon) physically connecting every device would be tiresome and monotonous. Therefore we might take help of Python constructs like *loops* and *conditionals*. This however shouldn't be viewed as a deviation from first principle implementation because even *Hardware Description Languages* make use of *Behavioral approach* which in turn, employ *procedural constructs* (The last line is only for those who have some basic idea of HDL. Others can ignore).

