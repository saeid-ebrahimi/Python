import database
#database.add_one("Laura","Smith","lura@smith.com")
#database.delete_one("6")
stuff = [
    ("Branda","Smitherton","branda@Smitherton"),
    ("Jashua","Raintree","Jashua@raintree"),
    ("Mike","Brand","mike@brand")
    ]
#database.add_many(stuff)
database.email_lookup("mike@brand")
database.show_all()

