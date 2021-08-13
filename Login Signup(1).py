import json
import os
main_dict={}
list=[]
dict_out={}
user_info={}
if os.path.exists("userdetails.json"):
    pass
else:
    create=open("userdetails.json","w+")
    create.close()
choose=int(input("choose 1 for siging in or choose 2 for logging in:"))
if choose==1:
    name=input("enter your first and last name")
    print(name)
    password=input("enter your password:a.)password should contain upper and lower letters,b)It should contain special character and numbers also")
    upper,lower,digit,special=0,0,0,0
    for i in password:
        if i.isupper():
            upper=upper+1
        if i.islower():
            lower=lower+1
        if i.isdigit():
            digit=digit+1
        if (i=="@",i=="#",i=="$",i=="_"):
            special=special+1
    try:
        with open("userdetails.json","r") as output:
            data=json.load(output)
            for info in data["user"]:
                pass
    except:
        pass
    if lower>=1 and upper>=1 and special>=1 and digit>=1 and lower+upper+special+digit==len(password):
        confirm_password=input("enter your password to confirm")
        if password==confirm_password:
            if os.stat("userdetails.json").st_size==0:
                print("congratulation!",name,"your profile has been created successfully!")
                description=input("write about yourself")
                dob=input("enter your date of birth")
                sex=input("enter the gender")
                hobbies=input("enter the hobbies")
                try:
                    user_info["description"]=description
                    user_info["DOB"]=dob
                    user_info["Sex"]=sex
                    user_info["hobbies"]=hobbies
                    user_info["username"]=name
                    user_info["password"]=password
                    user_info["profile"]=user_info
                    list.append(dict_out)
                    main_dict["user"]=list
                    with open("userdetails.json","r+") as file:
                        read_file=file.read()
                        userdata=json.loads(read_file)
                        for j in userdata:
                            if j=="user":
                                x=userdata[i]
                                x.append(dict_out.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict.file)
                                file.close()
                except:
                    with open("userdetails.json","w") as f:
                        f.write(json.dumps(main_dict,indent=4))
            else:
                print("your account already exists!") 
        else:
            ("your password has not been attached")
    else:
        print("your password should contain one special character and one digit")
elif choose==2:
    name=input("enrer your username=")
    password=input("enter your Log in password=")
    with open("userdetails.json","r") as log_in_file:
        log_in_info=json.load(log_in_file)
        for output_data in log_in_info["user"]:
            if output_data["username"]== name and output_data["Password"]==password:
                print(name+ "you are logged in successfully")
                print("____________________")
                print("      Profile       ")
                print("____________________")
                print("username",":",output_data["username"])
                print("Gender",":",output_data["Profile"]["Sex"])
                print("Bio",":",output_data["Profile"]["description"])
                print("Dob",":",output_data["Profile"]["DOB"])
                print("hobbies",":",output_data["Profile"]["hobbies"])
                break
        else:
            print("password and username are invalid")




            
