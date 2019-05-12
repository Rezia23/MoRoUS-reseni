import string
alphabet = string.ascii_uppercase + "0123456789"
print("Zadejte zachycenou zprávu")
msg = input()
msg = msg.upper()
shift = 0
while shift < 36:
  for i in msg:
    print(alphabet[(alphabet.index(i) + shift) % len(alphabet)], end = "")
  print("")
  shift += 1
