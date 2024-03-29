# {
#     "TITLE": "Better at pandas",
#     "DATE": "2020-01-01",
#     "BODYPATH": "bodies/20200529_better_at_pandas.py",
#     "OUTPUT": "posts/20200529_better_at_pandas.html",
#     "HIDDEN": true
# }

# Chances are that if you do data analysis in python you use <a>pandas</a>.
# I'll spare you an introduction paragraph about the library, if you're here
# you probably know what pandas is and is curious to know what my advice is. So
# let me go straight to the point.

# <blockquote>
#     To get better at pandas take it as a chalenge to do your whole data cleaning/transformation using one
#     (possibly quite long) sequence of (mostly builtin) method chains.
# </blockquote>

# I find this advice easier to follow when doing exploratory data analysis and
# cleaning on a jupyter notebook. So get ready, because you'll be writing
# <code>.pipe(lambda df:</code> a lot.

# If you're not familiar with the term, method chaining is the

# i like it because it turns into a puzzle that's quite satisfying to solve

# after a while you'll develop a sixth sense about what should and shouldn't be
# possible to do only builting functino

# Pandas dataframes contain a staggering ammount of functionality, but it's
# very easy to get stuck in a state where you know only the basic
# functionallity that's enough to perform most data transformation and
# analysis. The problem with that is that you end up with messy, fragile and
# hard to debug code.

# <pre>df[df.apply(lambda row: row.A in valid)]
# df[df['A'].isin(valid)]
# df.query('A in @valid')
# df.pipe(lambda df: df[df.A.isin(valid)])</pre>

# * .pipe
# * never reference the original dataframe
# * Use the `query` dataframe method
# * Plotting
# * Use a `jump` function
# * pipe(jump, display) is your print function

# <h3>Will it make data analysis easier?</h3>
# Definitelly on notebooks

# <h3>Will it make my analysis run faster?</h3>
# Most of the time won't make a difference, other times it will make it slower.

# <h3>Will it make code more readable?</h3>
# Depends, too many lambdas

# <h3>Will it be easier to debug?</h3>
# Well, kinda.
