from Databaseworker import databaseWorker
from User import user

from werkzeug.security import generate_password_hash, check_password_hash

class auth():

    @staticmethod
    def authenticate(dbw: databaseWorker, user: user) -> bool|user:
        while(True):
            choice = int(input("1-LogIN/2-Create new account"))

            if choice == 1:
                login = input("Provide loging: ")
                password = input("Provide password: ")
                if dbw.logIntoUser(login, password):
                    user.setLogin(login) 
                    user.setPassword(generate_password_hash(password)) 
                    user.setActiveness(True)
                    return True, user
                else:
                    print("TRY AGAIN")
                    #return False, user
            elif choice == 2:
                login = input("Provide loging: ")
                password = input("Provide password: ")
                dbw.createUser(login, password)
                
                user.setLogin(login)
                user.setPassword(generate_password_hash(password))
                user.setActiveness(True)

                return True, user
            else:
                print("WRONG INPUT")
                #return False, user
