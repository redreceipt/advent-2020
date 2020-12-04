import re


def organize_passport_data(lines):
    return [{
        field.split(":")[0]: field.split(":")[1]
        for field in passport.strip().replace("\n", "").split(" ")
    } for passport in " ".join(lines).split("\n \n")]


def present(passports):
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    return [
        passport for passport in passports if required_fields -
        set(passport.keys()) in [set(), set(["cid"])]
    ]


def year_filter(value, start, end):
    return True if len(
        value) == 4 and int(value) >= start and int(value) <= end else False


def height_filter(value):
    if len(value.split("cm")) == 2 and int(
            value.split("cm")[0]) >= 150 and int(value.split("cm")[0]) <= 193:
        return True
    if len(value.split("in")) == 2 and int(value.split("in")[0]) >= 59 and int(
            value.split("in")[0]) <= 76:
        return True


def valid(passports):
    return [
        passport for passport in passports
        if year_filter(passport["byr"], 1920, 2002)
        and year_filter(passport["iyr"], 2010, 2020) and year_filter(
            passport["eyr"], 2020, 2030) and height_filter(passport["hgt"])
        and re.match("#[0-9a-f]{6}", passport["hcl"])
        and re.match("amb|blu|brn|gry|grn|hzl|oth", passport["ecl"])
        and re.match("[0-9]{9}$", passport["pid"])
    ]


f = open("input.txt")
passports = organize_passport_data(f.readlines())
print(len(present(passports)))
print(len(valid(present(passports))))
