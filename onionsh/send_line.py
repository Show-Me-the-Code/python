import requests

MAX_RETRIES = 5
WAIT_SECONDS = 5

def send_line(msg):
    url = 'https://notify-api.line.me/api/notify'
    token = 'jK2eWVxZ0X5wF9meRIWkq7zCjPnWswhjcfsRWYuyJT0'
    headers = {
                'content-type':
                'application/x-www-form-urlencoded',
                'Authorization':'Bearer '+token
            }
    for i in range(MAX_RETRIES):
        try:
            r = requests.post(url, headers=headers , data = {'message':msg})
            return r.text
        except requests.exceptions.ConnectionError:
            msg = 'build http connection failed'
            print(f"{msg}")

        except requests.exceptions.InvalidSchema:
            msg = 'No connection adapters were found'
            print(f"{msg}")

        except requests.exceptions.HTTPError as e:
            msg = f"{e}"
            print(f"{msg}")

        except requests.exceptions.ReadTimeout:
            msg = 'time out'
            print(f"{msg}")

    else:
        msg = 'all tries failed'
        print(f"{msg}")
        return None

if __name__ == "__main__":
    print(send_line('test'))