import psycopg2 as db
import configparser
import os
import sys

class Config:
	def __init__(self):
		path = os.path.dirname(os.path.realpath(sys.argv[0]))
		cfgfile = os.path.join(path, 'config.ini')

		if (os.path.isfile(cfgfile)):
			cfg = configparser.RawConfigParser()
			cfg.read(cfgfile)
		else:
			print("O arquivo de configuração config.ini não foi encontrado.")
			quit()

		self.config = {
			"postgres": {
				"user": cfg.get('database', 'user'),
				"password": cfg.get('database', 'password'),
				"host": cfg.get('database', 'host'),
				"port": cfg.getint('database', 'port'),
				"database": cfg.get('database', 'database'),
			}
		}

class Conexao(Config):
	def __init__(self):
		Config.__init__(self)		

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.commit()
		self.connection.close()

	@property
	def connection(self):
		return self.conn
	
	@property
	def cursor(self):
		return self.cur
	
	def commit(self):
		self.connection.commit()

	def fetchall(self):
		return self.cursor.fetchall()

	def execute(self, sql, params=None):
		try:
			self.conn = db.connect(**self.config["postgres"])
			self.cur = self.conn.cursor()
			self.cursor.execute(sql, params or ())
		except Exception as e:
			print("Erro na conexão com o banco de dados: ", e)
			exit(1)

	def query(self, sql, params=None):
		try:
			self.conn = db.connect(**self.config["postgres"])
			self.cur = self.conn.cursor()
			self.cursor.execute(sql, params or ())
			return self.fetchall()
		except Exception as e:
			print("Erro na conexão com o banco de dados: ", e)
			exit(1)