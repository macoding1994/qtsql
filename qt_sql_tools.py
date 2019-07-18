from PyQt5 import QtSql

class QtSqlTools(object):


    def __init__(self,drivers,db=None,host=None,user_name=None,psw=None):
        self.db = QtSql.QSqlDatabase.addDatabase(drivers)
        self.db.setDatabaseName(db)
        self.db.setHostName(host)
        self.db.setUserName(user_name)
        self.db.setPassword(psw)
        self.db.open()
        self.sql = QtSql.QSqlQuery(self.db)

    def save(self,sql):
        if self.db.isOpen():
            self.sql.exec_(sql)
        else:
            print('DB ERROR -- <数据库未打开>')


    def savemore(self,sql,data_l):


        if self.db.isOpen():
            try:
                self.sql.prepare(sql)
                for var in data_l:
                    self.sql.addBindValue(var)
                else:
                    self.sql.exec_()
            except Exception:
                print('SQL ERROR -- <查询语句有误>')
        else:
            print('DB ERROR -- <数据库未打开>')


    def fetchone(self,sql):
        if self.db.isOpen():
            self.sql.exec_(sql)
        else:
            print('DB ERROR -- <数据库未打开>')


    def fetchall(self,sql,field,*args):
        '''"SELECT * FROM zmister where ID > 2000"'''
        if self.db.isOpen():
            try:
                query = QtSql.QSqlQuery(sql)
                fieldNo = query.record().indexOf(field)
                while query.next():
                    country = query.value(fieldNo)
                    print(country)

            except Exception:
                print('SQL ERROR -- <查询语句有误>')
        else:
            print('DB ERROR -- <数据库未打开>')

if __name__ == '__main__':
    D = QtSqlTools('QSQLITE','a.sqlite')
    '''--------------------------------------------'''
    # sql = "SELECT * FROM zmister where ID > 2000"
    # D.fetchall(sql,'site_url')
    '''--------------------------------------------'''
    # sql = "insert into zmister values(8888, '州的先生', 'http://zmister.com')"
    # D.save(sql)
    '''--------------------------------------------'''
    sql = "insert into zmister values(?, ?, ?)"
    D.savemore(sql,[8888,'州的先生','http://zmister.com'])
    '''--------------------------------------------'''


