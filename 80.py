# safe atm System 

print("="*30)
print("Safe Banking System")
print("="*30 + "\n")

Balance = 500000
print("Balance : ", Balance)
print("\n")

try:
    userAmount = int(input("enter amount you want to withdraw: "))
    if userAmount > Balance:
        print("Insufficient Balance")
    elif userAmount <= 0:
        print("Invalid Amount")
    else:
        Balance -= userAmount
        print("withdrawal successful")
        print("remaining balance : ", Balance)
except ValueError:
    print("Invalid input. Please enter a valid amount")
except Exception as e:
    print("an error occurred : ", e)

print("\nThank you for using Safe Baning System")

print("program ended here")    