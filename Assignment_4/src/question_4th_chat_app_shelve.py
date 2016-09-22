'''
Created on Sep 20, 2016

@author: sonaje_a

Question
4)    Upgrade console based chatting application to save information about chat rooms, users, messages into a file so that even though we restart the chatting application, the data about chat rooms, users & messages will be still available. (Use shelve module)
'''
import collections
import shelve
users = {'abc':'abc'}
chatroom = ''
i = 0

def chat_data_write_file():
    global users
    global chatroom
    global i
    
    f = shelve.open('chat_data.dat')
    f['users'] = users
    f['chatroom'] = chatroom
    f['i'] = i
    f.close()
    print('Storing of chat data is done')

def chat_data_read_file():
    global users
    global chatroom
    global i
        
    f = shelve.open('chat_data.dat')
    users = f['users']
    chatroom = f['chatroom']
    i = f['i']
    f.close()
    print('reading of chat data is done')


def addusertochatroom():
    global chatroom
    uname = input('\nEnter user name: ')
    if  chatroom.get(uname) == None:
        chatroom[uname] = []
        print ("\nAdded user successfully.\n")
    else:
        print ("\nUser Exists!\n")
        
    chat_data_write_file()
            
def deleteuserfromchatroom():
    global chatroom
    uname = input('\nEnter user name: ')
    if (chatroom.get(uname) == ''):
        print ("\nUser does not Exist.\n")
    else:
        del chatroom[uname]
        print ("\nUser Deleted successfully.\n")
    chat_data_write_file()


options2 = {'A' : addusertochatroom,
           'B' : deleteuserfromchatroom,
}


def createchatroom():
    #print ("You typed createcahtroom.\n")
    global chatroom
    if(chatroom == ''):
        chatroom = collections.defaultdict(list)
        print ("\nchatroom created successfully.\n")
    else:
        print('\nchatroom already created.\n')
    while True:
        print('Choose Option: ')
        print('\tA) Add user to chatroom')
        print('\tB) Delete User from chatroom')
        print('\tC) Exit')
        ch = input()
        if( ch == 'C'):
            break
        else:
            options2[ch]()
            
def sendmsg(uname):
    global chatroom
    global i
    str = input('Enter message: ')
    i += 1    
    l = chatroom[uname]
    l.append((i,uname,str))
    chat_data_write_file()
    
def displaymsg(uname):
    global chatroom
    listmsg = []
    for i in chatroom.values():
        #print("i:",i)
        for z in i:
            #print("z:",z)
            listmsg.append(z)
    #print(chatroom)
    #print(listmsg)
    listmsg.sort(key= lambda tup:tup[0])
    for i in listmsg:
            print(i[1],":",i[2])
                
def displayusers(uname):
    global chatroom
    for i in chatroom.keys():
        print(i)

options3 = {'A' : sendmsg,
           'B' : displaymsg,
           'C' : displayusers,
}    

def userlogin():
    global chatroom
    global users
    if(chatroom == ''):
        print('\nFirst Create chatroom')
    else:
        uname = input('Enter the username: ')
        password = input('Enter Password: ')
        if(users.get(uname) == None):
            print ("Username does not exists.\n")
        else:
            if(users.get(uname) == password):
                print ("User is logged in.\n")
                while True:
                    print('Choose Option: ')
                    print('\tA) Send Messages')
                    print('\tB) Display Messages')
                    print('\tC) List down Users')
                    print('\tD) Logout')
                    ch = input()
                    if( ch == 'D'):
                        break
                    else:
                        options3[ch](uname)

def deletechatroom():
    global chatroom
    if (chatroom == ''):
        print ("You didn't create any chatroom.\n")
    else:
        chatroom = ''
        print ("Deleted chatroom successfully.\n")
    chat_data_write_file()

def adduser():
    global chatroom
    global users
    if(chatroom == ''):
        print('\nFirst Create chatroom')
    else:
        uname = input('Enter username: ')
        password = input('Enter password: ')
        if(chatroom.get(uname) == None):
            print('User is not present in chatroom')
        else:
            if users.get(uname) == None:
                users[uname] = password
                #print(users)
                print('User added successfully.')
            else:
                print('User already exists!')
    chat_data_write_file()
    
# map the inputs to the function blocks
options1 = {'A' : createchatroom,
           'B' : userlogin,
           'C' : deletechatroom,
           'D' : adduser,
           'E' : chat_data_read_file
}

print('=============================Chat Application=============================')

while True:
    print('Choose Option: ')
    print('\tA) Create a chatroom')
    print('\tB) User login')
    print('\tC) Delete an Chatroom')
    print('\tD) Add user')
    print('\tE) Read Chat Data')
    print('\tF) Exit and to store chat data')
    ch = input()
    if( ch == 'F'):
        break
    else:
        options1[ch]()

chat_data_write_file()

