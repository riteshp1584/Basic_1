# To learn Pandas specifically for ML Projects

import re

txt1 = "Hello Planet"

txt2 = "Earth is so beautiful"

x = re.findall("^Hello", txt1)

if x:
    print("Yes, the string starts with Hello")

else:
    print("No")
