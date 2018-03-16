import pymysql

class DBConnect():
    """
    This class is used to connect to databases and run queries.
    """
    def __init__(self):
        pass

    def __connect(self, db):
        """
        This method stablishe's a connection with the passed in database and returns the connection.
        The host and user information are hardcoded here.
        :param db: the database name to connect to
        :return: the connection object
        """

        # connect to the db at the specified host
        host = '127.0.0.1'
        conn = pymysql.connect(host=host, port=3306, user='root', passwd='mysql', db=db)

        return conn

    def select(self, db, query):
        """
        This method is use to connect to a database and run a 'SELECT' statement.
        :param db: the database name to connect to
        :param query: the query to run
        :return: the result of the query (a list of lists)
        """

        # make the connection and execute the query
        conn = self.__connect(db)
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        # store the result in a list of lists. Each row is a list.
        all_rows = []
        for line in result:
            row = []
            for col in line:
                row.append(str(col)) # convert each value to string so no need to know what db will give us.

            all_rows.append(row)

        conn.close() #closing the db connection
        cur.close() #clearing the cursor

        # return all_rows


    def update(self, db, query):
        """
        This method is use to connect to a database and run a 'DELETE', 'UPDATE', 'INSERT' statements.
        :param db: the database name to connect to
        :param query: the query to run
        :return: result ( the number of rows affected)
        """

        # create connection
        conn = self.__connect(db)
        cur = conn.cursor()

        # execute the query
        result = cur.execute(query)
        conn.commit()

        conn.close()
        cur.close()

        return result





