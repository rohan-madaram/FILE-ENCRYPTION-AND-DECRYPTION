def Encrypt(filename,key):
  file = open(filename,"rb")
  data = file.read()
  file.close()

  data = bytearray(data)
  for index, value in  enumerate(data):
    data[index] = value ^ key 

  file = open("CC-" + filename , "wb")  
  file.write(data)
  file.close()

def Decrypt(filename,key):
  file = open(filename,"rb")
  data = file.read()
  file.close()

  data = bytearray(data)
  for index, value in  enumerate(data):
    data[index] = value ^ key 


  file = open("CC-" + filename , "wb")  
  file.write(data)
  file.close() 


  choice = ""
  while choice != 3:
    print("please select an option:")
    print("1.ENCRYPT FILE")
    print("2.DECRYPT FILE")
    print("3.EXIT")
    choice = input()
    if choice == "1"  or choice == "2":
      key = int(input("enter the key:\n"))
      filename = input("enter the filename with extension:\n")
    if choice == "1" :
      Encrypt(filename,key)

    if choice == "2"  :
      Decrypt(filename,key)

