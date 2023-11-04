def compact(lst):
    """Return a copy of lst with non-true elements removed.
    return copy(lst, True)
        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [val for val in lst if val]