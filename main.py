from data import alphabet_to_morse, morse_to_alphabet

def encode(string):
    output_string = []
    for i in range(len(string)):
        output_string.append(alphabet_to_morse[string[i].upper()])

        if (i+1) == len(string):
            break
        elif string[i+1] == " ":
            output_string.append("  ")
        else:
            output_string.append(" ")
    
    return ''.join(output_string)

print(encode(input("Enter the text you want to encode: ")))