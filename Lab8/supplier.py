class Supplier():
    def __init__(self, SupplierID, Name, ContactEmail):
        self.SupplierID = SupplierID
        self.Name = Name
        self.ContactEmail = ContactEmail


    def display_info(self):
        return(f"Supplier ID:{self.SupplierID} | Name:{self.Name} | Contact Email:{self.ContactEmail}")

    def to_dictionary(self):
            return {
                "ID": self.SupplierID,
                "Name": self.Name,
                "Contact Email": self.ContactEmail
            }


