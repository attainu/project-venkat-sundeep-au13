class DriverRegistration:
    
    def __init__(self, fullname, age, licence,experience, email, mobile, password):

        self.fullname = fullname
        self.age = age
        self.drivinglicence = licence
        self.experience = experience
        self.email  = email
        self.mobile = mobile
        self.createpassword = password
    
    def createAccount(self):
        
        return " Account Created "
         

if __name__ == "__main__":
    
    # Input for registration

    if create == 1:
        print(driver.createAccount())
    else: 
        print('Failed, Please Register again')


    driver   = DriverRegistration('Venkat sundeep', 24, 'YES', 1, 'sunnny@gmail.com', 999999, 'password')

    print("hello",driver.fullname, "Welcome to  MyCABS")