errors=[]

def errors_add(msg):
    errors.append(msg)

def is_error():
    if errors==[]:
        return False
    else:
        return True