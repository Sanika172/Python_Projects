mob_no = input("enter your mobile number")
cnt = len(mob_no)
if cnt < 10 or cnt > 10:
    print("invalid mobile number! please check it")
elif mob_no.isalpha():
    print("dont enter alphabets instead of numbers")
else:
    print("mobile number registered successfully")
