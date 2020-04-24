import sqlite3


class Handler(object):
	def __init__(self, filename):
		self.__filename = filename

	def select_query(self, elements, table, conditions, order=None):
		query = '''
		SELECT
		'''

		for element in elements:
			query += element + ', '

		query = query[:-2]

		query += ' FROM ' + table

		if conditions is not None:
			query += ' WHERE '
			for condition in conditions:
				query += condition + ' AND '

			query = query[:-5]

		if order is not None:
			query += ' ORDER ' + order

		query += ';'

		connection, cursor = self.__get_conn_and_cur()

		cursor.execute(query)
		rows = cursor.fetchall()
		connection.commit()
		connection.close()
		return rows

	def delete_query(self, table, conditions):
		query = 'DELETE FROM ' + table + ' WHERE '

		for condition in conditions:
			query += condition + ' AND '

		query = query[:-5] + ';'

		connection, cursor = self.__get_conn_and_cur()

		cursor.execute(query)
		connection.commit()
		connection.close()

	def insert_query(self, table, values):
		query = 'INSERT INTO ' + table + ' VALUES('

		for value in values:
			query += value + ', '

		query = query[:-2] + ');'

		connection, cursor = self.__get_conn_and_cur()

		cursor.execute(query)
		connection.commit()
		connection.close()

	def __get_conn_and_cur(self):
		connection = sqlite3.Connection(self.__filename)
		cursor = connection.cursor()

		return connection, cursor
