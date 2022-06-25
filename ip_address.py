import socket as s


def ip_address():
    # taking user input
    inp = input("Do you want system IP Address ? (y/n) ")

    if inp in ["y", "Y"]:
        print("Your Host name is ", s.gethostname())
        print("IP Address ",s.gethostbyname(s.gethostname()))
    else:
        inp = input("Enter the URL of site ")
        ip = s.gethostbyname(inp)
        print("IP Address ", ip)
    
if __name__=="__main__":
    ip_address()

