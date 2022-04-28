
D = {1:{"rollno":12,"class":"b.com","percentage":78.50},
 2:{"rollno":14,"class":"b.com","percentage":78.90},
 3:{"rollno":15,"class":"b.com","percentage":39.50}}
 
rollnum = int(input('enter rollNumber @'))

print("you entered rollnumber @", rollnum)
if (rollnum == D[1]["rollno"]):
    print("percentage ",D[1]["percentage"])
    if (D[1]["percentage"]>40):
        print ("you passed")
    else :
        print('failed beta')
    
elif (rollnum == D[2]["rollno"]):
    print("percentage ",D[2]["percentage"])
    if (D[2]["percentage"]>40):
        print ("you passed")
    else :
        print('failed beta')
elif (rollnum == D[3]["rollno"]):  
    print("percentage ",D[3]["percentage"])
    if (D[3]["percentage"]>40):
        print ("you passed")
    else :
        print('failed beta')
else :    
    print("not have rollnumber") 

