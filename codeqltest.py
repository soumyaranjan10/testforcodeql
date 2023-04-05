import random

# Define a function to generate a 4-digit OTP
def generate_otp():
    # Use the random module to generate a 4-digit number
    otp = random.randint(1000, 9999)
    return otp

# Call the function to generate an OTP
otp = generate_otp()

# Print the OTP
print("Your OTP is:", otp)
