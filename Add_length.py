def add_length(str_):
    return list(map(lambda x: " ".join([x, str(len(x))]), str_.split(" ") ))
