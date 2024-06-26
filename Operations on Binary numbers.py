#This program is used to apply Operations on Binary numbers (compute one's complement-compute two's complement-addition-subtraction)

#check if the number is binary or not
def check_binary (number):
    binary_digits=set('01')
    for digit in number:
        if digit not in binary_digits:
            print("please insert a valid binary number")
            return False
        else:
            return True
#take numbers from the user or exit
while True:
    print("type 'A' to add binary numbers")
    print("type 'B' to exit")
    choice = input("enter your choice")
    if choice == "A":
        #ask the user to insert a number
        num1 = input("please insert your first number")
        #checking if the number is binary or not
        if check_binary (num1) :
            # selecting the operations
            print("please select the operation")
            print("A_compute one's complement")
            print("B_compute two's complement")
            print("C_addition")
            print("D_subtraction")
            choose = input("choose the operation")
            #one's complement
            if choose == "A":
                def ones_complement(number):
                    ones_complement_result=""
                    for bit in number:
                        if bit=="0":
                            ones_complement_result+="1"
                        else:
                            ones_complement_result+="0"
                    return ones_complement_result
                print(num1, "one's complement = ", ones_complement(num1))
            #two's complement
            if choose == "B":
                def twos_complement(number):
                    #get the one's complement
                    ones_complement=""
                    for bit in (number):
                        if bit =="0":
                            ones_complement+="1"
                        else:
                            ones_complement+="0"
                    #add 1 to the one's complement
                    carry=1
                    result=""
                    for bit in reversed(ones_complement):
                        total=int(bit)+carry
                        result+=str(total%2)
                        carry= total//2
                    if carry:
                        result="1"+result
                    return result [::-1]
                print(num1, "two's complement = ", twos_complement(num1))
            #addition
            if choose =="C":
                #ask the user to insert the second number
                num2 = input("please insert the second number")
                # checking if the number is binary or not
                if check_binary(num2):
                    def addition(num1,num2):
                        num1=num1[::-1]
                        num2=num2[::-1]
                        #make both strings the same length
                        if len(num1)<len(num2):
                            num1 +="0"*(len(num2)-len(num1))
                        elif len(num2)<len(num1):
                            num2 +="0"*(len(num1)-len(num2))
                        #binary addition with carry
                        result=""
                        carry=0
                        for i in range (len(num1)):
                            total=int(num1[i])+int(num2[i])+carry
                            result+=str(total%2)
                            carry=total//2
                        if carry:
                            result+= str(carry)
                        return(result[::-1])
                    print(num1," + ",num2," = ",addition(num1,num2))
            #subtraction
            if choose=="D":
                #ask the user to insert the second number
                num2=input("please insert the second number")
                # checking if the number is binary or not
                if check_binary(num2):
                    def subrtaction(num1,num2):
                        #make both strings the same length
                        length=max(len(num1),len(num2))
                        num1=num1.zfill(length)
                        num2=num2.zfill(length)
                        #subtruction with borrow
                        result=""
                        borrow=0
                        for i in range (length-1,-1,-1):
                            bit1=int(num1[i])
                            bit2=int(num2[i])
                            # subtraction with borrow
                            subtraction=bit1-bit2-borrow
                            if subtraction<0:
                                subtraction+=2
                                borrow=1
                            else:
                                borrow=0
                            result+=str(subtraction)
                        #removing leading zeros
                        #result=result.lstrip("0")
                        return result[::-1]
                    print(num1," - ",num2," = ", subrtaction(num1,num2))
    elif choice=="B":
        break
    else:
        print("please select a valid choice")

#test A: if num1= 1110
#        one's complement=0001
#test B: if num1= 1110
#        tow's complement= 0010
#test C: if num1= 1110 , num2= 100
#        addition= 10010
#test D: if num1= 1110 , num2= 100
#        subtraction= 1010

