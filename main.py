from dotenv import load_dotenv
from module.proj_01 import execute

def main():
    print("Hello from my-method!")

    execute()



if __name__ == "__main__":
    load_dotenv()
    main()
