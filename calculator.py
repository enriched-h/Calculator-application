import os

def calculator():
        try:
               num1 = float(input("Please enter your first number\n"))
               operator = input("Please enter a valid operand(+ or - or / or *)\n")
               num2 = float(input("Please enter your second number\n"))
               

               with open('equation_file.txt', 'a+') as write_equaton_file:
                    write_equaton_file.write("")
                    try:
                      if  operator == "+":
                        add_result = num1 + num2
                        add_equation = (str(num1) + " + " + str(num2) + " = "  + str(add_result))
                        write_equaton_file.write("\n"+add_equation)
                        print(add_equation)            
                        return
              

                      elif operator == "-":
                         sub_result = num1 - num2
                         sub_equation = " "
                         sub_equation = (str(num1) + " - " + str(num2) + " = " + str(sub_result))
                         write_equaton_file.write("\n"+sub_equation)
                         print(sub_equation)
                         return

                    
                      elif  operator == "/" :
                          div_result = num1 / num2
                          div_equation = (str(num1) + " / " + str(num2) + " = " + str(div_result))
                          write_equaton_file.write("\n"+div_equation)
                          print(div_equation)
                          return
                   
                      elif operator == "*":
                         num1 * num2
                         mul_result = num1 * num2
                         mul_equation = (str(num1) + " * " + str(num2) + " = " + str(mul_result))
                         write_equaton_file.write("\n"+mul_equation)
                         print(mul_equation)
                         write_equaton_file.close()
                         return
            

            
                      else: operator != "+" or operator != "-" or operator != "/" or operator != "*"
                      print("You have not entered a valid operator ")
                      return
                    except ZeroDivisionError:
                           print(ZeroDivisionError)
                           print("You cannot divide by zero")
                           
        except ValueError:
                      print(ValueError)
                      print("You have entered an invalid character\n")
                  

def view_previous_calc():
                  user_file_name = input("Please enter the name of the file ")
                  if user_file_name != "equation_file":
                         print("No such file exists")
                  else:
                       # View previous calculations
                       with open('equation_file.txt', 'r') as read_equation_file:
                        
                        content = read_equation_file.read()
                        
                        # Check if file has data,the url i used: https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not
                        if os.stat("equation_file.txt").st_size == 0:
                              print("There are no previous calculations ")
                        else:
                            print(content)
                            return

 
while True:
        # Give user choce to ether use a calculator or view previous calculations
            user_choice = input("Would you like to use a calculator or view previous calculatons???\n\
Enter 'c' to use a calculator or enter 'v' to view previous calculations \n").lower()
        
            if user_choice == "c":
                  calculator()
            
        
            elif user_choice == "v":
                   view_previous_calc()
                    
            
            else: # Automatically print this statement if user has entered an incorrect value at some point
                  print("You have made an invalid selection\n")
