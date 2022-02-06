import re
def is_canonical(version):
    return re.match(r'^([1-9][0-9]*!)?(0|[1-9][0-9]*)(\.(0|[1-9][0-9]*))*((a|b|rc)(0|[1-9][0-9]*))?(\.post(0|[1-9][0-9]*))?(\.dev(0|[1-9][0-9]*))?$', version) is not None


# SomeProject
# SomeProject == 1.3
# SomeProject >=1.2,<2.0
# SomeProject[foo, bar]
# SomeProject~=1.4.2




tests = [
    # "4.1.0",
    # "4.2.1b2",
    # "1.1.dev1"
    # "1.1a1"
    "1.0b2.post345.dev456"
    ]


for test in tests:
   print(is_canonical(test))
   