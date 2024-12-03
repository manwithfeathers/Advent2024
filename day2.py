with open("data.txt") as f:
    reports = f.read().split("\n")
    reports = [report.split() for report in reports]
    reports = [[int(s) for s in report] for report in reports]

def lst_diff(lst):
    """check diff between items in list is between 1 and 3"""
    for x in range(1, len(lst)):
        diff = abs(lst[x] - lst[x - 1])
        if diff < 1 or diff > 3:
            return False
    return True

def is_ascending_or_descending(lst):
    if sorted(lst) == lst and len(set(lst)) == len(lst):
        return True
    elif sorted(lst, reverse=True) == lst and len(set(lst)) == len(lst):
        return True
    else:
        return False

#part 1
safe_reports = [report for report in reports if lst_diff(report) and is_ascending_or_descending(report)]
print(len(safe_reports))

def damp_report(lst):
    """remove item from report and test again"""
    backup_lst = lst
    for x in range(len(lst)):
        lst = lst[:x] + lst[x + 1:]
        if is_ascending_or_descending(lst) and lst_diff(lst):
            return True
        else:
            lst = backup_lst
    return False

#part 2
safe_reports = [report for report in reports if damp_report(report)]
print(len(safe_reports))

