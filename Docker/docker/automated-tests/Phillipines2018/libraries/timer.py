import time
import logging

def measure_time(func):
    def inner(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.debug('Elapsed time is: ' + str(elapsed_time) + ' for function ' +
              func.__name__)
        return result
    return inner
