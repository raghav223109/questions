try:
    with open("59.txt","w") as file:
        file.write("Raghuvendra kumar")

    with open("59.txt","r")as file:
        print(file.read())

except FileNotFoundError:
    print("file is not found")
except Exception as e:
    print(e)

finally:
    print("operations done")
