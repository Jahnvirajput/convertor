

# I have kept the whole code under while loop to keep on running it until the user wants to exit
# SO i have even made a condition where if the user enters exit the loop or programme would end exicution
while (True):
    print("Roman to integer and Integer to Roman converter")
    print("For roman to integer conversion  press'1':\nFor integer to roman conversion press'2':\nENTER 'Exit' to exit the programme")
    choice = input()
    choice = choice.upper()
    if choice == "1":
        roman_input = input("ENTER A ROMAN NUMBER: ")
        roman_input = roman_input.upper()

        settingvalues = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer_output = 0
        check = "IVXLCDM"
    
        if roman_input[0] in check:
            for i in range(len(roman_input)):
                if i+1 != len(roman_input) and settingvalues[roman_input[i]] < settingvalues[roman_input[i + 1]]:
                    integer_output -= settingvalues[roman_input[i]]
                else:
                    integer_output += settingvalues[roman_input[i]]
        else:
            print("Invalid input")
        print("After conversion:\n", roman_input, "=", integer_output)

#  From here the below code is for the integer to Roman number converter and i have made a logic with the help of for looop and if-else condition

    elif choice == "2":
        n = int(input("Enter the integer you want to convert into ROMAN:"))
        num = n
        val = n
        r = str()
        setting_values = {1: "I", 5: "V", 4: "IV", 10: "X", 9: "IX", 50: "L",
                          40: "XL", 100: "C", 90: "XC", 500: "D", 400: "CD", 1000: "M", 900: "CM", }
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while n <= num:
                r += setting_values[n]
                num -= n

        print("After conversion:\n", val, "=", r)
    elif choice == "EXIT":
        break
    else:
        print("Invalid input")
