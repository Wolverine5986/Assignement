class application():
    def __init__(self):
        self.add= "Succesfully added"
        self.delete = "User deleted Succesfully "
        self.update = "Succesfully Updated Your Data"
        self.error_msg = "Something Went Wrong"

    def add_user(self,data):
        self.data = data
        name = self.data["name"]
        email = self.data['email']
        password = self.data['password']
        user = {'name':name,'email':email,'password':password}
        return user
    


