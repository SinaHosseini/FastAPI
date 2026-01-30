import requests


def GetWeather(UrlStr: str ):
    try:
        Response = requests.get(UrlStr, timeout=10)

        response.raise_for_status()

        return Response
    
    except requests.exceptions.HTTPError as e:
        print("❌ HTTP Error:", e)

    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: مشکل در اتصال به سرور")

    except requests.exceptions.Timeout:
        print("❌ Timeout Error: سرور پاسخ نداد")

    except requests.exceptions.RequestException as e:
        print("❌ Request Error:", e)
    
    return None


if __name__ == "__main__":
    InputUser = input(str("Enter tour city: "))

    UrlStr = f"https://goweather.herokuapp.com/weather/{InputUser}"

    response = GetWeather(UrlStr)

    if response:
        print(response.json())