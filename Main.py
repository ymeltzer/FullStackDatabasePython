import sqlparse
from Table import Table
from Selector import Selector


class Main:
    tables = None

    def __init__(self):
        # holds all our Tables
        self.database = []

    # takes string query returnquit
    def execute(self, query):
        pass

    def print_database(self):
        for table in self.database:
            print(table)


# for now we will work with one sql statement at a time
if __name__ == '__main__':

    database = Main()
    sql = 'CREATE TABLE YCStudent; select * from bar;'

    parsed = sqlparse.parse(sql)

    temp = parsed[0].get_real_name()
    if parsed[0].get_type() == 'CREATE':
        table = Table(parsed[0].get_name())
        database.tables.append(table)

    elif parsed[0].get_type() == 'INSERT':
        pass

    elif parsed[0].get_type() == 'SELECT':
        pass
    print()


