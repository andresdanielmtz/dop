class LibraryOOP:
    catalog = {}
    userManagement = {}

    # Common OOP, notice that everything is within the class
    def getBookLendings(self, userId, memberId):
        return self.catalog


# DOP Example


class UserManagement:
    @staticmethod
    def isLibrarian(userManagementData, userId):
        pass  # TODO: Implement
    # ?? Notice how it is simple to implement new ways of checking the user 
    @staticmethod
    def isSuperMember(userManagementData, userId):
        pass 


class Catalog:
    @staticmethod
    def getBookLendings(catalogData, memberId):
        pass  # TODO: Implement


class LibraryDOP:
    @staticmethod

    # ?? Look at this method
    def getBookLendings(libraryData, userId, memberId):
        if UserManagement.isLibrarian(
            libraryData.userManagement
        ) or UserManagement.isSuperMember(libraryData.userManagement):
            return Catalog.getBookLendings(libraryData.catalog, memberId)
        else:
            raise "Not allowed to get book lendings"
