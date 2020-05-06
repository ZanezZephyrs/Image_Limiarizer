import re


def validate_output_name(name):
    aux = (name.strip()).split()
    if (len(aux) != 1):
        return False

    result = re.match(r'\S+\.(png|jpeg|jpg)', name)
    print(name, result)
    return not result == None  # se resultado n é nulo, o output é valido


#print(validate_output_name("nome.jpg"))