#script to create project folder and generate .hpp,.cpp for a given class name & namespace
import os
#Get class name
Confirm = 'N'
ValidSel=['Y','N']

while(Confirm=='N'):
    classNam=input("Please Enter Class Name\n")
    NameSpace=input("Please Enter Name space\n")
    Confirm=input(f"Enterd class Name is {classNam} ,Entered NameSpace is {NameSpace}? Y/N\n")
    Confirm=Confirm.upper()
    while(Confirm not in ValidSel):
       Confirm=input("Invalid selection ,Please enter a valid selection Y/N")
        
GenCpp=input("Do you want to generate .cpp? Y/N \n")
GenCpp=GenCpp.upper()
os.mkdir(classNam)
os.chdir(classNam)
#hfile=open(f"\{classNam}\"+classNam+".hpp","w")
hfile=open(classNam+".hpp","w")
#Hfile_content=f"#pragma once\nnamespace {NameSpace}\{\n\tclass {classNam}\{\n\t\tpublic:\n{classNam}();\n~{classNam}();\nprivate:\n\t\t\};"
hfile.write(f"#pragma once\nnamespace {NameSpace}"+"{")
hfile.write(f"\n\tclass {classNam}"+"{")
hfile.write(f"\n\t\tpublic:\n\t\t{classNam}();\n\t\t~{classNam}();\n\t\tprivate:")
hfile.write("\n\t};\n}")
hfile.close()
if(GenCpp=='Y'):
    cfile=open(classNam+".cpp","w")
    cfile.write(f"#include\"{classNam}.hpp\" ")
    cfile.write(f"\nnamespace {NameSpace}"+"{\n")
    cfile.write(f"{NameSpace}:: {NameSpace}"+"{}\n")
    cfile.write(f"{NameSpace}:: ~{NameSpace}"+"{}\n"+"}")
    cfile.close()