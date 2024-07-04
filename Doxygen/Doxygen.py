from bs4 import BeautifulSoup
import csv
import requests
    
Allfunc_ls=[]
AllParam_ls=[]
All_Param_Num_ls=[]
AllReturn_ls=[]

def DoxParser(soup):
    Contents=soup.find('div',class_='contents')
   # print(Contents)
    Allmemitems=Contents.find_all("div",class_='memitem')
    #print(Allmemitems)
   # FuncName=FuncNames.find("h2").text.strip()
    for memitem in Allmemitems:        
        proto=memitem.find("div",class_='memproto')
      #  print(proto)
        memname=proto.find("table",class_='memname')
      #  print(memname)
        Fname=memname.find("td",class_='memname').text
        Allfunc_ls.append(Fname)
        print("\nfn name: ",Fname,"\n=================\n")                   
        Allparam=memname.find_all("td",class_='paramname')
       # print(Allparam,":\n=================\n")
        param_counter=0
        for param in Allparam:
            paramName=param.find("em").text
            AllParam_ls.append(paramName)
            param_counter+=1
            print(paramName,"\n===============\n")
        All_Param_Num_ls.append(param_counter)

        freturns=memitem.find_all('div',class_='memdoc')
       # print(freturns)
               
        for freturn in freturns:
            retunarg=freturn.find_all('dl',class_='section return')
            for i in retunarg:
                x=i.find('dd').text
                AllReturn_ls.append(x)
                print("\n return :")
                print(x)    
            # print(retunarg)
            else:
                AllReturn_ls.append("void")     
    print("\nFunc list:",Allfunc_ls,"\n================\n")
    print("\nParam List:",AllParam_ls,"\n================\n")
    print("\nNumber of Param per Fnc List:",All_Param_Num_ls,"\n================\n")
    print("\nreturn Fnc List:",AllReturn_ls,"\n================\n")

def SavetoCSV():
    with open('Doxygen.csv', 'w') as csvfile:
          csv_writer = csv.writer(csvfile)    
          csv_writer.writerow(['Signature','Parameter','Return','\n'])                         
          row=[]
          k=0
          for i in range(0,len(Allfunc_ls)):
            if(All_Param_Num_ls[i]): #write function doc
                row.append(Allfunc_ls[i])
                print(f"\ni={i}")
                param=[]
                for j in range(0,All_Param_Num_ls[i]):
                    print("\nj=",j)
                    param.append(AllParam_ls[i+j])
                    print(param)
                row.append(" ".join(param))
                row.append(AllReturn_ls[i])
               # row.append("\n") 
                print(row)
                csv_writer.writerow(row)
                row.clear()
            else: # write arg
             #row=[f"Variable#{k}",Allfunc_ls[i],'\n']
                csv_writer.writerow([f"Variable#{k}",Allfunc_ls[i]])
                k+=1
                            

def main():
    fileDisc=open("C:/Users/hp/Documents/EmbbededLinux/Doxygen/output/html/namespace_doxygen__ex.html","r")
    fileCont=fileDisc.read()
    fileDisc.close()
    soup=BeautifulSoup(fileCont,"lxml")
    print(soup)
    print("==========================================")
    DoxParser(soup)
    SavetoCSV()

main()
