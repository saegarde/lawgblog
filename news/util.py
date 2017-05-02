from unidecode import unidecode
import re


def slug_to_practice_area(slug):

    if slug == "trusts_and_estates":
        return "Trusts and Estates"
    elif slug == "criminal":
        return "Criminal Law"
    elif slug == "real_estate":
        return "Real Estate Law"
    elif slug == "tax":
        return "Tax Law"
    elif slug == "family_law":
        return "Family Law"
    elif slug == "personal_injury":
        return "Personal Injury Law"
    elif slug == "litigation":
        return "Litigation"
    else:
        return False


def slugify(s):
    for c in [' ', '-', '.', '/']:
        s = s.replace(c, '_')
    s = re.sub('\W', '', s)
    s = s.replace('_', ' ')
    s = re.sub('\s+', ' ', s)
    s = s.strip()
    s = s.replace(' ', '-')
    return s
