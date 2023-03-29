def ask_number(question, low, high, multiplicity=1):
    """
    Просит ввести число из диапазона.
    :param question:
    :param low:
    :param high:
    :param multiplicity:
    :return:
    """
    response = None
    while response not in range(low, high, multiplicity):
        response = int(input(question))
    return response