

# OBTAIN the string 
pattern = input("Enter the characters no more than 7 characters: ")

# CHECK the string is less than 7 or not
if len(pattern) > 7:
    print("The string you have enetered is too long\n")

# IF not then enters in the block
else:

# IF the length of the string is even printed bfull_length slicing the string
    if len(pattern) % 2 == 0:
        full_length = len(pattern)
        half_length = int(full_length/2)
        print( (5-1)*half_length*' ' + (pattern[:half_length])*1 + (pattern[half_length:])*1 )
        print( (5-2)*half_length*' ' + (pattern[:half_length])*2 + (pattern[half_length:])*2 )
        print( (5-3)*half_length*' ' + (pattern[:half_length])*3 + (pattern[half_length:])*3 )
        print( (5-4)*half_length*' ' + (pattern[:half_length])*4 + (pattern[half_length:])*4 )
        print( (5-5)*half_length*' ' + (pattern[:half_length])*5 + (pattern[half_length:])*5 )

# IF the length of string is odd whole string printed
    else:
        full_length = len(pattern)
        print( str(pattern)*1 + str((5-1)*full_length*2*' ') + str(pattern)*1 )
        print( str(pattern)*2 + str((5-2)*full_length*2*' ') + str(pattern)*2 )
        print( str(pattern)*3 + str((5-3)*full_length*2*' ') + str(pattern)*3 )
        print( str(pattern)*4 + str((5-4)*full_length*2*' ') + str(pattern)*4 )
        print( str(pattern)*5 + str((5-5)*full_length*2*' ') + str(pattern)*5 )

