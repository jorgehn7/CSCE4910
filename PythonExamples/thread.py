'''

This is a simple thread processor example
that is inteded to demostrate its syntax
use the time flag to analyze its performance

Usage:
time python thread.py
'''

import thread
import time

def dummy():
    time.sleep(1)
    
def main():

    #Creates 10 threads
    for i in range(10):
        tid = thread.start_new_thread(dummy, ())
        print 'created new thread %d' % tid

if __name__ == '__main__':
    main()
