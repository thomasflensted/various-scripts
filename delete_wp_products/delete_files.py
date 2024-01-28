from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
PATH = "C:\THOMAS\coding\delete_files\chromedriver.exe"

def main():
        
    if len(sys.argv) == 1:

        sys.exit("Usage: delete_files.py [path/name of file with links]")

    else:

        link_file = sys.argv[1]

    # logs into fdaylife.dk admin page
    driver = wordpress_login("http://fdaylife.dk/wp-admin")
	
    # opens a txt file with all links to be processed and assigns it to a variable f
    f = open(link_file, "r")

    # counter set to 0 initialized to count number of links processed
    file_count = 0

    # loops through all links in txt file and passes each url to the delete_item function
    for url in f:

        delete_item(url, driver)
        file_count += 1

    # closes the browser and prints the number of links proessed to the screen
    driver.quit()

    if file_count == 1:

        print("\nProcess finished. 1 file was processed.")

    else:

        print("\nProcess finished. " + str(file_count) + " files were processed.")


def wordpress_login(link):

    # opens up wordpress and asks the user for username and password
    driver = webdriver.Chrome(PATH)
    driver.get(link)
    user = input("Mail address: ")
    pw = input("Password: ")

    # locates the password and username fields
    user_field = driver.find_element_by_id("user_login")
    password_field = driver.find_element_by_id("user_pass")
    login_button = driver.find_element_by_id("wp-submit")

    # puts the username given in the username field and the password
    # given in the password field and hits enter to complete the login
    user_field.send_keys(user)
    password_field.send_keys(pw)
    password_field.send_keys(Keys.RETURN)

    return driver

def delete_item(link, driver):

    # opens the link passed to the function, locates the edit button and clicks it
    driver.get(link)
    edit_button = driver.find_elements_by_class_name("post-edit-link")
    edit_button[0].click()

    # locates the delete button and clicks it
    delete_button = driver.find_element_by_id("delete-action")
    delete_button.click()

if __name__ == '__main__':
    main()
