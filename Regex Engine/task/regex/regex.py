def single(reg, str):
    if reg == '':
        return True
    elif str == '':
        if reg in ['']:
            return True
        return False
    elif reg == '.' and str:
        return True
    else:
        if reg in str:
            return True
        return False


def equal(re, substr):
    if len(re) == 0:
        return True
    elif re and not substr:
        if re == '$':
            return True
        return False
    elif re[0] == '\\':
        if re[1] == '\\' and single('\\', substr[0]):
            return equal(re[2:], substr[1:])
        elif single(re[1], substr[0]):
            return equal(re[2:], substr[1:])
        else:
            pass
    elif len(re) >= 2 and re[1] == '?' and re[0] != '\\':
        if not single(re[0], substr[0]):
            return equal(re[2:], substr)
        else:
            return equal(re[2:], substr[1:])
    elif len(re) >= 2 and re[1] == '*' and re[0] != '\\':
        if not single(re[0], substr[0]):
            return equal(re[2:], substr)
        else:
            if len(substr) == 1:
                return True
            else:
                return equal(re, substr[1:])
    elif len(re) >= 2 and re[1] == '+' and re[0] != '\\':
        if single(re[0], substr[0]):
            if len(substr) == 1:
                return True
            elif substr[0] == substr[1]:
                return equal(re, substr[1:])
            else:
                return equal(re[2:], substr[1:])
    elif not single(re[0], substr[0]):
        return False
    else:
        return equal(re[1:], substr[1:])


def check(r,s):
    if len(r) == 0:
        return True
    if r.startswith('^'):
        if single(r[1], s[0]):
            return equal(r[1:], s)
    for i, v in enumerate(s):
        if equal(r,s[i:]):
            return True
    return False


def main():
    regex, input_string = input().split('|')
    print(check(regex, input_string))


if __name__ == '__main__':
    main()