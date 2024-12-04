def steg(txt_file, photo ):
    
    message_in_binary = ""
    
    with open(txt_file, "r") as txt:
        message = txt.read()
        
    op = photo.replace(".bmp", "op.bmp")
    
    for character in message:
        message_in_binary += (f"{ord(character):08b}")
    
    message_length = len(message_in_binary)
    
    with open(photo , "rb") as file:
        
        photo_data= bytearray(file.read())
    
    start = 400
    
    index = 0

    for i in range(start , len(photo_data)):
        
        if index >= message_length:
            break
        
        else:
            photo_data[i] = (photo_data[i] & 0b01111111) | (int(message_in_binary[index]) << 7)
            
            index += 1
        
        
    
    with open(op, "wb") as opt:
        opt.write(photo_data)
        
    with open(op, "rb") as op:
        data = list(bytearray(op.read()))
    
    v = ""
    decoded = ""
    
    for i in range(start, message_length + start):
        msb = (data[i] & 0b10000000) >> 7  
        v += str(msb)

    for i in range(0, len(v), 8):  
     byte = v[i:i+8]
     decoded += chr(int(byte, 2))
     
     print(decoded)

def steg(message, photo ):
    
    message_in_binary = ""
    
    op = photo.replace(".bmp", "op.bmp")
    
    for character in message:
        message_in_binary += (f"{ord(character):08b}")
    
    message_length = len(message_in_binary)
    
    with open(photo , "rb") as file:
        
        photo_data= bytearray(file.read())
    
    start = 400
    
    index = 0

    for i in range(start , len(photo_data)):
        
        if index >= message_length:
            break
        
        else:
            photo_data[i] = (photo_data[i] & 0b01111111) | (int(message_in_binary[index]) << 7)
            
            index += 1
        
        
    
    with open(op, "wb") as opt:
        opt.write(photo_data)
        
    with open(op, "rb") as op:
        data = list(bytearray(op.read()))
    
    v = ""
    decoded = ""
    
    for i in range(start, message_length + start):
        msb = (data[i] & 0b10000000) >> 7  
        v += str(msb)

    for i in range(0, len(v), 8):  
     byte = v[i:i+8]
     decoded += chr(int(byte, 2))
     
     print(decoded)

#testing
def test_steg_with_txt():
    photo_path = "test.bmp"
    txt_file = "message.txt"

    message = "test message"
    with open(txt_file, "w") as txt:
        txt.write(message)

    with open(txt_file, "r") as txt:
        message_content = txt.read().strip()

    steg(message_content, photo_path)

    op = photo_path.replace(".bmp", "op.bmp")
    
    with open(op, "rb") as opt:
        data = list(bytearray(opt.read()))

    start = 400
    message_length = len(message_content) * 8

    v = ""
    decoded = ""

    for i in range(start, message_length + start):
        msb = (data[i] & 0b10000000) >> 7
        v += str(msb)

    for i in range(0, len(v), 8):
        byte = v[i:i+8]
        decoded += chr(int(byte, 2))

    print(f"Original message: '{message_content}'")
    print(f"Decoded message: '{decoded}'")

    if decoded == message_content:
        print("Testing function was successful")
    else:
        print("Testing function failed")

test_steg_with_txt()
