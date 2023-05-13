import sys
import book_dao

# options that will be printed for the
# user to select from in the main menu
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

# search options that will be printed for the user to
# select from upon selecting option 5 in the main menu
search_menu_options = {
    1: 'All Books',
    2: 'By Title',
    3: 'By ISBN',
    4: 'By Publisher',
    5: 'By Price Range',
    6: 'By Year',
    7: 'By Title and Publisher',
    8: 'Back to Main Menu'
}

# searches for and prints out 
# all books in the database
def search_all_books():
    
    # Use a data access object (DAO) to 
    # abstract the retrieval of data from 
    # a data resource such as a database.
    results = book_dao.findAll()

    # Display results
    print()
    print("The following are the ISBNs, titles, years, publishers, previous edition ISBNs, and prices of all books.")
    for item in results:
        print("%s, %s, %s, %s, %s, %s" %(item[0],item[1],item[2],item[3],item[4],item[5]))
    print("The end of books.")
    print()


# searches for and prints out all
# books in the database with the 
# title entered by the user
def search_by_title():
    title = ''

    # get title from user
    try:
        title = input('Enter book title (or enter \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)

    # handle function exit
    if(title == '-1'):
        print("Returning to search options menu")
    
    # or execute search
    else:
        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        titleResults = book_dao.findByTitle(title)

        # Display results
        print()
        print("The following are the ISBNs, years, publishers, previous edition ISBNS, and prices of all books titled %s." %title)
        for item in titleResults:
            print("%s, %s, %s, %s, %s" %(item[0],item[2],item[3],item[4],item[5]))
        print("The end of books.")
        print()

# searches for and prints out the
# book in the database with the 
# ISBN entered by the user, if
# one exists
def search_by_ISBN():
    isbn = ''

    # get ISBN from user
    try:
        isbn = input('Enter book ISBN (10 digits) (or enter \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)

    # handle function exit
    if(isbn == -1):
        print("Returning to search options menu")

    # or execute search
    else:
        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        isbnResults = book_dao.findByISBN(isbn)

        # Display results
        print()
        print("The following are the titles, years, publishers, previous edition ISBNs, and prices of all books with ISBN %s" %isbn)
        for item in isbnResults:
            print("%s, %s, %s, %s, %s" %(item[1],item[2],item[3],item[4],item[5]))
        print("The end of books.")
        print()

# searches for and prints out all
# books in the database published 
# by the publisher with the name
# supplied by the user
def search_by_publisher():
    publisher = ''

    # get publisher name from user
    try:
        publisher = input('Enter publisher name (or enter \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)

    # handle function exit
    if(publisher == "-1"):
        print("Returning to search options menu")
    
    # or execute search
    else:
        
        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        publisherResults = book_dao.findByPublisher(publisher)

        # Display results
        print()
        print("The following are the ISBNs, titles, years, previous edition ISBNs and prices of all books published by %s." %publisher)
        for item in publisherResults:
            print("%s, %s, %s, %s, %s" %(item[0],item[1],item[2],item[4],item[5]))
        print("The end of books.")
        print()

# searches for and prints out all
# books in the database within the
# price range indicated by the user
def search_by_price_range():
    lowprice = ''
    highprice = ''

    # get the minimum price
    # and ensuring that a 
    # decimal number is entered
    # via while-true loop
    while(True):
        try:
            lowprice = float(input('Enter minimum price (decimal format) (or enter \'-1.0\' to go back): '))
            break
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
        except:
            print('Wrong input. Please enter a decimal number ...')
    
    # handle function exit
    if(lowprice == -1.0):
        print("Returning to search options menu")
    
    # or continue executing search
    else:
        
        # get the maximum price
        # while ensuring that a 
        # decimal number is entered
        # via while-true loop
        while(True):
            try:
                highprice = float(input('Enter maximum price (decimal format): '))
                break
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)
            except:
                print('Wrong input. Please enter a decimal number ...')

        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        priceResults = book_dao.findByPriceRange(lowprice, highprice)

        # Display results
        print()
        print("The following are the ISBNs, titles, years, publishers, previous edition ISBNs and prices of all books ranging in price from %.2f to %.2f." %(lowprice, highprice))
        for item in priceResults:
            print("%s, %s, %s, %s, %s, %s" %(item[0],item[1],item[2],item[3],item[4],item[5]))
        print("The end of books.")
        print()

# searches for and prints out all
# books in the database published in
# the year entered by the user
def search_by_year():
    year = ''

    # get publishing year from user
    # while ensuring that an integer
    # is entered via while-true loop
    while(True):
        try:
            year = int(input('Enter year (Format: YYYY) (or enter \'-1\' to go back): '))
            break
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
        except:
            print('Wrong input. Please enter a year in format YYYY')

    # handle function exit
    if(year == -1):
        print("Returning to search options menu")

    # otherwise execute search
    else:


        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        yearResults = book_dao.findByYear(year)

        # Display results
        print()
        print("The following are the ISBNs, titles, publishers, previous edition ISBNS and prices of all books published in %d." %year)
        for item in yearResults:
            print("%s, %s, %s, %s, %s" %(item[0],item[1],item[3],item[4],item[5]))
        print("The end of books.")
        print()

# searches for and prints out all
# books in the database with the 
# title and publisher name indicated
# by the user
def search_by_title_and_publisher():
    title = ''
    publisher = ''

    # get book title from user
    try:
        title = input('Enter book title (or enter \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)
    
    # handle function exit
    if(title == '-1'):
        print("Returning to search options menu")
    
    # or else continue executing search
    else:
        # get publisher name from user
        try:
            publisher = input('Enter book publisher name: ')
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
    
        # Use a data access object (DAO) to 
        # abstract the retrieval of data from 
        # the database
        titlePublisherResults = book_dao.findByTitleAndPublisher(title, publisher)

        # Display results
        print()
        print("The following are the ISBNs, years, previous edition ISBNS, and prices of all books titled %s and published by %s" %(title, publisher))
        for item in titlePublisherResults:
            print("%s, %s, %s, %s" %(item[0],item[2],item[4],item[5]))
        print("The end of books.")
        print()

# prints the program's main menu 
def print_menu():
    print()
    print('--------------------------------------------Book Manager Software-------------------------------------------')
    for key in menu_options.keys():
        print (str(key)+'.', menu_options[key], end = "  ")
    print()

# prints the search options menu upon selecting option 5 in the main menu
def print_search_menu():
    print()
    print('---------------------------------------------Search Options Menu--------------------------------------------')
    for key in search_menu_options.keys():
        print (str(key)+'.', search_menu_options[key], end = "  ")
    print()

# adds a publisher to the database
# with the name, phone number, and
# city indicated by the user
def add_publisher():
    name = ''
    phone = ''
    city = ''

    # get publisher name
    try:
        name = input('Enter publisher name (or enter \'-1\' to go back) (required): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)

    # handle function exit
    if(name == "-1"):
        print("Returning to main menu")

    # otherwise continue
    else:
        
        # confirm that the publisher name does not 
        # already exist in the database before
        # continuing process
        results = book_dao.checkPublisher(name)
        if results:
            while(True):
                try:
                    name = input('Publisher already exists! Please enter a different name (or \'-1\' to go back) (required): ')
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                if(name == "-1"):
                    break
                elif book_dao.checkPublisher(name):
                    continue
                else:
                    break

        # handle function exit
        if(name == "-1"):
            print("Returning to main menu")
        
        # otherwise continue
        else:

            # get publisher phone number
            try:
                phone = input('Enter publisher phone number: ')
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # get publisher city
            try:
                city= input('Enter publisher city: ')
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # Use a data access object (DAO) to 
            # abstract the insertion of data into 
            # the database
            book_dao.addPublisher(name, phone, city)
            print("Publisher added to database!")

# adds a book to the database with
# the ISBN, title, year, price,
# previous edition ISBN, and 
# publisher name indicated by 
# the user
def add_book():
    ISBN = ''
    title = ''
    year = ''
    published_by = ''
    previous_edition=''
    price = ''

    # get book ISBN from user
    try:
        ISBN = input('Enter book ISBN (10 digits) (or enter \'-1\' to go back) (required): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)

    # handle function exit
    if(ISBN == "-1"):
        print("Returning to main menu")

    # otherwise continue function
    else:
        # verify that this ISBN is unique
        result = book_dao.checkISBN(ISBN)
        if result:
            while(True):
                try:
                    ISBN = input('ISBN already exists in database! Please enter a new ISBN (10 digits) (or \'-1\' to go back) (required): ')
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                if ISBN != "-1" and book_dao.checkISBN(ISBN):
                    continue
                else:
                    break
        
        # handle function exit
        if(ISBN == "-1"):
            print("Returning to main menu")

        # otherwise continue function
        else:
            # get book title from user
            try:
                title = input('Enter book title: ')
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # get publishing year from user
            # and ensure that an integer is
            # entered via while-true loop
            while(True):
                try:
                    year = int(input('Enter year (Format: YYYY): '))
                    break
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                except:
                    print('Wrong input. Please enter a year in format YYYY ...')

            # get publisher name from user
            try:
                published_by= input('Enter publisher name (Enter \'null\' if none): ')
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # confirm that the publisher name
            # matches an existing publisher in
            # the database before continuing
            if(published_by != "null"):
                results = book_dao.checkPublisher(published_by)
                if not results:
                    while(True):
                        try:
                            published_by= input('Please enter an existing publisher name (Enter \'null\' if none): ')
                        except KeyboardInterrupt:
                            print('Interrupted')
                            book_dao.closeConnection()
                            sys.exit(0)
                        if published_by != 'null' and not book_dao.checkPublisher(published_by):
                            continue
                        else:
                            break

            # get previous edition ISBN from user
            try:
                previous_edition= input('Enter previous ISBN (10 digits) (Enter \'null\' if none): ')
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # confirm that the previous ISBN exists
            # in the database before continuing
            if(previous_edition != "null"):
                results = book_dao.checkISBN(previous_edition)
                if not results:
                    while(True):
                        try:
                            previous_edition= input('Please enter an existing ISBN (10 digits) (Enter \'null\' if none): ')
                        except KeyboardInterrupt:
                            print('Interrupted')
                            book_dao.closeConnection()
                            sys.exit(0)
                        if previous_edition != 'null' and not book_dao.checkISBN(previous_edition):
                            continue
                        else:
                            break

            # get book price from user
            # and ensure that a decimal
            # number is entered via
            # while-true loop
            while(True):
                try:
                    price = float(input('Enter price: '))
                    break
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                except:
                    print('Wrong input. Please enter a decimal number ...')

            # Use a data access object (DAO) to 
            # abstract the insertion of data into 
            # the database
            book_dao.addBook(ISBN, title, year, published_by, previous_edition, price)
            print("Book added to database!")

# edits the book indicated by
# the user via ISBN by prompting
# new attribute values for the book
# to be edited which are then
# supplied to the DAO
def edit_book():

    # retrieve and print out all books 
    # for the user to choose from
    results = book_dao.findAll()


    print("The following are the ISBNs, titles, years, publishers, previous edition ISBNs, and prices of all books.")
    for item in results:
        print("%s, %s, %s, %s, %s, %s" %(item[0],item[1],item[2],item[3],item[4],item[5]))

    try:
        ISBN = input('Enter the ISBN of the book you would like to edit (10 digits) (or \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)
    
    # handle function exit
    if(ISBN == '-1'):
        print("Returning to main menu")

    # otherwise continue
    else:
        
        # confirm that the user enters 
        # an ISBN that already exists
        # in the database
        prevInfo = book_dao.checkISBN(ISBN)
        if not prevInfo:
            while(True):
                try:
                    ISBN = input('Please enter an existing ISBN (10 digits) (or \'-1\' to go back): ')
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                if ISBN != '-1' and not book_dao.checkISBN(ISBN):
                    continue
                elif ISBN != '-1':
                    prevInfo = book_dao.checkISBN(ISBN)
                    break
                else:
                    break
        
        # handle function exit
        if(ISBN == '-1'):
            print("Returning to main menu")

        # otherwise continue
        else:
            # get updated book ISBN
            try:
                newISBN = input('Enter new book ISBN (required) (Original ISBN: {0}): '.format(prevInfo[0][0]))
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # get updated book title
            try:
                newTitle = input('Enter updated book title (Original title: %s): ' %prevInfo[0][1])
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # get updated book year from user
            # and enforce that a number is 
            # entered via while-true loop
            while(True):
                try:
                    newYear = int(input('Enter updated new year (Format: YYYY) (Original year: %s): ' %prevInfo[0][2]))
                    break
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                except:
                    print('Wrong input. Please enter a year in format YYYY ...')

            # get updated publisher name from user
            try:
                newPublished_by= input('Enter updated publisher name (Enter \'null\' if none) (Previous publisher: %s): ' %prevInfo[0][3])
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # confirm that the publisher
            # name exists in the database
            # before continuing
            if(newPublished_by != "null"):
                results = book_dao.checkPublisher(newPublished_by)
                if not results:
                    while(True):
                        try:
                            newPublished_by= input('Please enter an existing publisher name (Enter \'null\' if none) (Previous publisher: %s): ' %prevInfo[0][3])
                        except KeyboardInterrupt:
                            print('Interrupted')
                            book_dao.closeConnection()
                            sys.exit(0)
                        if newPublished_by != 'null' and not book_dao.checkPublisher(newPublished_by):
                            continue
                        else:
                            break
    
            # get updated previous edition ISBN from user
            try:
                newPrevious_edition= input('Enter updated previous ISBN (10 digits) (Enter \'null\' if none) (Previous ISBN: %s): ' %prevInfo[0][4])
            except KeyboardInterrupt:
                print('Interrupted')
                book_dao.closeConnection()
                sys.exit(0)

            # confirm that the previous ISBN
            # exists in the database before
            # continuing
            if(newPrevious_edition != "null"):
                results = book_dao.checkISBN(newPrevious_edition)
                if not results:
                    while(True):
                        try:
                            newPrevious_edition= input('Please enter an existing ISBN (10 digits) (Enter \'null\' if none) (Previous ISBN: %s): ' %prevInfo[0][4])
                        except KeyboardInterrupt:
                            print('Interrupted')
                            book_dao.closeConnection()
                            sys.exit(0)
                        if newPrevious_edition != 'null' and not book_dao.checkISBN(newPrevious_edition):
                            continue
                        else:
                            break
            # get updated book price from user
            # and enforce decimal number entry
            # via while-true loop
            while(True):
                try:
                    newPrice= float(input('Enter updated price (decimal format) (previous price: %s): ' %prevInfo[0][5]))
                    break
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                except:
                    print('Wrong input. Please enter a decimal number ...')
        
            # Use a data access object (DAO) to 
            # abstract the updating of data in 
            # the database
            book_dao.editBook(ISBN, newISBN, newTitle, newYear, newPublished_by, newPrevious_edition, newPrice)
            print("Book info updated in database!")
    
# deletes the book indicated by
# the user via ISBN from the 
# database
def delete_book():

    # retrieve and print out the books 
    # for the user to choose from
    results = book_dao.findAll()

    print("The following are the ISBNs, titles, years, publishers, previous edition ISBNs, and prices of all books.")
    for item in results:
        print("%s, %s, %s, %s, %s, %s" %(item[0],item[1],item[2],item[3],item[4],item[5]))
    
    try:
        ISBN = input('Enter the ISBN of the book you would like to delete (10 digits) (or \'-1\' to go back): ')
    except KeyboardInterrupt:
        print('Interrupted')
        book_dao.closeConnection()
        sys.exit(0)
    
    # handle function exit
    if(ISBN == '-1'):
        print("Returning to main menu")

    # otherwise continue
    else:
        # first confirm the book ISBN exists
        results = book_dao.checkISBN(ISBN)
        if not results:
            while(True):
                try:
                    ISBN = input('Please enter an existing ISBN (10 digits) (or \'-1\' to go back): ')
                except KeyboardInterrupt:
                    print('Interrupted')
                    book_dao.closeConnection()
                    sys.exit(0)
                if ISBN != '-1' and not book_dao.checkISBN(ISBN):
                    continue
                else:
                    break

        # handle function exit
        if(ISBN == '-1'):
            print("Returning to main menu")
        
        # otherwise continue
        else:
            # Use a data access object (DAO) to 
            # abstract the deletion of data in 
            # the database
            book_dao.deleteBook(ISBN)
            print("Book deleted from database!")


# prints out and directs the
# user to the search option menu
def option5():
    
    # A sub-menu shall be printed
    # and prompt user selection
    while(True):
        print_search_menu()
        try:
            searchOption = int(input("Please select a function, type [1-8] and press enter: "))
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if searchOption == 1:
            search_all_books()
        elif searchOption == 2:
            search_by_title()
        elif searchOption == 3:
            search_by_ISBN()
        elif searchOption == 4:
            search_by_publisher()
        elif searchOption == 5:
            search_by_price_range()
        elif searchOption == 6:
            search_by_year()
        elif searchOption == 7:
            search_by_title_and_publisher()
        elif searchOption == 8:
            print('Returning to main menu')
            break
        else:
            print('Invalid option. Please enter a number between 1 and 8.')


# prints out and navigates the
# user to the main menu
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input("Please select a function, type [1-6] and press enter: "))
        except KeyboardInterrupt:
            print('Interrupted')
            book_dao.closeConnection()
            sys.exit(0)
        except:
            print('Wrong input. Please enter a number ...')

        # Check what choice was entered and act accordingly
        if option == 1:
            add_publisher()
        elif option == 2:
            add_book()
        elif option == 3:
            edit_book()
        elif option == 4:
            delete_book()
        elif option == 5:
            option5()
        elif option == 6:
            print('Thank you for using our database services! Bye')
           
            # close the connection to the database
            book_dao.closeConnection()
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 6.')

