"""
Program: Automatizing MySQL process
Author: Alef Matias
"""

import subprocess
import pymysql


# Execute a given terminal command
def terminalCommand(command):
    subprocess.Popen(command, shell=True).wait()


# Execute a MySQL command
def mySQLCommand(command):
    cursor.execute(command)
    conn.commit()


# Connecting to MySQL on localhost
conn = pymysql.connect(user='root', passwd='')
cursor = conn.cursor()

# Starting MySQL Server
terminalCommand('mysql.server start')

# MySQL command examples
mySQLCommand('CREATE DATABASE Test;')
mySQLCommand('USE Test;')
mySQLCommand('CREATE TABLE Testing (cod int(3), data char(10));')

# Stopping MySQL Server
terminalCommand('mysql.server stop')
