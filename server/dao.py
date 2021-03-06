import mysql.connector
from mysql.connector import errorcode
# from __future__ import absolute_import, print_function

class Dao:

  def __init__(self, user, password, host, database):
    self.user = user
    self.password = password
    self.host = host
    self.database = database


  def connect(self):
    try:
      db = mysql.connector.connect(user='stproch', password='fuzzwuzhere',
                                  host='keckmysql-rds.lmucs.com',
                                  database='stproch')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)

    else:
      return db

  def place_per_block(self, result):
    table_list = []
    res_dict = {}
    # variables for ward F assignment
    first_year_off = 0
    second_year1_off = 0
    second_year2_off = 0
    second_year1_B_first = True
    second_year_off_same = False

    for r in result:
      if r[5] == 0:
        res_dict['id'] = r[0]
        res_dict['name'] = r[1] + ' ' + r[2]
        res_dict['first_name'] = r[1]
        res_dict['last_name'] = r[2]
        res_dict['year'] = r[3]
      if r[6] == "B" and r[3] == 1:
        first_year_off = r[4]
      if not (r[6] == "B" and r[3] == 2):
        res_dict['id'] = r[0]
        res_dict['name'] = r[1] + ' ' + r[2]
        res_dict['first_name'] = r[1]
        res_dict['last_name'] = r[2]
        res_dict['year'] = r[3]
        res_dict['off'] = r[4]
        res_dict['block'] = r[5]
        res_dict['ward'] = r[6]
        res_dict['shift'] = r[7]
        res_dict['shift1'] = r[6] + " / " + r[7][2:5]
        res_dict['shift2'] = r[6] + " / " + r[7][9:12]
        res_dict['shift3'] = r[6] + " / " + r[7][16:19]
        res_dict['shift4'] = r[6] + " / " + r[7][23:26]
        res_dict['shift5'] = r[6] + " / " + r[7][30:33]
        res_dict['shift6'] = r[6] + " / " + r[7][37:40]
        res_dict['shift7'] = r[6] + " / " + r[7][44:47]
        res_dict['shift8'] = r[6] + " / " + r[7][51:54]
        res_dict['off_bool'] = r[8]
        table_list.append(res_dict.copy())
      else:
        if second_year1_off == 0:
          second_year1_off = r[4]
        else:
          second_year2_off = r[4]

    # make checks to decide which second year is in B first
    if first_year_off != None:
      if first_year_off == second_year1_off:
        if first_year_off <= 4 and first_year_off > 0:
          second_year1_B_first = False
      elif first_year_off == second_year2_off:
        if first_year_off > 4:
          second_year1_B_first = False
      elif second_year1_off == second_year2_off:
        second_year_off_same = True
    
    # go through the results again in a loop
    for r in result:
      if r[6] == "B" and r[3] == 2:
        if ((r[4] == second_year1_off and second_year1_B_first == True) or (r[4] == second_year2_off and second_year1_B_first == False)) and (second_year_off_same == False):
          res_dict['id'] = r[0]
          res_dict['name'] = r[1] + ' ' + r[2]
          res_dict['first_name'] = r[1]
          res_dict['last_name'] = r[2]
          res_dict['year'] = r[3]
          res_dict['off'] = r[4]
          res_dict['block'] = r[5]
          res_dict['ward'] = r[6]
          res_dict['shift'] = r[7]
          res_dict['shift1'] = r[6] + " / " + r[7][2:5]
          res_dict['shift2'] = r[6] + " / " + r[7][9:12]
          res_dict['shift3'] = r[6] + " / " + r[7][16:19]
          res_dict['shift4'] = r[6] + " / " + r[7][23:26]
          res_dict['shift5'] = "F / " + r[7][30:33]
          res_dict['shift6'] = "F / " + r[7][37:40]
          res_dict['shift7'] = "F / " + r[7][44:47]
          res_dict['shift8'] = "F / " + r[7][51:54]
          res_dict['off_bool'] = r[8]
          table_list.append(res_dict.copy())
        else:
          res_dict['id'] = r[0]
          res_dict['name'] = r[1] + ' ' + r[2]
          res_dict['first_name'] = r[1]
          res_dict['last_name'] = r[2]
          res_dict['year'] = r[3]
          res_dict['off'] = r[4]
          res_dict['block'] = r[5]
          res_dict['ward'] = r[6]
          res_dict['shift'] = r[7]
          res_dict['shift1'] = "F / " + r[7][2:5]
          res_dict['shift2'] = "F / " + r[7][9:12]
          res_dict['shift3'] = "F / " + r[7][16:19]
          res_dict['shift4'] = "F / " + r[7][23:26]
          res_dict['shift5'] = r[6] + " / " + r[7][30:33]
          res_dict['shift6'] = r[6] + " / " + r[7][37:40]
          res_dict['shift7'] = r[6] + " / " + r[7][44:47]
          res_dict['shift8'] = r[6] + " / " + r[7][51:54]
          res_dict['off_bool'] = r[8]
          table_list.append(res_dict.copy())
          second_year_off_same = False
    return table_list

  def select_all(self, table):
    table_list = []
    # res_dict = {}
    result = self.select_one("*", table, 'block = 1')
    table_list = self.place_per_block(result)
    result = self.select_one("*", table, 'block = 2')
    block2_list = self.place_per_block(result)
    for r in block2_list:
      table_list.append(r)
    result = self.select_one("*", table, 'block = 3')
    block3_list = self.place_per_block(result)
    for r in block3_list:
      table_list.append(r)
    result = self.select_one("*", table, 'block = 0')
    newRes_list = self.place_per_block(result)
    for r in newRes_list:
      table_list.append(r)
    return table_list

  def getDate(self):
    date = self.select_one('date', 'date', 'date_id = 1')
    return date

  def select_one(self, item, table, conditions):
    db = self.connect()
    mycursor = db.cursor()
    query = ( "SELECT %s FROM %s WHERE %s" % (item, table, conditions) )
    mycursor.execute(query)
    result = mycursor.fetchall()
    return result

  def update(self, table, columns, conditions):
    db = self.connect()
    mycursor = db.cursor()
    query = ( "UPDATE %s SET %s WHERE %s " % (table, columns, conditions) )
    print('QUERY: ', query)
    mycursor.execute(query)
    db.commit()
    print(mycursor.rowcount, "record(s) affected")

  def updateDate(self, date):
    val = 'date = \'' + date + '\''
    self.update('date', val, 'date_id = 1')

  def updateOff(self, value, id):
    val = 'off = \'' + str(value) + '\''
    cond = 'employee_id = \'' + str(id) + '\''
    self.update('employees', val, cond)

  def updateYear(self, value, id):
    val = 'year = \'' + str(value) + '\''
    cond = 'employee_id = \'' + str(id) + '\''
    self.update('employees', val, cond)
  
  def updateFirstName(self, value, id):
    val = 'first_name = \'' + value + '\''
    cond = 'employee_id = \'' + str(id) + '\''
    self.update('employees', val, cond)
  
  def updateLastName(self, value, id):
    val = 'last_name = \'' + value + '\''
    cond = 'employee_id = \'' + str(id) + '\''
    self.update('employees', val, cond)
  
  def insertEmpl(self, first_name, last_name, year):
    values = '\'' + first_name + '\', \'' + last_name + '\', \'' + str(year) + '\', \'0\', \' \',  \' \', \'0\' '
    self.insert('employees', 'first_name, last_name, year, block, ward, shift, off_bool', values)

  def insert(self, table, columns, values):
    db = self.connect()
    mycursor = db.cursor()
    query = ( "INSERT INTO %s ( %s ) VALUES(%s) " % (table, columns, values) )
    print('QUERY: ', query)
    mycursor.execute(query)
    db.commit()
    print(mycursor.rowcount, "record(s) affected")

  def delete(self, table, condition):
    db = self.connect()
    mycursor = db.cursor()
    query = ( "DELETE FROM %s WHERE %s " % (table, condition) )
    print('QUERY: ', query)
    mycursor.execute(query)
    db.commit()
    print(mycursor.rowcount, "record(s) affected")
  
  def deleteEmpl(self, id):
    cond = 'employee_id = \'' + str(id) + '\''
    self.delete('employees', cond)

  def deleteAllAttrInt(self, table, column, replace):
    db = self.connect()
    mycursor = db.cursor()
    
    query = ( "UPDATE %s SET %s = %i" % (table, column, replace) )
    print ('QUERY: ', query)
    mycursor.execute(query)
    db.commit()
    print(mycursor.rowcount, "record(s) affected")

  def deleteAllAttrStr(self, table, column):
    db = self.connect()
    mycursor = db.cursor()
    
    query = ( "UPDATE %s SET %s = \' \' " % (table, column) )
    print ('QUERY: ', query)
    mycursor.execute(query)
    db.commit()
    print(mycursor.rowcount, "record(s) affected")


def main():
  dao = Dao('schedule','fuzzwuzhere', 'schedule.ctsb7iugp6xk.us-east-1.rds.amazonaws.com', 'schedule')
  output = dao.select_all('employees')
  print (output)





if __name__ == "__main__":
    main()
