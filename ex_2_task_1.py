# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum())
# B must have between 2 and 8 alpha numeric chars (test: isalnum())
# C must be one of these:  com edu org gov
#
# Here are some tests and the expected results:
#
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes
# just something similar to that effect. You could even be more helpful e.g.
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail you at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt


def is_valid_email_address(s):

    # your code here
    error_dict = {
        'Pass': 'Seems legit',
        '1': 'Must have exactly one @',
        '2': 'pre @ part must contain 3 - 16 alfanum chars',
        '3': 'pre @ part must contain only alfanum chars',
        '4': 'post @ part must have exactly one dot!',
        '5': 'part after @ and before . must contain 2-8 alfanum chars',
        '6': 'part after @ and before . must only contain alfanum chars',
        '7': 'past-dot part invalid, must be from : com edu, org, gov'
    }

    error_list = []

    # Error status 1
    # find number of '@' signs contained in input
    chars_1 = [char for char in list(s) if char == '@']
    if len(chars_1) != 1:
        error_list.append('1')

    # Error status 2
    # ensure length is between 3 and 16 characters
    if len(s) <= 3 or len(s) >= 16:
        error_list.append('2')  # append errors to list

    # Error status 3
    # string before @ must be alphanum
    if s.split('@')[0].isalnum() == False:
        error_list.append('3')

    # Error status 4
    # find number of periods in string
    chars_4 = [char for char in list(s) if char == '.']
    if len(chars_4) != 1:
        error_list.append('4')

    # Error status 5 and 6
    try:
        chars_5 = s.split('@')[1].split('.')[0]
        if len(chars_5) <= 2 or len(chars_5) >= 8:
            error_list.append('5')

        if chars_5.isalnum() == False:
            error_list.append('6')

    except IndexError:
        # if string does not contain '@' or '.' ignore this test
        # relevant errors will be error code 1 and 4
        pass

    try:
        ext = s.split('.')[-1]
        if ext not in ['com', 'edu', 'org', 'gov']:
            error_list.append('7')

    except IndexError:
        # if string does not contain '.' ignore the test
        pass

    # after tests, if error_list is 0 return valid
    if len(error_list) == 0:
        return ('Pass', error_dict['Pass'])
    else:
        return [(err_code, error_dict[err_code]) for err_code in error_list]


# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu",
                  "chris.edu",
                  "chris@edu",
                  "@bla.edu",
                  "throatwobblermangrove@mpfc.org",
                  "chris@X.com",
                  "chris.harding@iastate.edu",
                  "chris@pymart.biz",
                  "chris@letsgo!.org",
                  "chris@megasavings.org",
                  "tc@tank.com",
                  ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e)
        if r == None:
            print(e, s)  # OK
        else:
            print(f"{e} - error: {s}, error code: {r}")  # Error
