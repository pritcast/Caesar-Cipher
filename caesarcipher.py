# Caesar Cipher Technique

# importing module
import string

# Welcome Msg
print("Welcome to Ceasar Cipher Encription Technique!")
print("----------------------------------------------------")


# Letters
letters = string.ascii_letters

# Encode Function
def encode(msg,secret_key):
    encode_msg = ""  # Taking encode message an empty string
    for ch in msg:  # Iterate over user message
        if ch in letters: # Check if the ch in letters or not 

            # Take the character index
            ch_index = letters.index(ch)

            # if character index is greater or equal to the length, reverse the character
            if ch_index >= len(letters):
                ch_index -= len(letters)

            # take the encode character index
            encode_ch_index = ch_index+secret_key

            # Find the encode character
            encode_ch = letters[encode_ch_index]
            
        else: #  if character is not in letters then the encode character is the character
            encode_ch = ch
        

        # Concatinate the encode character with the encode message
        encode_msg += encode_ch

    return encode_msg



# Decode Function
def decode(msg,secret_key):
    decode_msg = ""
    for ch in msg:
        if ch in letters:
            ch_index = letters.index(ch)
            decode_ch_index = ch_index-secret_key
            decode_ch = letters[decode_ch_index]
            
        else:
            decode_ch = ch
        
        decode_msg += decode_ch

    return decode_msg


# function for taking msg and key
def msg_and_key():
    user_msg = input("Enter your message: ").lower()
    secret_key = int(input("Enter your key: "))
    return user_msg,secret_key




# Encode Decode a msg



# Taking user input
user_choice = input("What do you want to do? (1 for encode/2 for decode): ")
if user_choice == "1":

    # Taking user message and secret key to encode the msg
    user_msg, secret_key = msg_and_key()

    # call the encode function
    encode_msg = encode(user_msg,secret_key)
    print(f"your message could be: {encode_msg}")


else:
    # Taking user message and secret key to decode the msg
    user_msg, secret_key = msg_and_key()

    # decode msg
    decode_msg = decode(user_msg,secret_key)
    print(f"your message could be: {decode_msg}")