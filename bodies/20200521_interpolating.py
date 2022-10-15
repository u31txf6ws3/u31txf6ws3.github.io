# {
#     "TITLE": "String Interpolation Interpolation",
#     "DATE": "2020-05-21",
#     "BODYPATH": "bodies/20200521_interpolating.py",
#     "REDDIT_COMMENTS": "https://old.reddit.com/user/u31txf6ws3/comments/go0ni8/string_interpolation_interpolation/",
#     "OUTPUT": "posts/20200521_interpolating.html"
# }

# This is a quick one, but while converting my <a
# href="./20150904_automata">old cellular automata posts</a> from Jupyter
# Notebooks to HTML I came across this function I wrote five years
# ago.

def make_rule(rule_name, k):
    rule_name = int(rule_name)
    rule_len = 2 ** k
    rule = [*map(int, bin(rule_name)[2:])]
    rule = [0] * (rule_len - len(rule)) + rule
    rule = rule[::-1]
    return rule

# This is just meant to return a list with the \(2^k\) binary digits of the
# integer <code>rule_name</code>, reversed. So we get something like

print(make_rule(123, 3))

# I purposefully did not use bit-shifting operations, yet still I don't like
# this code a lot. It has wonky things like

# <pre>bin(rule_name)[2:]</pre>

# Which is there to remove the <code>'0b'</code> that the function
# <code>bin</code> prefixes to its output. If I were writing that today I'd
# make use of the string format parameter <code>b</code>

x = 123
print(f"{x:b}")

# It's cleaner in my opinion, though admittedly a bit more cryptic if you're
# not used to string formating.

# Then there's this line, which is meant to left pad the resulting string with
# zeros

# <pre>[0] * (rule_len - len(rule)) + rule</pre>

# I knew you could set the minimum number of digits <code>n</code> of a number
# using the formating parameter <code>0n</code>

x = 123
print(f"{x:08}")

# but I didn't know if you could use both parameters in conjunction before
# writing this post. Turns out you can.

x = 123
print(f"{x:08b}")

# However in my case the number of digits is variable. I wonder if I'm allowed
# to...

k = 3
x = 123
print(f"{x:0{2 ** k}b}")

# Oh. So I could have written the function more succinctly.

def make_rule(rule_name, k):
    n_digits = 2 ** k
    as_binary = f"{rule_name:0{n_digits}b}"
    return [int(i) for i in reversed(as_binary)]

print(make_rule(123, 3))

# Which I think is a bit nicer.
