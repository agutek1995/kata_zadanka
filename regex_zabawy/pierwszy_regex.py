# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"3 szt ([0-9]+,[0-9]+)"

test_str = ("Czego dusza zapragnie	3 szt 28,96	5 szt 33,96\n"
            "Benedyktyńskie 3 szt 26,46 5 szt 32,46\n"
            "Dominikańskie 3 szt 26,46 5 szt 32,46")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
