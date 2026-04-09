import xmlrpc.client

# Connect to server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Input from user
num = int(input("Enter a number: "))

# Call remote function
result = server.factorial(num)

# Output result
print("Factorial of", num, "is:", result)