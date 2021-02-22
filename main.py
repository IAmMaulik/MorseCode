from data import alphabet_to_morse, morse_to_alphabet

def convert_to_arr(input_string):
    # logic to convert the morse code string into a list 😶
    if "  " not in input_string:
        li = list(input_string.split(" "))
    return li


def encode(input_string):
    # funtion to convert the text into morse code COMPLETE 🔥🔥🔥
    output_arr = []
    for i in range(len(input_string)):
        output_arr.append(alphabet_to_morse[input_string[i].upper()])
        if (i+1) >= len(input_string):
            break
        elif input_string[i+1] == " ":
            output_arr.append("   ")
        else:
            output_arr.append(" ")
    return ''.join(output_arr)

def decode(input_string):
    # funtion to convert the morse code back into text COMPLETE 🔥🔥🔥
    output_arr = []
    li = convert_to_arr(input_string)
    for i in range(len(li)):
        if li[i] == " ":
            output_arr.append(" ")
        else:
            output_arr.append(morse_to_alphabet[li[i]])
    return ''.join(output_arr)


user_input = input("Enter the text: ")
encoded_string = encode(user_input)
print(encoded_string)
print(decode(encoded_string))