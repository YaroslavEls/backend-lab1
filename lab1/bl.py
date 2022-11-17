def check(id, arr):
    for elem in arr:
        if elem['id'] == id:
            return True
    return False