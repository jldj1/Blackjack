from storage.storage import Storage

# We want only one instance of the "Database" throughout the application
# In real scenarios you would have only one database, in this case since we are making it
# I thought it would be better to have a single instance, or else we would have to create this "Database"
# in every file we use
 
# Storage(game_name, json_file)
storage_db = Storage("Tic Tac Toe", "storage.json")
