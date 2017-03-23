DB_NAME='Meter_Number'
TABLES={}
TABLES['Name']=(
    "CREATE TABLE 'name'("
    "'first_name' char(15) NOT NULL, "
    "'middle_name' char(15), "
    "'last_name' char(15) "
")ENGINE=INNODB")
TABLES['Address']=(
    "CREATE TABLE 'Address'("
    "'Address'VARCHAR(60) NOT NULL "
    ")ENGINE=INNODB")
TABLES['Billing_Cycle']=(
    "CREATE TABLE 'Billing_Cycle'("
    "'Month' char(20) NOT NULL "
")ENGINE=INNODB")
TABLES['Bill_Date']=(
    "CREATE TABLE 'Bill_Date'("
    "'Day' int(2) NOT NULL,"
    "print('\'),"
    "'Month'int (2) NOT NULL, "
    "print('\'),"
    "'Year' int(4) NOT NULL, "
")ENGINE=INNODB")
TABLES['Meter_No1']=(
    "CREATE TABLE 'Meter_no1'("
    "'Meter_no1' char(10) NOT NULL ,"
    "PRIMARY KEY('Meter_no1')"
")ENGINE=INNODB")
TABLES['Meter_Reading']=(
    "CREATE TABLE 'Meter_Reading'("
    "'Previous_Reading' varchar(20) NOT NULL, "
    "'Current_Reading' varchar(20) NOT NULL, "
")ENGINE=InnoDB")
TABLES['Total_Units']=(
    "CREATE TABLE 'Total_Units'("
    "'Total_Units'"
")ENGINE=INNODB")
TABLES['Rate_Per_Units']=(
    "CREATE TABLE 'Rate_per_Units'("
    "'Rate_per_Units' INT(15) ,"
    ")ENGINE=INNODB")
TABLES['Amount']=(
    "CREATE TABLE 'Amount'("
    "'Amount' INT(30),"
")ENGINE=INNODB")
TABLES['Fixed_Charges']=(
    "CREATE TABLE 'Fixed_Charges'("
    "'Load' int (15) NOT NULL, "
    "'Rate_Rs' int(15) NOT NULL, "
    " 'Amount_Rs' int(35) NOT NULL, "
")ENGINE=INNODB")
TABLES['Total_Money']=(
     "CREATE TABLE 'Total_Money'("
     "'Amount_Total' FLOAT(8),"
 ")ENGINE=INNODB")
TABLES['Remark']=(
    "CREATE TABLE 'Remark'("
    "'Remark' VARCHAR (200)"
")ENGINE=INNoDB")
TABLES['Maintance']=(
    "CREATE TABLE 'Maintance'("
    "'Maint_Amt' int (6)"
")ENGINE=INNoDB")
TABLES['Other']=(
    "CREATE TABLE 'Other'("
    "'Other_Amt' int (6)"
")ENGINE=INNoDB")
TABLES['Grand_Total_Rs']=(
    "CREATE TABLE 'Grand_Total_Rs'("
    "'Grand_Total_Rs' int (8)"
")ENGINE=INNoDB")
TABLES['Previous_Due']=(
    "CREATE TABLE 'Previous_Due'("
    "'Previous_Due' int (8)"
")ENGINE=INNoDB")
TABLES['Payment_Received']=(
    "CREATE TABLE 'Payment_Received'("
    "'Payment_Received' int (8)"
")ENGINE=INNoDB")
TABLES['Current_Charges']=(
    "CREATE TABLE 'Current_Charges'("
    "'Current_Charges' int (8)"
")ENGINE=INNoDB")
TABLES['Total_Amount_Due'] = (
    "CREATE TABLE 'Total_Amount_Due'("
    "'Total_Amount_Due' int (6)"
")ENGINE=INNoDB")
TABLES['Due_Date'] = (
    "CREATE TABLE 'Due_Date'("
    "'Due_Date' int (2)"
")ENGINE=INNoDB")
TABLES['Total_Amount_After'] = (
    "CREATE TABLE 'Total_Amount_After'("
    "'Total_Amount_After' int (8)"
")ENGINE=INNoDB")





