import csv 
from cs50 import SQL
open("concert.db", "w").close()
db= SQL("sqlite:///concert.db")
db.execute("CREATE TABLE Event (id INTEGER, event_name TEXT, event_date INTEGER, event_time INTEGER, event_venue TEXT, PRIMARY KEY(id))")
db.execute("CREATE TABLE Booking (book_id INTEGER, no_of_tickets INTEGER, book_date INTEGER, book_time INTEGER, venue TEXT, PRIMARY KEY(book_id))")
db.execute("CREATE TABLE Seller (seller_id INTEGER, seller_name TEXT, mobile INTEGER, rec_amount INTEGER, PRIMARY KEY(seller_id))")
db.execute("CREATE TABLE Buyer (buyer_id INTEGER, buyer_name TEXT, buyer_mobile INTEGER, buyer_email TEXT, PRIMARY KEY(buyer_id))")
db.execute("CREATE TABLE Payment (pay_id INTEGER, amount INTEGER, seller_id INTEGER, event_id INTEGER, ticket_id INTEGER, FOREIGN KEY(pay_id) REFERENCES Buyer(buyer_id), FOREIGN KEY(seller_id) REFERENCES Seller(seller_id), FOREIGN KEY(event_id) REFERENCES Event(id), FOREIGN KEY(ticket_id) REFERENCES Booking(book_id))")



with open("Booking Ticket.csv","r") as booking:
    reader=csv.DictReader(booking)

    for row in reader:
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


        db.execute("INSERT INTO Event(event_name,event_date,event_time,event_venue) VALUES(?,?,?,?);",plot, eveday,evetime,place)
        pols = db.execute("SELECT * FROM Event")
        for pol in pols:
            pm = pol["id"]
        book_id=db.execute("INSERT INTO Booking(no_of_tickets,book_date,book_time,venue) VALUES(?,?,?,(SELECT event_venue FROM Event WHERE id = ?));",ticket,date,time,pm)
        db.execute("INSERT INTO Seller(seller_name,mobile,rec_amount) VALUES(?,?,?);",cash,num,payed)
        db.execute("INSERT INTO Buyer(buyer_name,buyer_mobile,buyer_email) VALUES(?,?,?);",Name,contact,email)
        cols = db.execute("SELECT * FROM Seller")
        for col in cols:
           am = col["seller_id"]  

        db.execute("INSERT INTO Payment(pay_id,amount,seller_id,event_id,ticket_id) VALUES((SELECT buyer_id FROM Buyer WHERE buyer_name = ?),(SELECT rec_amount FROM Seller WHERE seller_id = ?),(SELECT seller_id FROM Seller WHERE seller_name = ?),(SELECT id FROM Event WHERE event_name = ?),(SELECT book_id FROM Booking WHERE book_id= ?));",Name,am,cash,plot,book_id)

      