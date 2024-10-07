def minLength(s: str) -> int:
    """
    Returns the minimum length of the given string after all occurrences of 'AB' and 'CD' have been removed.
    """
    if not s:
        return 0

    while 'AB' in s or 'CD' in s:
        s = s.replace('AB', '').replace('CD', '')

    return len(s)
minLength('ABFCACDB')