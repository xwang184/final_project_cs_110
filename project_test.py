from jy import *

def main():
    
    test = key()
    test.key_got()
    assert(test.sum == 1)
    assert(test.finish() == False)
    test0 = laptop(test)
    test0.on()
    test0.answer()

main()
