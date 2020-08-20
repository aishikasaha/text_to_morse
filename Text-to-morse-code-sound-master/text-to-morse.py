import time
from playsound import playsound



print("Seiling morse to sound converter v1.0")

# Addresses for dot and dash
dot = "noise/Dot.wav"

dash = "noise/Dash.wav"

converted_words = []

loop_tf = True
# Morse code variables
a = ".-"
b = "-..."
c = "-.-."
d = "-.."
e = "."
f = "..-."
g = "--."
h = "...."
i = ".."
j = ".---"
k = "-.-"
l = ".---"
m = "--"
n = "-."
o = "---"
p = ".--."
q = "--.-"
r = ".-."
s = "..."
t = "-"
u = "..-"
v = "...-"
w = ".--"
x = "-..-"
y = "-.--"
z = "--.."

one = ".----"
two = "..---"
three = "...--"
four = "....-"
five = "....."
six = "-...."
seven = "--..."
eight = "---.."
nine = "----."
zero = "-----"

space = " "


def let_to_morse(letters):
    if letters.lower() == "a":
        converted_words.append(a)
    elif letters.lower() == "b":
        converted_words.append(b)
    elif letters.lower() == "c":
        converted_words.append(c)
    elif letters.lower() == "d":
        converted_words.append(d)
    elif letters.lower() == "e":
        converted_words.append(e)
    elif letters.lower() == "f":
        converted_words.append(f)
    elif letters.lower() == "g":
        converted_words.append(g)
    elif letters.lower() == "h":
        converted_words.append(h)
    elif letters.lower() == "i":
        converted_words.append(i)
    elif letters.lower() == "j":
        converted_words.append(j)
    elif letters.lower() == "k":
        converted_words.append(k)
    elif letters.lower() == "l":
        converted_words.append(l)
    elif letters.lower() == "m":
        converted_words.append(m)
    elif letters.lower() == "n":
        converted_words.append(n)
    elif letters.lower() == "o":
        converted_words.append(o)
    elif letters.lower() == "p":
        converted_words.append(p)
    elif letters.lower() == "q":
        converted_words.append(q)
    elif letters.lower() == "r":
        converted_words.append(r)
    elif letters.lower() == "s":
        converted_words.append(s)
    elif letters.lower() == "t":
        converted_words.append(t)
    elif letters.lower() == "u":
        converted_words.append(u)
    elif letters.lower() == "v":
        converted_words.append(v)
    elif letters.lower() == "w":
        converted_words.append(w)
    elif letters.lower() == "x":
        converted_words.append(x)
    elif letters.lower() == "y":
        converted_words.append(y)
    elif letters.lower() == "z":
        converted_words.append(z)

    elif letters.lower() == "1":
        converted_words.append(one)
    elif letters.lower() == "2":
        converted_words.append(two)
    elif letters.lower() == "3":
        converted_words.append(three)
    elif letters.lower() == "4":
        converted_words.append(four)
    elif letters.lower() == "5":
        converted_words.append(five)
    elif letters.lower() == "6":
        converted_words.append(six)
    elif letters.lower() == "7":
        converted_words.append(seven)
    elif letters.lower() == "8":
        converted_words.append(eight)
    elif letters.lower() == "9":
        converted_words.append(nine)
    elif letters.lower() == "0":
        converted_words.append(zero)

    elif letters.lower() == " ":
        converted_words.append(space)

    elif letters.lower() == ".":
        converted_words.append("  ")
    else:
        print( letters + " Is not in morse code so it will not be included.")


print("Input the words you want to convert to morse code.")
phrase = input()

for char in phrase:
    let_to_morse(char)

run_up_to = len(converted_words)

times_ran = 0
while loop_tf == True:
    time_char_be = .3
    for x in converted_words[times_ran]:
        if x == ".":
            playsound(dot)
            time.sleep(time_char_be)
        elif x == "-":
            playsound(dash)
            time.sleep(time_char_be)
        elif x == " ":
            time.sleep(.8)

    # check to stop
    if times_ran == run_up_to - 1:
        loop_tf = False

    time.sleep(.3)
    times_ran += 1

print("Would you like to see the morse code(Y/N)")

yn = input()
if yn.lower() == "y":
    for y in converted_words:
        print(y)
else:
    print("Thank you for using Seiling morse to sound converter")
