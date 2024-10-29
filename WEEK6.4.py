
def askuser(message):
    answer = input(message)
    return answer

def main():
    answer = askuser("What do you want to do next?")
    if answer.casefold() == 'nothing':
        print("No fun!")
        print(askuser("What is our favorite color?"))

    if __name__ == "__main__":
     main()