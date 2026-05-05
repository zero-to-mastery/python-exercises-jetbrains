# This condition does not handle 0 correctly. How can you fix it?

def do_stuff(num=0):
    try:
        if num or num == 0:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
