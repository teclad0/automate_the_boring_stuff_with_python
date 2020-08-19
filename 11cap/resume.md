# Cap 11 - Debugging 

## Raising Exceptions
Raising an exception is a way of saying, "Stop running the code in this function and move the program execution to the except statement"
'''python
raise Exception('This is the error message.')

try:
	yeld
except Exception as err:
	print('An exception happened:' + str(err))
'''

## Getting the traceback as a string
Yu can obtain the traceback by calling traceback.format_exc()

## Assertions
Is a sanity check to make sure your code isn't doing somethin obviously wrong. 'I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.'

'''python
assert 'red' in stoplight.values(), 'Neither light is red!' + str(stoplight)
'''

## Logging 
Better choice than print() statements
'''python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)
s -  %(message)s')

logging.debug('Start of factorial(%s%%)'  % (n))

logging.disable(logging.CRITICAL) # to disable all logs

DEBUG
logging.debug()
The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.

INFO
logging.info()
Used to record information on general events in your program or confirm that things are working at their point in the program.

WARNING
logging.warning()
Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.

ERROR
logging.error()
Used to record an error that caused the program to fail to do something.

CRITICAL
logging.critical()
The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

'''

## Logging to a file
'''python
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')
'''
