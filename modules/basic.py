__author__ = 'B.Ranjbarsahraei'

def pretty_print(d, indent=0):
    """
prints a pretty tree from a stored in a mixed dictionary and list
"""
    if indent < 100:
        if isinstance(d, dict):
            for key, value in d.iteritems():
                print '\t' * indent + str(key)
                if isinstance(value, dict) or isinstance(value, list):
                    pretty_print(value, indent+1)
                else:
                    print '\t' * (indent+1) + str(value)

        if d and isinstance(d, list):
            for key, item in enumerate(d):
                print '\t' * indent + str(key)
                if isinstance(item, dict) or isinstance(item, list):
                    pretty_print(item, indent+1)
                else:
                    print '\t' * (indent+1) + str(item)


def print_matrix_print(M, indent=1):
    """
    prints a pretty tree from a stored in a mixed dictionary and list
    """
    for row in M:
        print '|', '\t' * indent,
        for item in row:
            print item, '\t' * indent,
        print "|\n",

