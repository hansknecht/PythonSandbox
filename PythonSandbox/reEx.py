#!/usr/bin/env python3
import re

def reExMatch(input_s, pattern_re):
    rePat = re.compile(pattern_re)
    return re.match(pattern_re, input_s)
