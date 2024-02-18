#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    final_char = ""
    for i in range(1, len(what)):
        final_char = what[len(what) - i]
        if final_char != " ":
            break
    if final_char == "?" and not what.isupper():
        return "Sure."
    elif what.isupper():
        return "Whoa, chill out!"
    elif what.split() == []:
        return "Fine. Be that way!"
    else:
        return "Whatever."