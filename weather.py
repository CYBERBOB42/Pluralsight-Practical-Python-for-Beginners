temperature = 79
forecast = "sunny"
raining = True

if temperature < 80 or forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")

if temperature < 80 and forecast != "rain":
    print("Go outside!")
else:
    print("Stay inside!")

if not forecast == "rain":
    print("Go outside!")
else:
    print("Stay inside!")

if raining:
    print("Stay inside!")
else:
    print("Go outside!")

if not raining:
    print("Go outside!")
else:
    print("Stay inside!")

print("have a good day!")