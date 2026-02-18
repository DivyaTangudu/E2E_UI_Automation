# create_test_data.py
import pandas as pd

# Define multiple sets of test data
data = [
    {
        "username": "testuser1",
        "email": "user1@gmail.com",
        "password": "Test@123",
        "first_name": "John",
        "last_name": "Doe",
        "company": "ABC Ltd",
        "address": "Hyderabad",
        "country": "India",
        "state": "Telangana",
        "city": "Hyderabad",
        "zipcode": "500081",
        "mobile_number": "9493381298",
        "dob": "1992-09-12"
    },
    {
        "username": "testuser2",
        "email": "user2@gmail.com",
        "password": "Test@456",
        "first_name": "Alice",
        "last_name": "Smith",
        "company": "XYZ Inc",
        "address": "Mumbai",
        "country": "India",
        "state": "Maharashtra",
        "city": "Mumbai",
        "zipcode": "400001",
        "mobile_number": "9123456789",
        "dob": "1995-05-23"
    },
    {
        "username": "testuser3",
        "email": "user3@gmail.com",
        "password": "Test@789",
        "first_name": "Bob",
        "last_name": "Johnson",
        "company": "LMN Pvt",
        "address": "Bangalore",
        "country": "India",
        "state": "Karnataka",
        "city": "Bangalore",
        "zipcode": "560001",
        "mobile_number": "9876543210",
        "dob": "1990-12-15"
    }
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel in a 'data' folder
df.to_excel("data/test_data.xlsx", index=False)
print("Excel test data created successfully in 'data/test_data.xlsx'")