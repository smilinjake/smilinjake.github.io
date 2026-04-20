# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # USER = 'aacuser' 
        USER = username 
        PASS = password
        # PASS = 'admin' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        
        # indexing the database on rec_num to make sorting by rec_num more efficient
        self.collection.create_index([("rec_num", -1)])

    # Create a method to return the next available record number for use in the create method
    def find_next(self):
        max_record = self.collection.find_one(
            filter={}, # The empty filter will match all documents
            sort=[("rec_num", -1)],
            projection={"rec_num":True}
        )
        if max_record:
        # Accessing the 'rec_num' value directly from the dictionary and incrementing
            return max_record.get("rec_num") + 1
    

    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        try:
            # Checking if all of the keys are truthy. 
            # Creating a record with a falsy key would raise an exception.
            if all(data.keys()): 
                result =  self.collection.insert_one(data)  # data should be dictionary
                # Checking if data was successfully added and returning True or False 
                return result.acknowledged 
            else:
                print("    Exception Caught Before Thrown:  Nothing to save, because data parameter is empty") 
                # Returning False if an exception would have occurred,
                # due to someone attempting to create a record with a falsy key
                return False 
        except: 
            print("A Fatal Error Occurred") 


    # Create method to implement the R in CRUD.
    def read(self, data):
        try:
            # Checking if all of the keys are truthy. 
            # Searching a falsy key would raise an exception.
            if all(data.keys()): 
                response = self.collection.find(data)
                # return response
                if response:
                    # Casting the response cursor to a list makes the result printable, 
                    # however it can cause memory issues if large datasets are expected to be returned. 
                    return list(response)
                    # Note to Professor: If you would prefer read() to return a list of cursor objects
                    # I can re write the definition to append them to a defined list variable and allow  
                    # for casting to be done on the other side. 
                elif data == {}:
                    # response = self.collection.find({})
                    return response
                else:
                    return []
            else:
                return []
        except:
            print("A Fatal Error Occurred") 

    # Update method to implement the U in CRUD
    def update(self, query, data):
        try:
            # Checking if all of the keys are truthy. 
            # Searching a falsy key would raise an exception.
                # We need to check both the query and the update data for truthy values so that we do not
                # break an existing record, or throw an exception when searching. 
            if all(data.keys()) and all(query.keys()): 
                response = self.collection.update_many(query, {"$set": data})
                return response.modified_count
            else: 
                print("    Exception Caught Before Thrown:  Nothing to Update, because data parameter is empty")
        except:
            print("A Fatal Error Occurred")
    
    # Delete method to implement the D in CRUD
    def delete(self, data):
        try:
            # Checking if all of the keys are truthy. 
            # Searching a falsy key would raise an exception.
            if all(data.keys()): 
                response = self.collection.delete_many(data)
                return response.deleted_count
            else:
                print("    Exception Caught Before Thrown:  Nothing to Delete, because data parameter is empty")
        except:
            print("A Fatal Error Occurred")