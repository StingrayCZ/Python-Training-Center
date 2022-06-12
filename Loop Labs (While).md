# Loop Labs (While)


```Py
secrete_words = "giraffe"

guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secrete_words and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")

```


```Py
while True:
    number = float(input("Enter a number:"))
    if number < 0:
        break
        print("You entered", number)
print("End")
```