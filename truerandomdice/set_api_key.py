import diceroller
from database import ApiKey
from ranclient import test_connection


def ask_api_key():
    # https://stackoverflow.com/questions/4960208/python-2-7-getting-user-input-and-manipulating-as-string-without-quotations
    api_key = str(raw_input('Enter valid api-key: '))
    final_key = ApiKey.save_key(api_key)
    return final_key

def verify_api_key():
    db_key = ApiKey.get_key()

    if db_key is None:
        db_key = ask_api_key()
    api_key = db_key.key
    verified = db_key.verified

    if verified != True:
        while test_connection(api_key) != True:
            api_key = ask_api_key()
        ApiKey.update_key_to_valid()

    print('api-key verification complete')
    return api_key


if __name__ == '__main__':
    verify_api_key()
    diceroller.simple_dice_app()
