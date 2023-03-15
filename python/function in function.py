def fun():
    def do_local():
        test=1
    def do_non_local():
        nonlocal test
        test=2
    def do_global():
        global test
        test=3
    test=0
    do_local()
    print(" test value after do_local : ",test)
    do_non_local()
    print(" test value after do_non_local : ",test)
    do_global()
    print(" test value after do_globel : ",test)
fun()
#print(" test value after do_globel : ",test)