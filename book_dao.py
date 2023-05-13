from mysql_connector import connection

# returns all books from the Book table
def findAll():
    cursor = connection.cursor()
    query = "select * from bookmanager.Book"
    cursor.execute(query)
    results = cursor.fetchall()
    return results
    
# returns books from the Book table that have the indicated title
def findByTitle(title):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title=%s"
    cursor.execute(query, (title,))
    results = cursor.fetchall()
    return results

# returns the book from the Book table that has the 
# indicated ISBN (if one exists)
def findByISBN(isbn):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where ISBN=%s"
    cursor.execute(query, (isbn,))
    results = cursor.fetchall()
    return results

# returns books from the Book table that were published by the 
# indicated publisher (publisher name provided)
def findByPublisher(publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where published_by=%s"
    cursor.execute(query, (publisher,))
    results = cursor.fetchall()
    return results

# returns books from the Book table that were published 
# in the indicated year
def findByYear(year):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where year=%s"
    cursor.execute(query, (year,))
    results = cursor.fetchall()
    return results

# returns books from the Book table within the indicated 
# price range (lowprice to highprice, inclusive)
def findByPriceRange(lowprice, highprice):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where price >= %s and price <= %s"
    cursor.execute(query, (lowprice,highprice))
    results = cursor.fetchall()
    return results

# returns books from the Book table with the 
# indicated title and publisher
def findByTitleAndPublisher(title, publisher):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where title=%s and published_by=%s"
    cursor.execute(query, (title,publisher))
    results = cursor.fetchall()
    return results

# adds a publisher with the indicated
# attributes to the Publisher table
def addPublisher(name, phone, city):
    cursor = connection.cursor()
    query = "insert into bookmanager.Publisher values (%s, %s, %s)"
    cursor.execute(query, (name, phone, city))
    connection.commit()

# adds a book with the indicated attributes
# to the Book table
def addBook(ISBN, title, year, published_by, prev_edition, price):
    cursor = connection.cursor()

     # construct and execute query based on which 
     # foreign key attributes get null values
    if(published_by == 'null' and prev_edition == 'null'):
        query = "insert into bookmanager.Book values (%s, %s, %s, NULL, NULL, %s)"
        cursor.execute(query, (ISBN, title, year, price))
        connection.commit()
    elif(published_by == 'null'):
        query = "insert into bookmanager.Book values (%s, %s, %s, NULL, %s, %s)"
        cursor.execute(query, (ISBN, title, year, prev_edition, price))
        connection.commit()
    elif(prev_edition == 'null'):
        query = "insert into bookmanager.Book values (%s, %s, %s, %s, NULL, %s)"
        cursor.execute(query, (ISBN, title, year, published_by, price))
        connection.commit()
    else:
        query = "insert into bookmanager.Book values (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (ISBN, title, year, published_by, prev_edition, price))
        connection.commit()
    
# updates a book with the indicated ISBN with the 
# indicated new values
def editBook(ISBN, newISBN, newTitle, newYear, newPublished_by, newPrev_edition, newPrice):
    cursor = connection.cursor()

    # construct and execute query based on which 
    # foreign key attributes get null values
    if(newPublished_by == 'null' and newPrev_edition == 'null'):
        query = "update bookmanager.Book set isbn=%s, title=%s, year=%s, published_by=NULL, previous_edition=NULL, price=%s where ISBN=%s"
        cursor.execute(query, (newISBN, newTitle, newYear, newPrice, ISBN))
        connection.commit()
    elif(newPublished_by == 'null'):
        query = "update bookmanager.Book set isbn=%s, title=%s, year=%s, published_by=NULL, previous_edition=%s, price=%s where ISBN=%s"
        cursor.execute(query, (newISBN, newTitle, newYear, newPrev_edition, newPrice, ISBN))
        connection.commit()
    elif(newPrev_edition == 'null'):
        query = "update bookmanager.Book set isbn=%s, title=%s, year=%s, published_by=%s, previous_edition=NULL, price=%s where ISBN=%s"
        cursor.execute(query, (newISBN, newTitle, newYear, newPublished_by, newPrice, ISBN))
        connection.commit()
    else:
        query = "update bookmanager.Book set isbn=%s, title=%s, year=%s, published_by=%s, previous_edition=%s, price=%s where ISBN=%s"
        cursor.execute(query, (newISBN, newTitle, newYear, newPublished_by, newPrev_edition, newPrice, ISBN))
        connection.commit()

# deletes a book with the given ISBN from the Book table
def deleteBook(ISBN):
    cursor = connection.cursor()
    query = "delete from bookmanager.Book where isbn=%s"
    cursor.execute(query,(ISBN,))
    connection.commit()

# helper method that checks whether a book with the 
# indicated ISBN exists in the Book table
def checkISBN(ISBN):
    cursor = connection.cursor()
    query = "select * from bookmanager.Book where isbn=%s"
    cursor.execute(query,(ISBN,))
    results = cursor.fetchall()
    return results

# helper method that checks whether a publisher with 
# name publisher_name already exists in the 
# Publisher table
def checkPublisher(publisher_name):
    cursor = connection.cursor()
    query = "select * from bookmanager.publisher where name=%s"
    cursor.execute(query,(publisher_name,))
    results = cursor.fetchall()
    return results

# helper method to close the MySQL connection upon 
# program exit
def closeConnection():
    connection.close()