from email_validator import validate_email, EmailNotValidError
from crayons import red, green
def is_exist(email, debug=False):
    try:
        v = validate_email(email) # validate and get info
        _email = v["email"] # replace with normalized form
        if debug:
            print(green(f"{_email} is valid", bold=True))
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        if debug:
            print(red(str(e), bold=True))
        return False

def get_combinations(first, last, domain, middle=None):
    combination_list = ["{fn}", "{ln}", "{fn}{ln}","{fn}.{ln}", "{fi}{ln}", "{fi}.{ln}", 
    "{fn}{li}", "{fn}.{li}", "{fi}{li}", "{fi}.{li}",
    "{ln}{fn}","{ln}.{fn}", "{ln}{fi}", "{ln}.{fi}","{li}{fn}",
    "{li}.{fn}","{li}{fi}","{li}.{fi}","{fn}-{ln}","{fi}-{ln}",
    "{fn}-{li}","{fi}-{li}","{ln}-{fn}","{ln}-{fi}","{li}-{fn}","{li}-{fi}",
    "{fn}_{ln}","{fi}_{ln}", "{fn}_{li}","{fi}_{li}","{ln}_{fn}","{ln}_{fi}","{li}_{fn}","{li}_{fi}"]
    
    combo_with_middle = [
        "{fi}{mi}{ln}", "{fi}{mi}.{ln}","{fn}{mi}{ln}",
        "{fn}.{mi}.{ln}", "{fn}{mn}{ln}","{fn}.{mn}.{ln}",
        "{fi}{mi}-{ln}","{fn}-{mi}-{ln}", "{fn}-{mn}-{ln}",
        "{fi}_{mi}_{ln}","{fn}_{mi}_{ln}","{fn}_{mn}_{ln}",
        "{fi}{mi}{li}.{fn}.{ln}"
    ]

    name_list = []
    fn = first
    fi = first[0]
    ln = last
    li = last[0]

    for combo in combination_list:
        cc = combo.format(fn=fn, fi=fi, ln=ln, li=li)
        name_list.append(cc)

    if middle is not None:
        mn = middle
        mi = middle[0]
        for combo in combo_with_middle:
            # Run through combinations
            cc = combo.format(mn=mn, mi=mi, fn=fn, fi=fi, ln=ln, li=li)
            name_list.append(cc)

    final_list = []
    for name in name_list:
        cc = f"{name}@{domain}"
        final_list.append(cc)
    
    return final_list

def get_valid_emails(first, last, domain, middle=None, debug=False):
    verified = []
    email_combinations = get_combinations(first, last, domain, middle=middle)
    for email in email_combinations:
        exist = is_exist(email, debug=debug)
        verified.append(email)
    return verified


if __name__ == "__main__":
    combo_list = get_valid_emails("kevin", "hill", "gmail", middle="andrew")
    print(combo_list)