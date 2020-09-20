



from custom_exceptions import UserNotFoundException

try:
    raise UserNotFoundException()
except UserNotFoundException as e:
    print(e)