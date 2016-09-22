'''
Created on Sep 22, 2016

@author: sonaje_a

Question
5)    Write a program to read accounts.xml file using python element tree. Also increment the balance of account by 20% if balance is less than 10 thousand.
'''
import xml.etree.ElementTree as ET

def read_xml_file():
    f = ET.parse("accounts.xml")
    root = f.getroot()
    for account in root:
        print(account.tag, ' - ', account.attrib)
        for child_elements in account:
            print(child_elements.tag,' - ',child_elements.text)
    #f.close()
        
def update_xml_file():
    f = ET.parse("accounts.xml")
    root = f.getroot()
    for account in root:
        #print(account.tag, ' - ', account.attrib)
        for child_elements in account:
            #print(child_elements.tag,' - ',child_elements.text)
            if child_elements.tag == 'balance' and int(child_elements.text) < 10000:
                child_elements.text = str(int(child_elements.text) + 0.2 * int(child_elements.text))
    
    for account in root:
        print(account.tag, ' - ', account.attrib)
        for child_elements in account:
            print(child_elements.tag,' - ',child_elements.text)
    
    f.write("accounts.xml")
    #f.close()
    
read_xml_file()
update_xml_file()