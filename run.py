from secrets import password, clientSecret
from time import sleep
from prawcore.exceptions import RequestException, ServerError, ResponseException
from TwoWE4uBot import Bot

if __name__ == '__main__':
    westernBot = Bot(
    client_id = "6qC4n0Gzak1Kdh1RdqMGrA",
    client_secret = clientSecret,
    user_agent = "<2WE4uBot:v1.0.0>",
    username = "2WE4uBot",
    password = password
)

    while True:
        try:
            westernBot.run()

        except RequestException:
            print("RequestException")
            sleep(10)

        except ServerError:
            print("504 HTTP response")
            sleep(10)

        except ResponseException:
            print("500 HTTP response")
            sleep(10)