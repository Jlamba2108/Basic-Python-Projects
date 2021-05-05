logo=''' 
 ______     ______     ______     ______     ______     ______        ______     __     ______   __  __     ______     ______    
/\  ___\   /\  __ \   /\  ___\   /\  ___\   /\  __ \   /\  == \      /\  ___\   /\ \   /\  == \ /\ \_\ \   /\  ___\   /\  == \   
\ \ \____  \ \  __ \  \ \  __\   \ \___  \  \ \  __ \  \ \  __<      \ \ \____  \ \ \  \ \  _-/ \ \  __ \  \ \  __\   \ \  __<   
 \ \_____\  \ \_\ \_\  \ \_____\  \/\_____\  \ \_\ \_\  \ \_\ \_\     \ \_____\  \ \_\  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ /_/      \/_____/   \/_/   \/_/     \/_/\/_/   \/_____/   \/_/ /_/ 
                                                                                                                                 
'''

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,direction):
  message=""
  for i in range(0,len(text)):
    char=text[i]
    if char in alphabet:
     char_index=alphabet.index(char)
     if direction=="encode":
       char_index+=shift
     elif direction=="decode":
       char_index-=shift
     char=alphabet[char_index]
     message+=char
    else:
      message+=char
    char_index=0
  print(message)


continue_check=True
while continue_check:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))
 shift=shift%26
 caesar(text,shift,direction)
 result=input("Type 'yes' if you want to go again else type 'no'\n")
 if result=="no":
   print("Bye!")  
   continue_check=False
