# Executing mod_a.py, it outputs 1000, which is present in mod_b.py
# Eventhough in mod_a.py, import of mod_c.py occurs after import of mod_b.py,
# The value of x is set by mod_b.py.
# It is so, because mod_b.py itself imports mod_c.py and then modifies x
# Thus, in mod_a.py import mod_c.py doesnt do much, because it was already imported by mod_b.py
# The first import mod_c in mod_b.py file, just loads the module
# Whereas from mod_c import * just changes base of the names of attributes of mod_c