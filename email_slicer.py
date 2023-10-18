def main():
    print("welcome to the email slicer")
    print("")

    email_input = input("Enter you email address:")

    (username,domain)=email_input.split("@")
    (domain,extension)=domain.split(".")

    print("Username :", username)
    print("Domain :", domain)
    print("Estension :", extension)

while True:
  main()    
