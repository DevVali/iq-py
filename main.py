print("<=> IQ COMPARATOR <=>")

name = [input("What is the name of the first user?: "), input("What is the name of the second user?: ")]
iq = [input("What is the IQ of the first user?: "), input("What is the IQ of the second user?: ")]

if iq[0] > iq[1]:
    print(f"The IQ of {name[0]} is higher than {name[1]}'s IQ.")
elif iq[0] < iq[1]:
    print(f"The IQ of {name[1]} is higher than {name[0]}'s IQ.")
elif iq[0] == iq[1]:
    print("The IQ of both users is same.")
else:
    print("Somewhere, an unexpected error has happened.")