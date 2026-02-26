mood = input("How are you?: ")
def greet():
    print("good morning sir,")
    if mood in {"fine", "good", "happy", "ok"}:
        print("glad to hear that")
    else:
        print("tell me how can i help to fix that, gentleman")