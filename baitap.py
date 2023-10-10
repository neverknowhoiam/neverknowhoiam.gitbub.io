    # print('Enter number:')
    # c = input()
    # c = int(c)
    # if c % 2 == 0:
    #     print ('Even number')
    # else :
    #     print('Odd number')
    
# # Input AGV mark  and rank:
#          Excelent :         ĐTB >=8    
#          Good:           8> ĐTB >=6.5
#          Fairly Good:  6.5> ĐTB >= 5
#          Bad:               ĐTB <5
    # print('Enter your grade:')
    # grade = input()
    # grade = int(grade)
    # if grade >= 8:
    #     print('Exellent')
    # elif grade < 8 and grade >= 6.5 :
    #     print('Good')
    # elif grade <6.5 and grade >= 5 :
    #     print('Fairly Good')
    # else :
    #     print('BAD!!!')
        

#Input three int number a,b,c => Find maximum and minimum
    # print('Enter 3 number')
    # a = int(input('Enter a:'))
    # b = int(input('Enter b:'))
    # c = int(input('Enter c:'))
    # max = a
    # min = a
    # if max < b:
    #     max = b
    # elif min > b:
    #     min = b
    # if max < c:
    #     max = c
    # elif min > c:
    #     min = c
    # print('Max is', max)
    # print('Min is',min)    

#Calculate total of 3 numbers entered from keyboard. 
# If the input is incorrect, then assign that number to zero


    # if type(a) != '<class 'int'>':
    #     a = 0
    # elif type(b) != '<class 'int'>':
    #     b = 0
    # elif type(c) != '<class 'int'>':
    #     c = 0
    # try :
    #     a = float(input('Enter a:'))
    # except ValueError:
    #     a = 0
    # try :
    #     b = float(input('Enter b:'))
    # except ValueError:
    #     b = 0
    # try :
    #     c = float(input('Enter c:'))
    # except ValueError:
    #     c = 0  
    # print('Sum = ',a + b + c)
                # sum = 0    
                # while True:
                #     try:
                #         a = input('Enter num:')
                #         a = int(a)
                #         sum += a
                #         break
                #     except:    
                #         print('Try again:')
                # print(sum)    
    
# 1	Input  4  real numbers  a, b, c and x.
# 3.	Calculate  S1 = ax2  + bx + c.
# 4.	Calculate  S2 =   if   b2 - 4ac  > 0, otherwise  S2 = 0 
# 5.	Re-input  a, b and  c. Check whether a, b and c are sides of a triangle or not.
# 6.	If a, b, c are sides of a triangle, then calculate its perimeter and area, otherwise display on the screen a message "a, b, c are not side of a triangle". The area is calculated by the Heron formula below:
# S1 =  , where  
    # a = float(input('Enter a:'))
    # b = float(input('Enter b:'))
    # c = float(input('Enter c:'))
    # print(a,'x^2 +',b,'x +',c)
    # if b ** 2 - 4*a*c > 0 :
    #     S2 = (b ** 2 - 4*a*c) ** 0.5
    # else:
    #     S2 = 0
    # print('S2 =', S2)
    # if a + b >= c and b+c >= a and a+c >=b :
    #     print('a, b, c are  side of a triangle')
    #     p = (a+b+c)/2
    #     S = (p*(p-a)*(p-b)*(p-c))**0.5
    #     print('S =',S)
    # else:
    #     print('a, b, c are not side of a triangle')
# Q6 (1 marks). Write a program to accept 3 real numbers a, b, c, then:
# .	Display the maximum and minimum values among them.
# .	Arrange them in ascending order, i.e.  a ≤ b ≤ c.  

    # try :
    #         a = float(input('Enter a:'))
    # except :
    #         a = 0
    # try :
    #         b = float(input('Enter b:'))
    # except :
    #         b = 0
    # try :
    #         c = float(input('Enter c:'))
    # except :
    #         c = 0   
    # max = a
    # min = a
    # if max < b:
    #     max = b
    # elif min > b:
    #     min = b
    # if max < c:
    #     max = c
    # elif min > c:
    #     min = c
    # print('Max: ', max)
    # print('Min: ', min)
    # list1=[a,b,c]
    # list_sorted = sorted(list1)
    # print(list_sorted)

#tìm ucln,bcnn
    # def ucln(a,b):
    #     if a > b:
    #         min = b
    #     else:
    #         min = a
    #     for i in range(1,min+1):
    #         if a % i == 0 and b % i == 0:
    #             uscln= i
    #     return uscln

    # def bcnn(a,b):
        

    # print(ucln(18,9))        
    
    
    
    
#So Nguyen To
    # a = int(input())
    # if a < 2:
    #     print(a,'ko phai snt')   
    # elif a == 2:
    #     print(a,'la snt')
    # else:
    #     prime= True      #Giả sử a là snt    
    #     for i in range(2,int(a)):        #Loop xét xem a có đúng là snt ko
    #         if a % i == 0 :
    #             prime = False 
    #             break
    #     if prime == True:
    #         print(a,'la snt')
    #     else:
    #         print(a,'ko phai snt')
#Số nhỏ thứ nhì
#Arrange them in ascending order, i.e. a ≤ b ≤ c.
    # a = int(input('Nhap so a:'))
    # b = int(input('Nhap so b:'))
    # c = int(input('Nhap so c:'))
    # Max = a
    # Min = a
    # n2 = 0
    # if Max < b:
    #     n2 = Max
    #     Max = b
    # elif Min > b:
    #     n2 = Min
    #     Min = b
    # if Max < c:
    #     n2 = Max
    #     Max = c
    # elif Min > c:
    #     n2 = Min
    #     Min = c
    # print(Min, n2, Max)
    # print('So nho thu nhi la: ', n2)    
#Chuyển đổi 1 số nguyên sang binary number
# a = int(input('Enter an integer:'))    

#Input an integer number  n, where  n > 5 (If  n≤ 5 then prompt a user to re-enter). Then calculate
# 1.	S1 = 1 + 2 + 3 + ... + n.
# 2.	S2 = n! 
# 3.	Re-input n. Check whether n is a prime number or not.
    # def num(count):
    #     sum = 0
    #     minus = 1
    #     for i in range(0,count):
    #         while True:
    #             try:
    #                 a = input()
    #                 a = int(a)
    #                 sum += a
    #                 minus *= a 
    #                 break
    #             except:
    #                 print('Enter again:')
    #     return sum, minus                   #tuple (sum, minus)
    # num1 = int(input())
    # result = num(num1)
    # print(result[0])

# 1.	Input an integer number  n , then
# 2.	Display n  in binary number format.
# 3.	Re-input n . Calculate the sum of all digits of n.
# 4.	Find the number m, which is the reverse of n. 
#Int to Bin and contrast
    # def int_to_bin(a):
    #     arr = []  
    #     b = ''
    #     while True:
    #         arr.append(a % 2)
    #         a //= 2 
    #         if a == 0:
    #             break
    #     for i in arr[::-1]:
    #         b += str(i)       
    #     return int(b)

    # def bin_to_int(b):
    #     bin_num = 0
    #     x = 0
    #     for i in b[::-1]:
    #         if i != '0' and  i != '1':
    #             return 'Error Value'
    #         bin_num += (2**x)*int(i)
    #         x +=1
            
    #     return bin_num 

    # int_num = int(input('Enter an int:'))
    # bin_num = input('Enter an bin:')
    # print('Int -> Bin:',int_to_bin(int_num))  
    # print ('Bin -> Int:',bin_to_int(bin_num))         



          

        
            