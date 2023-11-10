from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or access a database
db = client['example_database']

# Create or access a collection (similar to a table in relational databases)
collection = db['users']

# Create data (Insert)
user_data = [
    {"name": "Eniolorunfe Oladapo", "age": 22},
    {"name": "Gideon Ihonre", "age": 25}
]
result = collection.insert_many(user_data)
print("Inserted IDs:", result.inserted_ids)

# Read data (Retrieve)
all_users = collection.find()
print("\nAll Users:")
for user in all_users:
    print(user)

# Update data
query = {"name": "Eniolorunfe Oladapo"}
new_values = {"$set": {"age": 23}}
collection.update_one(query, new_values)
print("\nUser 'Eniolorunfe Oladapo' updated.")

# Modify data (Update)
query = {"name": "Eniolorunfe Oladapo"}
new_values = {"$set": {"name": "Enioluwa Oladapo"}}
collection.update_one(query, new_values)
print("\nUser 'Eniolorunfe Oladapo' modified to 'Enioluwa Oladapo'.")

# Read data after modification
all_users_after_update = collection.find()
print("\nAll Users After Update:")
for user in all_users_after_update:
    print(user)

# Delete data
query = {"name": "Enioluwa Oladapo"}
collection.delete_one(query)
print("\nUser 'Enioluwa Oladapo' deleted.")

# Read data after deletion
all_users_after_deletion = collection.find()
print("\nAll Users After Deletion:")
for user in all_users_after_deletion:
    print(user)