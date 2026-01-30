import requests


BASE_URL = "http://127.0.0.1:8000"


def ReturnApi(url, params=None):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.json())

    else:
        print("There's an error.")


def HelloWorld():
    url = f"{BASE_URL}/"
    ReturnApi(url)


def ItemsInput():
    item = int(input("Enter your integer item: "))

    url = f"{BASE_URL}/items/{item}"

    ReturnApi(url)


def ExtraInput():
    item = int(input("Enter your integer item: "))
    extra_item = input("Enter your extra item: ")

    url = f"{BASE_URL}/items/{item}"
    params = {"q": extra_item}

    ReturnApi(url, params)

if __name__ == "__main__":
    
    inp = input(str("Enter your choice: \n1.Hello world \n2.With items input \n3.with extra input \n"))

    match inp:
        case "1":
            HelloWorld()
        case "2":
            ItemsInput()
        case "3":
            ExtraInput()