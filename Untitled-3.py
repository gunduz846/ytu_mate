a= input("vize notunuzu giriniz")
b= input("final notunuzu giriniz")

if 100>= (int(a)*4+int(b)*6)/10 >= 80:
    print("AA")
elif 80 > (int(a)*4+int(b)*6)/10 >= 60:
    print("BB")
elif 60 > (int(a)*4+int(b)*6)/10 >= 40:
    print("CC")
elif 40 > (int(a)*4+int(b)*6)/10 >= 20:
    print("DD")
elif 20 > (int(a)*4+int(b)*6)/10 >= 0:
    print("FF")
