def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).
    
        >>> is_palindrome('tacocat')
        return True

        >>> is_palindrome('noon')
        True
    else
        >>> is_palindrome('robert')
        return False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]