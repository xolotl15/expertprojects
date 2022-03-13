def is_palindrome(string: str) -> bool:
    
    string = string.lower().replace(' ','')
    if string == string[::-1]:
        return True

    return False


def run():
    print( is_palindrome('hO la Aloh ') )


if __name__ == '__main__':
    run()