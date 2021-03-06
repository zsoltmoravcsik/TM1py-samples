"""
Reschedule all chores by -1 Hour.
Chores get deactivated implicitly before update (and activate after transaction is done)

"""
from TM1py.Services import TM1Service


with TM1Service(address='localhost', port=12354, user='admin', password='apple', ssl=True) as tm1:
    # Get all chores. Loop through them and update them
    for chore in tm1.chores.get_all():
        chore.reschedule(hours=-1)
        tm1.chores.update(chore)





