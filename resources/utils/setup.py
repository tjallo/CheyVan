import os
def startRoutine():
    if not os.path.exists('messages'):
        os.makedirs('messages')


    print('Startroutine completed')