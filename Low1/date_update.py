from datetime import datetime
import time
def main():
    while True:

        now = datetime.now()
        

        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        

        print(formatted_now)

        time.sleep(5)

if __name__ == "__main__":
    main()