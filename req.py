from requests import put, get

while True:
    route = input("masukkan route url: ")
    url = f"http://127.0.0.1:5000{route}"
    if route == "":
        print("masukkan ulang")
        continue    
    else:
        break

while True:
    put_data = input("masukkan data: ")
    if put_data == "":
        valid = input("yakin? (y/n): ")
        if valid == "y" :
            break
        else:
            print("masukkan lagi")
            continue
    else:
        break          
            
put(url, data={"data":put_data})


if __name__ == "__main__":
    print(f"data diambil api {route}:",get(url).json())