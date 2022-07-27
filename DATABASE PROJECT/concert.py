import csv #Import CSV libray for opeing and reading from a csv file
from cs50 import SQL #we are going to use this to excecute SQL Queries
open("concert.db", "w").close() #we are opening the database to write into it and close so that it doesnt interfere with what we are writing
db= SQL("sqlite:///concert.db") #we are creating our database in sqlite
#creating tables for our database
db.execute("CREATE TABLE Event (id INTEGER, event_name TEXT, event_date INTEGER, event_time INTEGER, event_venue TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE Booking (book_id INTEGER, no_of_tickets INTEGER, book_date INTEGER, book_time INTEGER, venue TEXT, PRIMARY KEY(book_id))")
db.execute("CREATE TABLE Seller (seller_id INTEGER, seller_name TEXT, seller_mobile INTEGER, rec_amount INTEGER, PRIMARY KEY(seller_id))")
db.execute("CREATE TABLE Buyer (buyer_id INTEGER, buyer_name TEXT, buyer_mobile INTEGER, buyer_email TEXT, PRIMARY KEY(buyer_id))")
db.execute("CREATE TABLE Payment (P_Id INTEGER,pay_id INTEGER, amount INTEGER, seller_id INTEGER, event_id INTEGER, ticket_id INTEGER, PRIMARY KEY(P_Id) FOREIGN KEY(pay_id) REFERENCES Buyer(buyer_id), FOREIGN KEY(seller_id) REFERENCES Seller(seller_id), FOREIGN KEY(event_id) REFERENCES Event(id), FOREIGN KEY(ticket_id) REFERENCES Booking(book_id))")



with open("Booking Ticket.csv","r") as booking:# opening our csv file to read whats there 
    reader=csv.DictReader(booking)#enables us to read what is in our csv file

    for row in reader: #creating a loop through our csv file
        #creating variables
        Name = row["Name"]
        contact = row["contact"]
        email = row["email"]
        ticket = row["tickets"]
        date = row["boodate"]
        time = row["booktime"]
        cash = row["cashier"]
        num = row["number"]
        payed = row["amountpayed"]
        eveday = row["eventday"]
        evetime = row["eventtime"]
        place = row["eventvenue"]
        plot = row["funky"]

#we are inserting data in our created tables
        db.execute("INSERT INTO Event(event_name,event_date,event_time,event_venue) VALUES(?,?,?,?);",plot, eveday,evetime,place)
        pols = db.execute("SELECT * FROM Event")#creating a variable
        for pol in pols:# looping through the selected column
            pm = pol["id"]
        book_id=db.execute("INSERT INTO Booking(no_of_tickets,book_date,book_time,venue) VALUES(?,?,?,(SELECT event_venue FROM Event WHERE id = ?));",ticket,date,time,pm)
        db.execute("INSERT INTO Seller(seller_name,seller_mobile,rec_amount) VALUES(?,?,?);",cash,num,payed)
        db.execute("INSERT INTO Buyer(buyer_name,buyer_mobile,buyer_email) VALUES(?,?,?);",Name,contact,email)
        cols = db.execute("SELECT * FROM Seller")
        for col in cols:#looping through the selected column
           am = col["seller_id"]  

        db.execute("INSERT INTO Payment(pay_id,amount,seller_id,event_id,ticket_id) VALUES((SELECT buyer_id FROM Buyer WHERE buyer_name = ?),(SELECT rec_amount FROM Seller WHERE seller_id = ?),(SELECT seller_id FROM Seller WHERE seller_id = ?),(SELECT id FROM Event WHERE id = ?),(SELECT book_id FROM Booking WHERE book_id= ?));",Name,am,am,pm,book_id)

      