#! /usr/bin/env python3

import datetime

taareek = datetime.date(2018, 11, 23)                                             # Using datetime library.

print(f"{taareek} was a {taareek:%A}, and it was then I started with Python.")      # Getting the day with %A.
