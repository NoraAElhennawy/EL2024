DDR_Sel=0
Valid_port=["A","B","C","D","E","F"]
Valid_Dir=["IN","OUT"]
DDRX=0
PortName=input(" Please Enter port(A-F) you need to init:  ")
if(PortName in Valid_port ):    
    for i in range(0,8):
        DDR_Sel=input(f"\nEnter Bit{i} direction IN/OUT:  ")
        if(DDR_Sel=='IN'):
            DDRX|=0<<i
        elif(DDR_Sel=='OUT'):
            DDRX|=1<<i
        else:
            print("\nInvalid input ,valid direction is IN/OUT defualting to IN")    
    
else:
    print("\nInvalid input ,valid port name A:F")
print(f"\nvoid Init_PORT{PortName}_DIR(void)","\n{")
print(f"\nDDR{PortName} = {DDRX};","\n}")

