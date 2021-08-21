"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        self.table.append(string)
        # Your code goes here
        # pass
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        if(string in self.table):
            return HashTable.calculate_hash_value(self,string)
        # pass
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        val = 0 
        cnt = 0
        for i in string:
            if(cnt==0):
                val+=ord(i)*100
            elif(cnt==1):
                val+=ord(i)
                break
            cnt+=1
        return val
        # pass


