Hey, so far we have discussed how Boolean algebra turned out to be the perfect solution for implementing logic with the power of electricity. However just as any big machine can be boiled down to nuts and bolts, any computer can be boiled down to a set of switches(whether manual or transistor based) arranged in a specific order. Let's probe into the "order" aspect first.
We shall now be designing the 7 logic gates which are fundamental to computer circuits and human thought. If you have ever taken a course on Digital Logic or have had curiosity about how computers actually implement instructions, you must have heard about this.
In this section we give you a holistic understanding of logic gates and further in this chapter we would implement them(in the most fundamental manner possible). Please note that we have made the implementation of the logic gates in a module named "Logic_Gate_module" so that we can access these gates easily when needed. Besides we have used the truth table to implement this logic instead of logical operators because this is the more fundamental and authentic style of execution if we want to stay true to our ideology of circuit level implementation.
**The Basics of Thought(NOT,AND,OR)**
NOT,AND and OR are the three most fundamental logic operations that we perform on a daily basis. Their usage is so common that none of our effective communications can be executed without them. 
*NOT*-: This refers to the inversion of a statement.
Implementation-: 
If in=0,then  out=1
If in=1,then  out=0

*AND*-: This is a logic operation which gives a 'True' as an output only and only when both inputs are 'True'
If in1=0, in2=0, then out=0
If in1=0, in2=1, then out=0
If in1=1, in2=0, then out=0
If in1=1, in2=1, then out=1

*OR*-: This is a logic operation which gives 'True' as an output when at least one of the two inputs is set to 'True'
If in1=0, in2=0, then out=0
If in1=0, in2=1, then out=1
If in1=1, in2=0, then out=1
If in1=1, in2=1, then out=1

**The Universal Gates(NAND, NOR)**
Now that we have completed the basic gates, lets move forward and construct something that logicians term as universal gates. NAND is essentially NOT AND and NOR is essentially NOT OR, then what's so universal about them? The answer lies in the fact that any other logic gate, even the fundamental ones, can be constructed using a circuits purely made of NAND gates or NOR gates. Now let's look at the their implementation.

*NAND*-: This is the inverse of the AND operation.
If in1=0, in2=0, then out=1
If in1=0, in2=1, then out=1
If in1=1, in2=0, then out=1
If in1=1, in2=1, then out=0

*NOR* -: This is the inverse of the OR operation
If in1=0, in2=0, then out=1
If in1=0, in2=1, then out=0
If in1=1, in2=0, then out=0
If in1=1, in2=1, then out=0

**The special gates(XOR, XNOR)**
These gates are stuff which no programmer gets a hang of, when they start programming initially. For now you may accept it on face value. Later, when we proceed to combinational circuits, you will be able appreciate the impact of these gates.

*XOR*-: This is the gate which gives it's output as 'True' only when exactly one input is set to 'True'
If in1=0, in2=0, then out=0
If in1=0, in2=1, then out=1
If in1=1, in2=0, then out=1
If in1=1, in2=1, then out=0

*XNOR*-: This is the gate which gives it's output as 'True' only when both inputs are 'False' or both inputs are 'True'
If in1=0, in2=0, then out=1
If in1=0, in2=1, then out=0
If in1=1, in2=0, then out=0
If in1=1, in2=1, then out=1
