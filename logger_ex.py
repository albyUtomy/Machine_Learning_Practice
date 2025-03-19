import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG, filemode='w', format='%(asctime)s - %(levelname)(s) -  %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.basicConfig(filename='example.log', level=logging.INFO)
# logging.basicConfig(filename='example.log', level=logging.WARNING)
# logging.basicConfig(filename='example.log', level=logging.ERROR)
# logging.basicConfig(filename='example.log', level=logging.CRITICAL)


logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

