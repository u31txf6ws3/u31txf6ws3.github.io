# {
#     "TITLE": "1D Cellular Automata in Python",
#     "DATE": "2015-09-04",
#     "BODYPATH": "bodies/20150904_automata.py",
#     "REDDIT_COMMENTS": "https://old.reddit.com/user/u31txf6ws3/comments/go0lwo/1d_cellular_automata_in_python/",
#     "OUTPUT": "posts/20150904_automata.html"
# }

# A common exercise in programming is making an instance of <a
# href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's game of
# life</a>. It's a great example of a simple set of rules that generate
# incredibly complex behavior. And if you're like me, you're sick of it. I
# mean, it's such an overused example and it got really old by now, which is a
# shame because the subject of cellular automata (of which the game of life is
# but a single example) is very fascinating. This inspired me to make a series
# of posts exploring the subject and it's applications. And I decided to do it
# in python, because python is so hot right now, you guys.

# Simply put, a (1D) cellular automata is composed of an array of cells distributed in a circular
# pattern, where they can be found in one of two states: 0 or 1. In the
# beginning of each time step, every cell looks at its own state and the state of
# its nearest neighbors, and according to a deterministic rule decide whether to
# change its state or keep the current one.

# Simple right? Taking by the name "cellular automata" the uninitiated reader
# might be mislead to think that the cells are the interesting part of this
# whole thing. Wrong! The rules that the cells use to update their state is
# where the money is at. Here is what a rule looks like

# <img style="width:95%; height: auto;"
#  src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAywAAABPCAYAAAAJBkH0AAAABmJLR0QA/wD/AP+gvaeTAAAegElE
# QVR4nO3deVAUZ/oH8O9wKCo4ICCnQUaQBBXB2+xGZjHrgReCqwGN4hVvtDwqVhmp7M9dEo2YqLgY
# MWJw1RVRZxVrECNKUisiQXTWEBV1JIoKXiAglzC/P6jpBbmGyNvT0/N8qqxqprvf53nfbtp+6en3
# lWg0Gg0IISgpKcHDhw/Rq1cvWFpa6jsdUbp//z5evXoFLy8vfaciShqNBjdu3IBUKoWzs7O+0xGl
# ly9foqCgAK6urrCystJ3OqJUUFCAly9f4r333tN3KqJ148YNWFpawtXVVd+piFJpaSkePHgAFxcX
# dO/eXd/piIHKRN8ZECIUSUlJ8Pb2Rnp6ur5TEa1FixZh4MCB+k5DtKqqquDt7Y21a9fqOxXROnXq
# FLy9vZGamqrvVEQrIiIC3t7eoL+nsvPee+9hxYoV+k5DtM6ePQtvb2+cPHlS36mIBnVYCCGEEEII
# IYJFHRZCCCGEEEKIYFGHhRBCCCGEECJY1GEhhBBCCCGECBZ1WAghhBBCCCGCxUuH5cKFC5BIJJBI
# JPjss8/4CEkIIYQQQggRATN9JyBmu3fvxpIlSwAAarUavXv3ZhJn69atePToEZOytWbPng2pVIqY
# mBimQ0127doVmzZtwpEjR3D58mVmcQDgT3/6EyZOnNjmdvn5+di5cyfTenfp0gV/+9vfkJiYiMzM
# TGZxAEAulyMwMBAbNmxgGgcAVq9ejZ49e7a5HR/19vf3x4QJE3ir9927d3H06FGmcWQyGZYtW9bm
# dnV1dfj0009RV1fHLBeJRIJ169ZBrVZDoVAwiwMAbm5uWLJkCXbu3ImCggKmsaZNm4YhQ4a0uV1m
# ZiZOnDjBNJd33nkHS5cuxfbt2/Hbb78xjRUaGgonJyd8/fXXTK99ZmZm2Lx5s07bxsTE4MGDB8xy
# AYCQkBC4uLhg27ZtTOttamqKLVu2QKFQ4NKlS8ziAMDw4cMxderUNrd7+PAhduzYwTQXiUSCL774
# gtd6r1+/HjU1NcziSCQSrFq1Sqc5bf79738jIyODWS4AMGzYMAQHB2PDhg2ora1lGmv58uUoLCxk
# /n+dlZWVPXVYRGDHjh2wtLSEubk5k/KLioowZMgQuLq6IiEhAU5OTkziAEBeXh42bdqExMREXLly
# hdmES8+fP0dFRYVOHZb79+/zUm9thyU7O5tpvV+9eoWxY8fiH//4B7Zs2cIkDlDfkf7444916rAk
# JSXh8uXLkEqlTHJ58eIFysvLMW7cON7qnZ2djUOHDulU/9+jsrISnTt31qnDUltbi507dzKdsPPB
# gwcIDw/HlStXcO3aNUyZMoVJnMePHyMhIQFLlizBvn37MG3aNNja2jKJlZSUhL59++rUYbly5Qqu
# Xr2KoKAgJrkUFhYiISEBS5cuxa5du2BqaopOnToxiVVUVARvb29IJBLs378fLi4uTOIA9RMY6tph
# iY+Px9SpU2FnZ8ckl2PHjsHDwwOmpqa81HvLli1ISUnB69evdTrHfo/s7GykpKTo1GF5/PgxFAoF
# Vq1axSQXoP6POV988QXOnDmDmpoapvVWKpWYOnUqvvnmG6bXvoKCAsyYMUOnDsuZM2dQVVWFoUOH
# MsnlypUrUCqVCA4Oxvbt27F161YmcYD6e8/g4GDk5uYiKysLf/nLX5jEef78OQ4ePGhHHRaR6NWr
# Fzp37syk7Orqam65e/fucHNzYxIHAG7fvs0t29vbw9HRkUkcE5P2fRtSjPW2sLDA4sWLmcQBgAMH
# DrRr+549e4qu3jY2NszOm9LSUjx79kzn7c3NzZmew8XFxdyyn58fszb+9ddfcebMGe7nsLAwuLu7
# M4l169atdm3Pst43btyAUqnkfnZxcUHXrl2ZxGr412grKyum501eXl67tg8NDUWfPn2Y5NLwOsxn
# vT/88EN89NFHTOIcOXIEaWlpOm/v7OzM9Pq4fv16bnn06NEIDQ1lEicxMRE//PADgPqnWSyPZWlp
# abu2Hz16NMLCwpjkcvToUW5SWzMzM6bH8vjx49zygAEDmMXKz8/HwYMH6aV7QgghhBBCiHAJosOy
# detW7qX8p0+fora2FrGxsRgxYgSsra3RrVs3+Pr64ssvv0RlZaXO5ZSXlyMqKgq+vr7o3r07pFIp
# 3n//fezZs6fV73KHh4dDIpG0+XhPoVBw8X7++Wfuc+0gA9r3VwDA3d2d21b7j/X3vAkhhBBCCDF0
# gvtKWFlZGaZNm4b09PRGn1+7dg3Xrl3DqVOncPbs2TYfhT9+/BgzZsxAbm5uo88zMjKQkZGBI0eO
# 4NSpU8weqRNCCCGEEELeniCesDQ0f/58/Pjjj5g+fToOHz6Mc+fO4bvvvoO3tzcA4OLFi/j73//e
# Zjnh4eHIzc3FnDlzcPbsWVy9ehVHjhzB8OHDAQBpaWmYM2cOkzrI5XJoNBrExsZyn6nVamg0mkb/
# WL2c+aYPPvgAS5YsQXR0NJKSknDy5Elm3xsVaywh5cJnrF9++QXBwcGws7NDly5d4OPjg507dzId
# baolYqy3sZ7DAL/nlpDOYz5yEev1SFdia2PA+M5hPmMZ6znMZ5yOiCW4JyxpaWn45z//iZkzZzb6
# fNq0afD19YVarca3336Lv/71rzAzazn97OxsbN++HREREdxnAwcORHBwMCZPngylUomkpCSkpKRg
# 3LhxzOojBGFhYXBxcUFZWRlevHgBBwcHimXAufAVKysrC3K5HDU1NZg6dSocHBygVCoRERGBnJwc
# 7Nu3j0ncloix3sZ6DvPZxkI6j/nKRYzXI12JsY2N8RzmM5axnsOGdiwF12H56KOPmnRWgPpRmlas
# WIHVq1fj2bNnyM3NhY+PT4vljBw5slFnRcvMzAxxcXGQyWSorq7Grl27RN9hiY2NRWFhIQoLCzF+
# /PhG79ZQLMPLhY9YGo0GCxYsQEVFBZKTkxEYGAgAqKioQEBAAOLj4zFjxgyMHTu2w2O3RIz1NsZz
# mM82FtJ5zGcuYrse6UqMbWys57AYj6Uu+Kq3IR5LwX0lbPbs2S2uGzFiBLd89+7dVssJDw9vcZ2L
# iwvGjBkDADh//jzziXX0TaVSobCwkGIxJLZ6X7p0CSqVCgEBAdzFBaif4HLTpk0A6idG5ZMY622M
# 5zCfbSyk85jPXMR2PdKVGNvYWM9hMR5LXfBVb0M8loLrsPTr16/FdQ0nB2tr3Othw4a1ul47aU95
# eXmbnR9CjM2FCxcAoNmnj/7+/rCwsOC2ERNjrTef+GxjIR1PIeUiVmJsYyHVyVh/d/nEV70N8VgK
# rsPS2qhdDSd/a+upSFuzSzf8juLz5891zI4Q46CdMM/T07PJOu0EhMXFxXjy5AnfqTFlrPXmE59t
# LKTjKaRcxEqMbSykOhnr7y6f+Kq3IR5LwXVYCCH6V1JSAgCQSqXNrtd+3nB2czEw1nrzic82FtLx
# FFIuYiXGNhZSnYz1d5dPfNXbEI+laDssRUVFra5v+H3FHj16NFqnfZLT1lBr5eXlvzM7QgghhBBC
# iC5E22G5fPlyq+uzsrIAAN26dYNMJmu0zsrKCkB9b0+j0bRYxpuTUr5JIpHokiohgqP9i4f2LyNv
# 0n5ubW3NW058MNZ684nPNhbS8RRSLmIlxjYWUp2M9XeXT3zV2xCPpWg7LN9//32L6x49eoTU1FQA
# 9ZM8mpqaNlrv7u4OoH7INZVK1WwZNTU1OHz4cKs5WFhYcMtVVVU65U2IEPTt2xcAkJeX12RdTU0N
# 8vPzYW1tDXt7e75TY8pY680nPttYSMdTSLmIlRjbWEh1MtbfXT7xVW9DPJai7bBcvHgRu3btavJ5
# bW0tPvnkE1RXVwMAli5d2mQbf39/bjkqKqrJeo1Gg5UrV0KtVreag4uLC7fc3IEiRKjkcjkAICUl
# pcm69PR0VFZWctuIibHWm098trGQjqeQchErMbaxkOpkrL+7fOKr3oZ4LEXbYRk0aBBWrFiBefPm
# IS0tDSqVCklJSfjjH/+I5ORkAEBQUFCjMaG1/Pz8MHLkSABAYmIiJk2ahGPHjiEtLQ179+7FH/7w
# B8TGxmL06NGt5jB06FB07twZALBhwwakpKTg5s2buH37Nm7fvk3vwBDBGjFiBHx8fJCWlgalUsl9
# XlFRgY0bNwIAFi9erK/0mDHWevOJzzYW0vEUUi5iJcY2FlKdjPV3l0981dsQj6XgZrrvKPv378f0
# 6dMRHx+P+Pj4Juv9/f1x4MCBFvePj4/HqFGjUFRUhOTkZK6To7Vy5UrI5XKcO3euxTKkUikiIiLw
# 1VdfQaVSYfz48Y3WnzhxAkFBQe2sWfv5+/vDz88PwP+e+owYMYIb2vnmzZuNTiKKJexc+IglkUiw
# d+9eyOVyTJkyBcHBwXBwcIBSqUReXh7mzp3L6yz3gDjrbYznMJ9tLKTzmM9cxHY90pUY29hYz2Ex
# Hktd8FVvQzyWou2wODk5ISsrC9u2bUNSUhLUajUkEgm8vb0RHh6OhQsXNnl3pSEvLy/k5OQgKioK
# p0+fxsOHDyGVSuHn54fly5dj0qRJUCgUbeaxefNmeHl5ISEhAdevX0dJSUmbc8h0tL59+yIgIKDR
# Z+7u7ty7Oubm5h32yyjWWELKha9YQ4cORWZmJiIjI3H27FmUl5fD09MTO3bswLJly966/PYSY72N
# 9Rzms42FdB7zlYsYr0e6EmMbG+M5zGcsYz2HDe1Y8tJhkcvlrY62tXbtWqxdu7bNcjw8PFot502W
# lpaIjIxEZGSkzvs05OzsjJiYGMTExDS7PigoqM18JBIJ5s+fj/nz5/+uHDpCXFwc4uLiKBZDYq13
# //79cfz4cV5itUWM9TbWcxjg99wS0nnMRy5ivR7pSmxtDBjfOcxnLGM9h/mM0xGxRPsOCyGEEEII
# IcTwUYeFEEIIIYQQIljUYSGEEEIIIYQIlmhfujc2T58+RadOnZiU3XD45VevXuHJkydM4gBo9E7Q
# y5cvWx0Y4W28fPmyXdvzWe+SkhJm9S4tLeWWq6urcebMGSZxAKC4uLhd24ux3mVlZczOm1evXrVr
# +9raWqbncGVlJbesVquZtfH9+/cb/fzTTz/h1q1bTGLl5+ejf//+Om/Pst4PHjxo9POzZ8+YDY3f
# sNyKigrern26+Omnn3D79m0mudy7dw/vvvsuAPb1rqur45ZVKhVsbGyYxGlp8uuWPH/+nOn18fXr
# 19yySqVCjx49mMS5du0at1xXV8f0WFZUVLRre5VKBVtbWya5NKx3bW0t02P57Nkzbjk/P59ZrKKi
# IgDUYRGFyZMn4969e8zKt7Ozg5ubG3r06IEhQ4Y0utB2tClTpgCoH2awqqqKWRxbW1sMGzZMp23t
# 7e15rXfDG7+Opq23qakpxo4di3379jGL1b9/f0ilUp22HTVqVLtvwNvD1tYWw4cP57Xenp6e8PHx
# YRbH1tYWAwYM0GlbExMTjB07FjU1Nczy6dmzJ1fv9PR0pm384YcfAgDGjh2L06dPM4tjZmYGmUym
# 07YeHh64cOECL/WePHkybty4wSyOnZ0dZDIZevTogeHDhzMd2bK5udBaMmbMGKajNZmamkImk8HG
# xoa3eg8ZMgRnz57FnTt3mMXSnjdtsbGxgZeXF9NzeOLEiQDq652amoq7d+8yi6Wt94QJE5j+v9qz
# Z0+dOyCDBw9GampqmxOPvw3tHIGTJ09meiw9PDxga2sLd3d3dOrUiWksuVxeItG0988bhIjUd999
# hwULFiA5ORkTJkzQdzqiFBgYiLS0NKb/eRizyspKdOnSBaGhoTh06JC+0xGlgwcPYtasWUhKSkJI
# SIi+0xGlkJAQHD9+HHV1dZBIJPpOR5QkEgmCgoJw4sQJfaciSsePH0dISAgOHDiAWbNm6TsdMVDR
# OyyEEEIIIYQQwaIOCyGEEEIIIUSwqMNCCCGEEEIIESzqsBBCCCGEEEIEq0mHpbKyEvv378e0adPQ
# p08fWFlZoVu3bpDJZJgyZQr27NnDbChFQgghhBBCCGmo0bDGCoUCK1euxG+//dZkQ7VaDbVajZMn
# T+Lzzz9HdHQ0QkNDmSe4e/duLFmyhMuhd+/ezGN2FEPOvTlPnz7FDz/8wDSGubm5UY+8k5mZyXS4
# QwDw8vKCn58f0xhCVVdXh8TEROZxAgMD0b17d+ZxhOj27dv4+eefmcaws7PTeahWMUpNTcXz58+Z
# xhg2bJjOQzqLzYsXL5jOXwHUj9I1Y8YMpjGELDs7G3l5eUxjeHh4YMiQIUxjCFliYiLT6RiA+qHG
# Wc2l8yauw/L1119jzZo13CROgwcPRkhICPr06QMTExOo1WooFApcvHgRjx49QlhYGO7cuYPPPvuM
# l0SJ/v36669Yv349xo0bxyzGoUOHjLrDEh0djYyMDFhaWjIpv6SkBFOmTEFsbCyT8oXu9evXmD17
# Nvr06cMsRkFBATIyMtCvXz9mMYQsNTUVn3/+ObOJ0aqrq9GtW7d2T4gnJhEREXj9+jXMzc2ZlP/0
# 6VN8+eWXRtthUavVWLRoEZydnZnFuHPnjlF3WGJiYpCamsrsDzulpaUICAhAQkICk/INQXh4OGbP
# ns2s/NOnT0Mmk+k8p93bMgPqn6ysXr0aAGBhYYE9e/bg448/brLxunXrcOzYMcyZMwfl5eXYuHEj
# ZDIZwsLCeEmW6N+AAQOwe/duZuX/61//Yla2Iairq4OTkxMcHR2ZlP/mLOHGyMLCAp6enszKZzkB
# pqGws7ODh4cHk7LLysqYzlptCOrq6tC7d2907dqVSfk09wnQo0cPpteJ/Px8ZmUbAo1GA0dHR7i4
# uDAp/+HDh8yfLghdp06dmN6vjRkzhlnZzTEpLi7G/PnzAdRfpI4ePdpsZ0UrJCQEJ0+ehIlJ/esv
# ixcvRlFRES/JEkIIIYQQQoyLybfffst9F3bu3LmYOHFimzsFBARg6dKlAOofu8XExDTZJjw8HBKJ
# BK6urq2WpVAoIJFIIJFIGn3v+cKFC5BIJNw7IADg7u7Obav9p1AouPVbt27lPn/69CnKy8sRFRUF
# X19fdO/eHVKpFO+//z727NnTas9bH7kTQgghhBBCmjLZt28f98OaNWt03nHNmjXcY+OGZQjF48eP
# MWzYMGzYsAHXrl1DaWkpXr58iYyMDCxatAh//vOf6asbhBBCCCGECJzZrVu3AADvvvsuvL29dd6x
# d+/eGDRoELKzs1FQUAC1Wg13d/cOS0wul0Oj0fzukbbCw8ORm5uLOXPmYNasWbC3t8fNmzexbds2
# ZGZmIi0tDXPmzMHRo0c7LOeOyt3Q/fLLL9i4cSN+/PFHlJeXw9PTEwsXLsSyZcu4rxKS3++DDz5A
# //794eHhATc3N3Tq1AmHDx/G4cOH9Z2aKFD7skdtzBa1L3vUxuxRG7NnSPdr3ChhgwcPbvfOgwcP
# RnZ2NgDg6tWrHdpheVvZ2dnYvn07IiIiuM8GDhyI4OBgTJ48GUqlEklJSUhJSWE66pWxycrKglwu
# R01NDaZOnQoHBwcolUpEREQgJydHkE/jDE1YWBhcXFxQVlaGFy9ewMHBQd8piQq1L3vUxmxR+7JH
# bcwetTFbhna/xnVYnJyc2r1zw5GMnj592jEZdZCRI0c26qxomZmZIS4uDjKZDNXV1di1axd1WDqI
# RqPBggULUFFRgeTkZAQGBgIAKioqEBAQgPj4eMyYMQNjx47Vc6aGLTY2FoWFhSgsLMT48eMbvStF
# 3h61L3vUxmxR+7JHbcwetTE7hni/xj3v+T3zPlhZWXHLL1++7JiMOkh4eHiL61xcXLjh2M6fP4/a
# 2lqeshK3S5cuQaVSISAggDv5AaBLly7YtGkTADAdYs9YqFQqFBYW6jsN0aL2ZY/amC1qX/aojdmj
# NmbHEO/XuA5LWVlZu3cuLS3lloU2q3NbE9kMHToUAFBeXo67d+/ykZLoXbhwAQCafWLl7+8PCwsL
# bhtCCCGEEMI/Q7xf4zosjx49avfOjx8/5pbt7Ow6JqMO0rNnz1bXN/wupHZYZ/J2tAM4NDfZlrm5
# Odzc3FBcXGz0k74RQgghhOiLId6vcR0W7cvz7dFwH19f347JiBiskpISAIBUKm12vfbz4uJi3nIi
# hBBCCCH/Y4j3ayZ9+/YFANy4cQM3btzQecf8/Hzk5OQAAFxdXZuMEKYdDq21CRqB+q9ksVBUVNTq
# +obfi+zRo0ejdfrOnRBCCCGEEFLPZO7cudwPW7du1XnHbdu2cTf0DcvQ0r6QX1xcDI1G02I5ubm5
# rcbRTk7ZXpcvX251fVZWFgCgW7dukMlkjdbpO3dDpe2Ra3vub9J+bm1tzVtOhBBCCCHkfwzxfs1k
# 0aJFsLGxAVA/Y71SqWxzp/T0dOzatQtA/c398uXLm2yjfeJSUVEBlUrVbDk1NTVtTgBkYWHBLVdV
# VbWZm9b333/f4rpHjx4hNTUVQP0kj6ampo3W6zt3Q6V9WpeXl9dkXU1NDfLz82FtbQ17e3u+UyOE
# EEIIITDM+zUTGxsbxMXFAagflzkkJASHDh1qcQeFQoGJEydyQwHHxsY2+4K7v78/txwVFdVkvUaj
# wcqVK6FWq1tN0MXFhVturmFbcvHiRa5T1VBtbS0++eQTVFdXAwCWLl0quNwNlVwuBwCkpKQ0WZee
# no7KykpuG0IIIYQQwj9DvF8zA4CQkBBs2bIFn376KSoqKjBz5kx88803CA4OhoeHByQSCdRqNRQK
# Bf7zn/9wO//f//0fZs6c2WzBfn5+GDlyJDIyMpCYmIhXr14hPDwcNjY2uHv3Lvbt24eMjAyMHj0a
# 586dazHBoUOHonPnzqiqqsKGDRtgZmYGd3d37qmIk5MTunXr1mS/QYMGYcWKFcjOzsasWbNgZ2eH
# W7duITo6GpcuXQIABAUFNRp/Wii5G6oRI0bAx8cHaWlpUCqVGD9+PID6J1UbN24EACxevFifKRJC
# CCGEGDVDvF/jZrpft24dZDIZVq1ahQcPHiArK4t7z+NNjo6OiI6ORlhYWKuFx8fHY9SoUSgqKkJy
# cjKSk5MbrV+5ciXkcnmrN/1SqRQRERH46quvoFKpuEbVOnHiBIKCgprst3//fkyfPh3x8fGIj49v
# st7f3x8HDhwQZO6GSiKRYO/evZDL5ZgyZQqCg4Ph4OAApVKJvLw8zJ07V1Czphoqf39/+Pn5Afjf
# U7wRI0ZwQ3XfvHlTp692kuZR+7JHbcwWtS971MbsURuzY4j3a2YNfwgJCUFgYCAOHz6M5ORk5OTk
# cKNt2dvbw8fHBxMnTsTMmTN1ejLg5eWFnJwcREVF4fTp03j48CGkUin8/PywfPlyTJo0CQqFos1y
# Nm/eDC8vLyQkJOD69esoKSlpc3Z6JycnZGVlYdu2bUhKSoJarYZEIoG3tzfCw8OxcOHCJu+uCCV3
# QzZ06FBkZmYiMjISZ8+eRXl5OTw9PbFjxw4sW7ZM3+mJQt++fREQENDoM3d3d+7dK3Nzc7qIvwVq
# X/aojdmi9mWP2pg9amO2DO1+zezND7p06YJ58+Zh3rx5HRLA2dkZMTExiImJaXZ9UFBQqyNxAfU9
# wfnz52P+/Pntim1paYnIyEhERka2az8tfeZuyPr374/jx4/rOw3RiouL4947Ix2P2pc9amO2qH3Z
# ozZmj9qYPUO6XzNpexNCCCGEEEII0Q/qsBBCCCGEEEIEizoshBBCCCGEEMFq8g4LIa2prq5GYWGh
# vtMQtdevXzObaPT169dMyjUkGo2G6USuYh5UQ1csz2HtHFrGrrq6utWBY94GXSfqf4+NYcJnfWJ5
# naipqWFSrqFheb/G97WYOixEZ127dsW9e/cwatQoZjFkMhmzsg2Bm5sbMjMz8eTJE2YxnJ2dmZUt
# dBKJBHZ2dsjNzWUWw8zMDJ07d2ZWvtDZ2NigoqKCaRsPGTKEWdmGwNPTEyqViln5EokE1tbWzMoX
# OgsLC5iYmDA9hx0dHZmVbQh69eqFc+fO4fnz58xivPPOO8zKNgSurq5M79eA+oG6+CKqDsvatWux
# du1afachWoMHD8bNmzf1nYaoRUdHIzo6Wt9piJa5uTnUarW+0xC10NBQhIaG6jsNUTt9+rS+UxA1
# b29v3Lt3T99piNqmTZuwadMmfachatevX9d3Ch2K3mEhhBBCCCGECBZ1WAghhBBCCCGCRR0WQggh
# hBBCiGBRh4UQQgghhBAiWNRhIYQQQgghhAgWdVgIIYQQQgghgkUdFkIIIYQQQohgUYeFEEIIIYQQ
# IljUYSGEEEIIIYQIFnVYCCGEEEIIIYIl0Wg0Gn0nQYgQPHr0CLm5ufD19YWtra2+0xGla9eu4cWL
# F5DL5fpORZTq6upw/vx5ODo6ol+/fvpOR5QKCwtx/fp1+Pj4wN7eXt/piNJ///tfFBUVYfTo0fpO
# RbTS0tJgb2+PAQMG6DsVUXry5AlUKhX69esHR0dHfacjBiqJRqNx1ncWhBBCCCGEENKMmv8HZuxx
# eMjmxLwAAAAASUVORK5CYII=
# " />

# The input row represents all the possible neighborhoods of a cell. Depending
# on its own state and the states of its first neighbors to the left and right,
# the cell will turn to the state given in the output row. In cellular automata
# jargon, we say this is a rule with \(k=3\), because each cell look at its own
# state and the state of its direct neighbors to the left and to the right. If
# each cell looked instead to the two nearest neighbors in each direction this
# would be a \(k=5\) rule, rules with \(k=7\) look at its three nearest
# neighbors and so on. Each rule must take \(2^k\) inputs.</p> <p>To deal with
# rules with more ease, we can treat each input as a 3 bit integer. Doing that
# and converting them to base 10, you should notice that they are ordered from
# 7 to 0. If, in this order, you take the all of the outputs as an 8 bit
# integer, the resulting number is the "name" of the rule. The rule above is
# therefore rule 126.</p> <p>To get our cellular automata going, the first
# thing we gotta do is to write a function that takes the rule's name and
# generates a python list out of it. This should be quite simple to do with
# some bit shifting and whatnot. I'm feeling lazy though, so I'll just use the
# built-in <code>bin</code> function

print(bin(126))

# The problem is that it returns a string prefixed with "0b". No big deal, well
# strip the two first characters, transform each character into an integer,
# left-pad with zeros and reverse it (because the rules are organized in
# descending order, but lists are indexed in ascending order)

def make_rule(rule_name, k):
    rule_name = int(rule_name)
    rule_len = 2 ** k
    rule = [*map(int, bin(rule_name)[2:])]
    rule = [0] * (rule_len - len(rule)) + rule
    rule = rule[::-1]
    return rule

print(make_rule(126, 3))

# Next we need to make a function that take a list representing the state and
# turn into an integer. It's just the reverse of what <code>make_rule</code>
# does

def state_id(state):
    # Thank god for the `base` argument in python's build-in `int` =)
    return int(''.join(map(str, state)), base=2)

assert state_id([0,1,1]) == 3
assert state_id([1,0,1]) == 5

# I know, this looks clunky, converting to and from strings just to convert an
# integer from one base to another, but it's a perfectly valid approach in my
# opinion, and not much slower than the other pure python alternatives (but
# more on that on a later post).

# We'll also need a simple rolling window function (and make it a generator for
# extra python points)

from pprint import pprint as print

def rolling_window(arr, wsize):
    arr = arr[-wsize//2 + 1:] + arr + arr[:wsize//2]
    for i in range(len(arr) - wsize + 1):
        yield arr[i:i + wsize]

print(list(rolling_window([1,2,3,4,5,6], 5)))

# Now applying a rule is just a matter of putting it all together

def apply_rule(cells, rule, k):
    assert len(rule) == 2 ** k
    return [rule[state_id(w)] for w in rolling_window(cells, k)]

assert apply_rule([0,0,1,1,0,0], make_rule(126, 3), 3) == [0, 1, 1, 1, 1, 0]

# And it works! But not very interesting right now, right? Before
# trying to do something fancier, let's first put together all we did in
# a nice little class

#$
import matplotlib.pyplot as plt
from random import randint
import numpy as np  # for now we'll only use numpy to help with plotting

class CAutomaton:
    def __init__(self, ncells, k, init='center'):
        self.ncells = ncells
        self.k = k

        if init == 'center':
            self.cells = [0] * self.ncells
            self.cells[self.ncells // 2] = 1
        elif init == 'random':
            self.cells = [randint(0, 1) for _ in range(self.ncells)]
        else:
            self.cells = list(init)
            assert len(self.cells) == self.ncells

    @staticmethod
    def make_rule(rule_id, k):
        rule_len = 2 ** k
        rule = [*map(int, bin(rule_id)[2:])]
        rule = [0] * (rule_len - len(rule)) + rule
        rule = np.array(rule)[::-1]
        return rule

    def state_id(self, state):
        assert len(state) == self.k
        return int(''.join(map(str, state)), base=2)

    def apply_rule(self, rule):
        assert len(rule) == 2 ** self.k
        self.cells = [rule[self.state_id(w)]
                      for w in rolling_window(self.cells, self.k)]
        return self

    def iterate_and_plot(self, rule_id, niter=None, ax=None):
        if niter is None:
            niter = self.ncells // 2

        rule = CAutomaton.make_rule(rule_id, self.k)
        states = [self.cells] + [self.apply_rule(rule).cells for _ in range(niter)]
        states = np.array(states)[::-1]

        if ax is None:
            fig, ax = plt.subplots(figsize=(10,10))

        ax.pcolormesh(states, cmap="Greys")
        ax.set_xlim(0, self.ncells)
        ax.set_ylim(0, niter+1)
        ax.set_title(r'$Rule\;%i$' % rule_id, fontsize=20)
        ax.set_axis_off()
        ax.set_aspect("equal")

        return ax

# I made a practical <code>iterate_and_plot</code> method to repeatedly apply
# the rule to the cells and plot the history (time flowing from top to bottom).
# I also added two possible initial conditions: <code>'center'</code> (where
# all cells start at state 0 except for the middle one) and
# <code>'random'</code> (which should be pretty obvious).

# Let's see what happens when we apply rule 126 a bunch of times with a simple
# initial condition

#$
CAutomaton(ncells=520, k=3, init='center').iterate_and_plot(rule_id=126, niter=255)
plt.show()

# <img 
# src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlIAAAFDCAYAAADxveDQAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
# AAALEgAACxIB0t1+/AAAIABJREFUeJzt3WvMPElVx/FfsYvcJQpIFBARQkAIElTAAPtnISCb6As1
# eHnhPZogBDV4iYpcgqhE5IVEBTEB5KLEGBNi0BATAkbdGDUYLyA3JSoKq6CoyAJL+WJmfKYvM11d
# c7r6VPX3k5DlP9NP9emq6p4z3fWcJ8QYBQAAgPlut3YAAAAAtSKRAgAAyEQiBQAAkIlECgAAIBOJ
# FAAAQCYSKQAAgEwkUgAAAJmuXzsAAHUJIbxW0iMkfbmk/5X0R5Juk3QnSXeU9BeSfiXG+FeZ7b9B
# 0lMk3VPSA2KMH7SIO3Hfd5Z0c4zxESfef7SkH9PuWO8r6U8lPS/G+KGRbR8s6fna9dGt+/++IMb4
# 3wuFD2AFgYKcAOYKITxQ0nslvTTG+KNHr99O0sskPUPSU2OMb89s/6WSnh5jvL9FvIn7/CpJvyzp
# UTHG60bef5Skn93H9fEQwl0kvUXSQyQ9+jjhCyF8maTfk/TNMcabQwj3lnSzpNfEGF9Y4HAAFMKj
# PQA5btj/963HL8YYPyvpFZJuL+kHLmj/mqSsJGyuEMJDQgi/K+n7JX3mzKYvkvSMGOPHJSnG+D/a
# HeO9JP3cUXvXS/odSb8QY7x5//LnSLqLpI/aHwGANfFoD0COa5I+KekPR977kv1/P5bTcAjhcyU9
# UruEbHExxndL+tr9vl8j6TEnNr0m6W0hhK+MMd6y/9l3hhD+U9KTj7b7du364DVH+/hHSV9gHTuA
# 9XFHCkCOGyT9cYzx1pH3niXpPyS9JLPtJ0i6ToXuSM3wAe2SoTv3Xr9VuzVTB98q6b2HO1cA2sYd
# KQCzhBDuq90dl1/tvX4vSS/W7lHXE2KM79m//kBJP7j/mdfHGN909DPPlnRTjPGmo6ZulPShGOP7
# Rvb9SO3WX31Mu8eH95T0zEILuB8r6a4xxo8cxfNF2iVXb9v/O0h6vKSbQwhPkPRUSXfV7thfGGN8
# Z4E4ARREIgVgrmv7/35pCOH52l1HHifpQZK+O8b4fYcN94vPf1i7u1TPkvQTkt501NZ3SPrrXvtP
# 1MjdqBDCd2qXkN0UY/yX/Ws/IulJkt586UFNiTF+QtInei8/W9JnJf3k/t/3kHQHSfeW9NAY40/t
# 47wm6R0hhMfGGP926VgBlEMiBWCua9r9Kv8zYoy3SVII4Y6Sfl/S90r6g6Ntb5T01hjjbSGEp0n6
# u8MbIYS7aVdG4ZeOXru7dmUV+ne7vnr/2rWjJOrR+1hebX2AKUIID5L0TEk/c7So/PDbfl8i6bWH
# bWOMb9+vpXqJpK8rGSeAZZFIAZjrBkl/dkiiJCnG+MkQwm9JenkI4cdjjB/Yv/UuSbeEEO6jXW2o
# bzxq53EaroU6tT7qBdr9xtvXhxC+Yb/NuyR9yxp1mUIId5D0RkmvjDE+7+itw2/lvW9k/dg/S3pK
# COH2McZPl4gTwPJIpAAk29dDerB2v97f98X7/95Tu4XZOhSqDCF8k6T/0q7u0sEN2q2Fev/RazdK
# +tcY4/Gdq9tr91txrzquWbWW/TqoV0t6S4zxBcfvxRg/HUK4ReO/sXirduu6Pl/Sh5eOE0AZ/NYe
# gDkO9aP+ZOS9GyVFSR8Zee9rJL2tdyfmBknvkKQQwgP2rz3x6LWH7F+7h3bXquOEa00vkvQ3x0lU
# COHbjt6/WbsF93130C6ZumXR6AAURSIFYI5r2iVLY4nUw/f//bAkhRDut797I0n3U3d91J0kfYWu
# 6lA9Z18p/JG6eqx3KOj5b5I+rt3dnI4QwkNDCN+TfTTjTv65hxDCd0m6Lcb44t5bjz/6/78h6f77
# dWOHnwvaVUB/875oKYBGkEgBmONGSR88FKTsOayLUgjhOu1+3f+QlLxXuztLB8/VbmnBP4QQHq7d
# eqfbaZfEvD+E8Bjtk7UY42ckvVLS0453FkJ4sna/Efg6g+M6uOOu6XCn/hshhCdJ+nntflvx9Uf/
# +01Jdzva9E2S/lK7hegHT9fubtTqjyYB2OJv7QE4a18f6g2SvlDSwyR9SrvHV78dY3z50XaPlPSL
# 2j2C+5Sklx3WOu0f3b1C0rslBUmvknSTdo/y3i/pOTHGT4UQnqNdOYP3xBh/6Kjt67T7jbf7SPon
# 7f7kyp/HGH/d6Phet2/7Ydolc/+uXVmGX4sxvnG/3Ucl3X0f/+HCefj/Px1jfP5Rm5+n3d8cvIuk
# w+PM58YY//7SeAH4QiIFAACQiUd7AAAAmUikAAAAMpFIAQAAZCKRAgAAyLRWZXNWuAMwFUIQvzwD
# YCHh1BvckQIAAMhEIgWgeocC6leF1AGgDBIpAFU7JE+Hx3ohBBIqAMWQSAGo1nHC1E+eSKYAlLDW
# YnMAuEj/TtTY+yxAB7A07kgBqM7Unahz7wOAJRIpAFU5vhN1vC7q+L+n3gcAa2v90WLutQOY7dKE
# iMd8ADKdvPiwRgpAFabWRKX8PGumAFjj0R4A9y5d88SaKQBLIZEC4Nq5NVElfh4AzmGNFAC3phKe
# qevXpT8PAHsnLyYkUgDc6f/23bltlnofAI7wR4sBAACskUgBcCXlT71cWpCTxecArJBIAXCjvzB8
# bHH4pQU5WXwOwBJrpAC44CGZYb0UgBMoyAnALw8Lv48fCZJQAUjFoz0Aq/KwXillXRYAjCGRArAa
# D+uVUtZlAcAprJECsIqURGXp65OHGABUgYKcAPxILZZ5bpulY0jdBsAmUJATgA9zajyd2mbpGFK3
# AQASKQDFTK2JKrFeKWVdloe1WwDqwKM9AEVYJCKXXq88xACgSqyRArAei7VGl7bhIQYA1WKNFIB1
# WKw1urQNDzEAaBOJFIBF9CuF5641urQNDzEAaBeJFAAAQCbWSAEwZ1XocqqdqTYu/XmrNgBUj8Xm
# AMqwKHSZUpAztY3c963aANAEEikAyxu7e9O/xvS3mXp/bhsWMVjFCaAZ/NYegGWNLcg+fv3UNnML
# cp5ro38na+7P58Y5dqwAtoE7UgAuRgLRxZ0poDknL3LXl4wCQHtYJ9R1KPtAfwDbwKM9ANkoUtlF
# fwDbQyIFIAtFKq9YFR8FUB/WSAGYjdpKV6xqZgFwjfIHAGxQW+mKRS0qAFUgkQJwOWorXbGqVwWg
# CtSRAnAZaitdsaiZBaAN3JECcJbVh38rd2Ms+qOVvgA2hDtSAAAA1rgjBeCklD8ePKed2u/EWBxH
# K30BbAx3pADMc+rvz13STs1rhCyOo5W+AHCFO1IABsbumsy9kzJ2N6vWuzH9uHOOw6INAKuh/AGA
# NBYFJlsqUmlRfLSl/gA2ikQKwDSLApMtFakscaxW69AALIpECsB5KcUjLQpy1lKkssSxbqmAKVA5
# FpsDOC2leKRFQc5ailSWONb++577A8Bp3JECNs7LB7eHOzFe+kLy0R8A/h+P9gAMeVmr5CEOT2uV
# PPQHgA4e7QHo8lLTyEMcVjWzLHjoDwDpSKSADfKyVslDHJ7WKnnoDwDz8GgP2BiLukgl4pCWj8VD
# DAdexgXAKNZIAbCpi1QyjiVj8VLvKuVYWTMFrI41UsCWhRAm196UWpszJ46lYkk51hL9kXKsrJkC
# fCORAgAAyMSjPaBxKX88uNQf1M3Zr3UsOftcoj9y9ssjPmA1rJECtsjiUZB1AnOJS2PxEIOnOAAk
# I5ECtsbi7oXVom/LWHLb8BCDpzYAzMJic2BLLBYoWy36to4lpw0PMSzVBgvQgXVxRwpozKl1Ncev
# zW3j1GspbYzFMue6c+k6IYt1Rt7bmNsOgNl4tAdsgUWBSS9tpLRzaRwlYkhpI6UdT8VDgQ0ikQJa
# Z1Fg0lsbl+xnS8eaug2AbCRSQMv6dyv65/XY3YypbcauDSX2c2kbWzrWOdsAuAiJFNCq1NpDKdtc
# UlvJw363dKyp+wVggkQKaBG/sYVzSKYAMycvtteXjAKAHe484JxDaQTmB7As6kgBFbKoR4R2MT+A
# ckikgMoc34kaWyuDbWN+AGWxRgqoBHWEMMWi5hWAUfyJGAAAAGvckQIqYFW0Ee2yKB4K4CTuSAG1
# SvnjwSwu3rap8Wd+AMvhjhTgmEXRRrTrkkKgx68BmERBTqA2FncO+KBsl9WdJeYIkIRECqiJxV0l
# 7ky1y2psmSNAMhIpoBYWf4CWP2LbrpQ/dFyiDWBjWGwO1MCimOKpNlhkXL+xsT1+fU4b/XaYH0Ae
# 7kgBTlgUU6RoZ7ssxpb5AWTj0R7gWWoNoJRtzp3TrImpk8XYMj+Ai/BoD/BqTg2glG1OvU8toTql
# jJtFHSnmB5CHO1LAinJqQs39mZRaQ/DJYmwtfgYAj/YAd7x86+fD0ifmB+AKiRTghafK0tx58MnL
# uHiJA3CANVIAAADWSKSAglIWjpfC4mKfvIyLlzgA70ikgEL6xRTXLIRoUfgT9ryMi5c4gBqwRgoo
# wFMhRIvCn7DnZVy8xAE4w2JzYC2eCiFaFG2ELatiq5axXFIYFmgUi82BNXgphJhSkJM1MeVZFFtd
# IpbcwrDAFnFHCliIRXFNyzjO7YeCjOVZFFtdKpacuQs0jkd7QEkW39Ytzk0vcaDL07h4igVwjEQK
# KMXim7q3Ni5tB1e8jK23WADnSKSAEvrf7nPOL69t5LaDK17GxWpsLY4HqASJFLA0i/UsS7Yxpx3W
# xNjzNrZLxcL8QKNIpIAlWdTeKdFGSjueal61wsu4eGkDqBCJFLAUi9pMFvV7LPfjoeZVK1oaW081
# r4DCqCMFLMGiNpNF/Z6UNkrEiq4SYzt3P2vOQ6BF3JECMljVZirxM6ViRZf3sc35GQ81r4CVcEcK
# AADAGnekgJl4ZDHEXYcu5kgX8wMNYLE5YIHHFUP0SRf90UV/oBE82gMu1V9Iy10HFhf30R9d9Ae2
# gDtSQAKLQoitYXHxFasily3hnEFjeLQH5KIA4ZBF8dBWMD+G6BM0iEQKyEGByiGLwo+tYH4M0Sdo
# FIkUMFf/W/XYuZKyTUumjnfsTkSrfZJyrMyP7c4PNIfF5sAcx9+Yx9Z4HC82P7VNa1L6pP9+f5tW
# pBwr8+P0YvOt9Am2gTtSQI/Fhb2lb9lWH3St9AnzY4g+wQbwaA9IYbF2o6X1H1a/adVKnzA/hugT
# bASP9oApFjVvWqqbk/JHaue2U3OfMD+G6BOAO1KAJJuaSC3VVUr5I7WpbRz/TK19wvwYok+wMTza
# A06xqInUUl0lixpALdURKjE/UtvxwOpYWjpnsAkkUkBfyvofi5o4NX3LLnW8tfRJiWOtqeI35ww2
# jDVSAAAA1rgjhU2yKqY4twCh52/YSxxvyjZe+6TEsdZUoLLU8dYyP7A5PNoDDlIWUqf+O+dnPH4w
# pMRaoo+8WGs+1NIfY69t7ZzB5pBIAZKvX6/28uHgpU889IeXvpB89IdEnwB7JFKAl2+3nhYXe+uT
# NeNgXPzHIa0fCzaLxebYNi9F/6yKXFrw2CdrxcG41BHH2L+BtXFHCs3zsu7C05oYr32yRhyMSz1x
# rBkLNo9He9gmL4UQvcQh+SmE6KFPPMRwUMu4eIlDIplCUSRS2B4vhRA9Faj0UgjRw9h4GRerIpeW
# sXDOAAOskcK2TK3vKLXuImWdSYm1KCGEWX2y5DoUD2PjaVzO/btUHCn72do5A6TijhSa46V+T85+
# l4zj3H5KrYnxMDbexuWS2kxLxbL1cwYYwaM9bIPFt1OLc4I4hjzE4iEGT3FIfmLxEgdwAokU2mfx
# zZQ2xtvwFEtuGx5i8NSGp1i8tAGcQSKFdo19k82Z1/12aKOdfvUQw1Jt5LTT0thatQFMYLE5AACA
# Ne5IoWopC6nntNNyG3PasVhc7GVsvI/LWmO7VCw1tgEk4NEe2pOyODVlfk+101IbKe14aSOlnUvj
# YFzWaSOlnVJtAIlIpNCWlG+dU9ukfJu33M/WYl37eLd0rMSa1wYwA4kU2pGysHRqm5TFtkvsZ61Y
# 1zreNWLd0rHm7mdrx3uqHWAGEim0IWWNyNSaiZT1P6n/Lr3fmmJdY79bOtZL91tTrNb7BTKQSKF+
# Y98yAWAOkilkOvkBdH3JKIBcrHcAcKkQdn9zkusILFFHCu4d34nirhSAHFxHsBQSKbh2fCdqbM0D
# AJxzuAslcR3BMlgjBbemLnTcngdwTkqyxHUEiVhsjrpQIwbAJSxqUQFHTiZSPNqDO1NrGVjrAOCc
# /jWC6wiWRCIFV6bWMpx6nwshAGn8GnH8+qltuIYgF4/24ILVRYxb9MB2WVxHuIbgBB7tAQAAWOOO
# FFZn9SccWDgKbJfF+c81BGdwRwo+9W/F59ya76+RYq0DsC0W5z/XEOQikcJq+gs+cxZ99u9msXAU
# 2BaLheMsPscleLSHVVgUyqPYHrBtFkV7uY4gEQU54YdFoTyK7QHbVuIaYbV+E01gjRR8SFmHYFGQ
# k/UOQLvmXiNyriMW6zexDdyRQjH9b39j3wantjn17zk/A6BeJa4RKdcmbA6P9rAuL9/muAgC9eI6
# ghWRSGE9Xr7JeYkDwDye1ipxHdks1khhHV7WKnmJA8A8ntYqcR3BGBIpLMZLbRYvcQCYx6LW3FKx
# rBUH/OHRHhZhUd+lRBwSt+gBjzydu16uZ1gVa6RQjkV9l5JxlIgFQDovdeJSrhGsmdoM1khheSl/
# 867UGgNqxAB18lInLuUawZopSCRSAAAA2Xi0BxNWRe8sY6HYHlAXi6K9S8SRsl+uIc1jjRSWY3FL
# 22oeeooFQDov566XOOAOiRSWYfEtzGrRt2UsXAiBcrycu56uZ3CHxeawZ7HQ0mLRd8oi97mxsHAU
# KMPLuevleob6cEcKWVL+MOjcNk69ltLGWCxz5jbrHYDyLM47r23ktgO3eLQHOxaF8ry0kdIOF0HA
# nsV5V6KNlHY8FQ/FYkikYMOiUJ63Ni7dD4B5tnaN4DrSBBIpXK7/ras/d8a+lU1tMzb/5u7Hoo3c
# /QBIt9Y1Imc/pWJFNUikcJnUGiop21xSI8bLfgHMs8VrBNeRppBIIR+/edLFRRCYh2vIENeR6pBI
# IQ/foLroD2Aezpkh+qRK1JHCfNRV6ur3B30CnMc1ZIg+aQ93pDBgVZupJRZ1s4At4ZwZYs1U1bgj
# BQAAYI07UuigsNwQfQLMwzkzROHf6rHYHNMoLDdEnwDzcM4MWRQPxepIpHAeBSqHKLYHzGNR5LI1
# FgWG4QKJFE6zKGDXGosif8CWcM4MWRQPhRskUhhn8eu3rZ3w9AkwD+dMl1VZg5b6pAEkUhiy+DbY
# 2jdK+gSYh3Omy+quUkt90gjKH6DLoihca4Xl6BNgHs6Zrn78OcfTL/Zbe59sAXekNshivVNrz/aX
# 7JMa+wOYwjnTlfJHi1PbOP6ZmvukMTzaw45FLZPWasSU6JOa+gM4x+r8b+mcseiT1q6rDSKRgk0t
# k5ZqxKTcRbM43lr6A5jCOTNU6nhr6pNGkUhtnUV9l5ZqxFjVzaJGDLai1DWipnOm1DWipj5pGInU
# llnUMmmpRkzKWoYl+8hbfwBTOGeGUmIt0UcohkRqq7z8xoeXk95Lf0h++gQ4h3NmyEufeOmPjSCR
# 2hpPv0Xn5RuUtzik9WMBzuGcGfLWJ2vHsSHUkQIAALBGItUgi6JwVrwUlvMYx9i/AS84Z4Y89gnX
# kPXxaK8xFkXhloqFOPyMDXAO58x0LFuPY4NYI7UFngq6eSm256VPvMQBTOHcHaqlT7iGLIpEqnWe
# Crp5KbaXGsfSsXgaG+AczpnxfZzbz9auZxvGYvOWpTwvL/FMPYTpP7ZZ6tn+nDiWjMXL2ABTOGdO
# 7+PUfrZ2PcM47khVzqIonGUc5/ZT6tl+zn6X7JO1xwaYwjlzPo6U/bZ+PQOP9ppk8a3DYvy9xCH5
# icVLHMAUL3OVOIY8xQISqeZYfOPw1oanWFpoA5jiZa622IanWLiOmCCRakn/W0rOGHptI6cdizbG
# 2qm5DeAczpkybeS042ls0EEi1QqL5/JLtjGnHYtn+ylrs3JiqbkN4BzOmTJt5LTjaWwwQCLVgqnn
# 5SljWaKNlHa8tJHSTk1tAOdw3s1vI6WdltrASSRStZv6RpHyjaNEGzXFmnIXraZYgXO2es5s7Xgv
# 3Q9OIpGq2dSz7pRn4XPbyNmPRRs5+1nreD3FCpzj5ZxZ67yrKdY1r2c4i0SqRinPy1Oehc/9mUv2
# W1OsNe731GvAKV7m7tb2W1usmHQykaKyOQAAQCbuSDk1dqsW6OMbJc7hOoIpXEOS8WivJtx2RQrm
# Cc5hfmAKc2QWEqlasLAYKVg4inOYH5jCZ81srJGqwfG3g7GFg4A0Pk+YIzhgfmAKnzW2uCPlRMoE
# 5tvCtjFHMGVqjjA/wHUkG4/2PLMoxoa2UWwPUyyKPqJtfNZchEd7Xh1/QJ76ppCyDdrVH/OxOcAc
# 2bap8Wd+gM+a5XBHakUWxdnQNort4Ryr4rloG581Jni0541Fts8EbxtzBOdY3TFgjrSN64gZEilP
# LDJ9vi20jTmCc6zGljnSNq4jpkikvLCo70KNmLYxR3CORf0fagi1j+uIORabe2BR34UaMW1bco4w
# T+pnUf+nvx6G60h7+KwpiztSBVjV7aBGTNssxpcaMe2yGFvmR9v4rFkUj/bWYlX/hxoxbUsd35Rt
# qBHTnlLXCOZHvfisWRyP9gAAAKyRSC3IqpAixfbaNmd8U7Y59T7zpE6lrhHMj3rxWbMuHu0txKKQ
# 4iXF9jZ427VKOeO5xDyCT0teI+b8DPzis6YY1kiV5ClT39Akr46XecIc8Yn5gSle5oi0iXlCIlWK
# lyw9ZeEh1uFpbLzMV3R5GRcvcWDIy9h4up4tjMXmJXh5fpzyvBzr8DQ2XuYruryMi5c4MORlbDxd
# z9bEHSkjXp4fpzwvxzo8jY2X+YouL+PiJQ4MeRkbT9ezQni0tyQvxcusirHBnqex8TJf0eVlXLzE
# gSEvY+PpelYQidRSUouXndumRByp28Cep7Gh2J4/KdcIb/OjRCzo8jI2nq5nhbFGagkW9X9KxJG6
# Dex5GZsQputIMUfKs6r/Yx3LmtczDHkZGy/XM2+4I5XJov5PiThSt4E9L2NDjRifLOr/LBXLWtcz
# DHkZGy/XsxXxaM+SRZZt0e9e4sCQl7HxEge6PI2Lp1jQ5WVsvMSxMhIpKxYZdkttYMjL2Fi2cWk7
# uOJlbL3Fgi4vY+OlDQdIpC41lpHn9F2/nZrbwJCXsVmijdx2cMXLuHi6nqHL09h4acMJFpsDAABY
# 445UgpTFunPaaaENDHkZm1NtzGmHxcX2vI3tUrEwP/J5GhsvbTjCo71cKYvspvrQoo2Udkq1gSEv
# Y+NpvuKKl3Hx0gaGPI2Nl+uZMyRSOVKy56ltUr4xWu5n6TYwVHJsSu3nkjbQ1dLYWsWKLk9jw2fN
# SSRSc6UskJvaJmXR4BL7WSpWDHkZGy9zEV1exsXLPMSQp7HxMo+cIpGaI2UdwtSz35Q1Jqn/9rBf
# dK01Njk/UypWdHkf25yfuXTuosvL2Hjar2MkUqnGsuWtq2CCF8UcGWKOdDFHupgfQ8yRIefzhEQq
# Bd+ghuiTLvpjiD7poj+66I8h+mSogj45mUhRR2rv+NsB3xR26JOufn/QJ8yRPvqji/4Yok+Gau8T
# 7kiJZ/t9Kc/Lt6byZ/uL4Ly5wjkzxDkzxDnTVdl5w6O9U6ayX4eDuaiUbwP0yRB90rWl/mB+DNEn
# Q5wzXRXOERKpMVOZr+PMeBEpx0uf5G3TEs6bK8yPIfpkiHOmq9I5QiLV18+Gc+pltGTs2wF9Mn28
# 9Mn5OTK2TSs4Z4aYH0N81nRVfN6QSB1rvNbFbBY1RVpjUXelNZw3Vzhnhjhnhjhnuio/b0ikJLvf
# BnAwoGYs+qSl/pDokz7Omy7mxxB90sU5M9TAHKH8AQAAgLXN3JGyumXq6DbjxSyOpaX+kOiTPs6b
# LubHEH3SxTkz1Mgc2fajPYsFjq0tkrRYzOd0QWA2+qTLas630ifMjyH6pIvPmqGG5sh2E6mxLHZu
# ZtvaIkmLxXytLZJcsk9a6I9Tr6W0cfwztfYJ82OIPuninBlq7LNmm4lUyuK2qeO3aMOTqeNJORb6
# ZJk2vOC86eKc6bI6Fs4Z+zY8afC82V4ilZL5Tm1j0YYnpY63lj5J+WZTah55wXnTVeJYa7qbyzkz
# xDkz1OhnzbYSqZTnqVPbWLThydzjTdkmpw0vLI43ZZuW5kjKNlb96gHnTFep461lfkh81oxp+LzZ
# TiKV8kx2apuUZ7I1Pdsvcbw1Pdtfa0547Q+J86ZvrflQS3+MvcY5s+1zRmr+s2YbidRYlroGTxOc
# Puny0h8SfdLnoT+89IXkoz8k+mSMlz7x0h/SJvqk/UTKS5buLQ7JTyzE0Y1D8hMLcTAuNcQh+YmF
# OLpxSH5iWSiOk4lUE5XNjwdyzazYYxxj/y7JY594iWPs3yV57JO14mBc6ohj7N8leewTL3GM/buk
# Nfuk+jtSXp4fe43DUyzEwdh4jINxqScOT7EQx+bGps1He1NZZ6ljqyUOyU8sXuKQysTiJQ6JsfEW
# w0Et4+IlDslPLMQx5CUWwzjaSqRSnsmWyoyn9lPq+XHK8XrrEy9xLB0LY5Mfx5KxeBkXrmfz40jd
# xiqOc/thbPK2KRGLcRztJFJj2Wf/GPrbLH0hTo1jqVhSjrdEnzA28+NI3cY6jrH9bGlsGJfpWDhn
# GJu5caRuYx3H2H4WiONkItXEYnMAAIA1VHVHKmVxW6mFeDn7XSKWnP0uGce5/TA2jI2HsfE2LlzP
# 0uNI3cY6jpT9MjbNX8/qf7Q3ditv9k6NL8SXsIiFOIa8xEIcQx5i8RCDpzgkP7EQx5CXWIhjt/uT
# b9SQSFlkk1YL8SxjoY1uG55ioY1uG55iyW3DQwye2vAUS4tteIqFNrptZLZTbyJlsWDMYiGe1WK+
# JY6npTZy2mFsyrThKZZL50itxzHWRk47LY2t5zZy2mFsyrSR0U6diZTFc06L58cpz2RzYmmxjTnt
# MDZl25gjiSiSAAABgklEQVTTTktj431c1hrbpWKhjfrPmRramNOOxdioxkRqLHscNDIRe0ttpLTj
# pY2Udry0kdJOS22ktOOljZR2Lo2DcVmnjZR2vLSR0k5LbaS046WNlHas+kS1JVJTmWJKRpqSbabu
# x6KNmmK9pI2aYq1xbGqKde3j3dKxEuuybRCrvzZK7uew6ck3vCVS/eyxH99Ydjm1zdgxzt2PRRut
# x7q1460p1rWOd41Yt3SsufvZ2vHWFCvXMz/H29/85BueEql+Zjj171I/M5bps9/6Y61xvzXFusZ+
# t3Ssl+63plhr3G9Nsda436VjHRFOvnHmh5Y02Olx5wAAAKzhRF7kLpECAACoHn9rDwAAIBOJFAAA
# QCYSKQAAgEwkUgAAAJlIpAAAADKRSAEAAGQikQIAAMhEIgUAAJCJRAoAACATiRQAAEAmEikAAIBM
# JFIAAACZSKQAAAAykUgBAABkIpECAADIRCIFAACQiUQKAAAgE4kUAABAJhIpAACATCRSAAAAmf4P
# G48asXue09UAAAAASUVORK5CYII=
# " />

# Whoa! Look at that nice <a
# href="https://en.wikipedia.org/wiki/Sierpinski_triangle">Sierpinski
# triangle</a>! If you're not sold on cellular automata by now, there's not
# much I can do for you, buddy. As you play with different rules you'll notice
# they show a variety of different behaviors

#$
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(8,5))

CAutomaton(ncells=63, k=3).iterate_and_plot(rule_id=12, ax=ax[0,0])
CAutomaton(ncells=63, k=3).iterate_and_plot(rule_id=1, ax=ax[0,1])
CAutomaton(ncells=63, k=3).iterate_and_plot(rule_id=45, ax=ax[1,0])
CAutomaton(ncells=63, k=3).iterate_and_plot(rule_id=150, ax=ax[1,1])

fig.tight_layout()
plt.show()

# <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAjgAAAFhCAYAAAB9HNBUAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
# AAALEgAACxIB0t1+/AAAGIdJREFUeJzt3XvMfVlZH/DvwzDIRUAL4w3wAihYEEaNUIrMj4GKjDGp
# 2GJIaYNoJUUolwwSVFqgFFOQ8odE5JZYgUGJEqqh0EzboJAgTTAYouXmoLQW5CJQZBQGmNU/9nmZ
# M++cd857ztnntvbnk0xefmfvs/fa++y9eM5az3l2tdYCANCTW+y7AQAAYxPgAADdEeAAAN0R4AAA
# 3RHgAADdEeAAAN0R4AAA3RHgdKiqfqOq3lNV11fVtVV1dVW9tap+v6reVVUvq6rv2WD7V1XVJ2bb
# /7Yx236Ofd+2qt57M8sfUFVvrKq3VNV7q+rVVfUtu2wjTNmU+x8OiwCnQ621xyX5p7N//mpr7RGt
# tStaaw9N8g+TXJfk3VV1Yc3tPzbJa5L8n9baR8Zo83lU1Q8k+YMk9zlj+fcleX6Sx7fWfiTJg5J8
# Z5L37LojhKmaav/D4RHg9Ouy2d+r519srV2f5OVJLk7y1A22fyHDzb51VXXvqnpzkp9N8uWbWfX5
# SZ7YWvtckrTWrs1wjJck+Q9bbyhwYor9DwdGgNOvC0m+kOQdC5Z9++zvZ9bZcFXdIcml2VEH01p7
# f2vtR1trj0/ygSR1xqoXkrytqi6Ze+8fJ/l/SR6+/ZYCM1PsfzgwApx+XZbkna21Ly5Y9uQkn03y
# wjW3/ZAkF2VHHcwKPpzkG5Lc9tTrX0xym903ByZriv0PB+aW+24A46uqu2b4lvTKU69fkuQFGaZs
# HtJa++Ds9XskedrsPa9rrb1h7j1PSXJFa+2KuU1dnuSjrbU/W7DvS5M8McO3s4uT3DnJk1prnx/r
# +G7GP0jyta21T8y151syBD1v28H+YfIm3P9wYAQ4fTpJ3rt7VT0nw+f84CT3TPJTrbUnnKxYVbdI
# 8owM36qenOQXkrxhbluPS/Inp7b/0Cz49lRVP5mho7qitfax2Ws/l+RhSX5v04NaprX2t0n+9tTL
# T0lyfZJf3Pb+gSQT7X84PAKcPl1I8ncZEm6/kiRVdesk/zXJzyT573PrXp7k6tbaV6rqkRnmmDN7
# z+2T3C/Jr869dsck989Nv509aPbahbnO5QGztvz62Ad4HlV1zyRPSvJLrbV37aMNMEH6Hw6CAKdP
# lyV590nnkiSttS9U1W8neWlV/Xxr7cOzRe9L8smqukuSH0ryT+a28+DcdK77rPnv5yb5dJJHVdWP
# z9Z5X5LH7GN4uKq+Jsnrk7yitfZvd71/mLDJ9z8cBgFOZ6rqG5N8V5I3LVj8rbO/d86QkJvW2kdn
# 7/uJJH+T5C1z61+WYa77mrnXLk/yV621+W9aF2f4ldKrWmvPHOlQ1lZVleFb21taa8/dc3NgMvQ/
# HBK/ourPSf2JP1yw7PIkLcknFiz74SRva6196dS23p4kVfUds9ceOvfavWev3SnDtTTfEe3T85P8
# 6XxwU1X/Yn/NgcnQ/3AwBDj9uZChE1nUwdx39vfjSVJVd5uNdiTJ3XLj+e/bJPn+3FDH4sqqul1u
# XH/ipFDXp5J8LsOvFm6kqr67qn567aNZrJ21oKoen+QrrbUXnFr0gyO3AbipSfc/HBYBTn8uT/KR
# 1tonFyw7mfdOVV2U5HmttZOb9UMZvgmdeHaGKcy/qKr7ZpjPvkWGm/uaqnpgZp1Ya+3LSV6R5JHz
# O6uqh2f4hcRrRziuE7ceNl03qWtTVQ9L8ssZfr3xurn/fivJ7UdsA7DYZPsfDk/dcH1xrGb1Ja5K
# 8s0ZnpNyXZJ3JXlja+2lc+tdmuRXMgzlXpfkJSdz2bMh4JcneX+GSp2vSnJFhiHha5Jc2Vq7rqqu
# zPCzyw+21p4+t+2LMhTuukuSv0xyqyR/1Fp7zUjH99rZtu+ToZP76ww/H311a+31s/U+neSOs/af
# XNgn//vft9aes2lbgBvT/wz9D4dHgAMAdMcUFQDQHQEOANAdAQ4A0B0BDgDQnW1WMpa9PEE3lLUY
# SGKftFq+yihcZBOkr2HOwr7GCA4A0B0BDgDQHQEOANAdAQ4A0J1tJhkDbN3pZFP6dDqJeFlSseti
# Os66FozgAADdEeAAAN0R4AAA3ZGDAxw1Bd6maVmhP9cFRnAAgO4IcACA7ghwAIDuyMEBjpp6J9Og
# Dg5nUQcHAJgMAQ4A0B0BDgDQHTk4wFFT72Sa1MFhGSM4AEB3BDgAQHcEOABAd+TgAEdNvZNpUAeH
# s6iDAwBMhgAHAOiOAAcA6I4cHOCoqXcyTergsIwRHACgOwIcAKA7AhwAoDtycICjpt7JNKiDw1nU
# wQEAJkOAAwB0R4ADAHRHDg5w1NQ7mSZ1cFjGCA4A0B0BDgDQHQEOANAdOTjAUVPvZBrUweEs6uAA
# AJMhwAEAuiPAAQC6IwcHOGrqnUyTOjgsYwQHAOiOAAcA6I4ABwDojhwc4KipdzIN6uBwFnVwAIDJ
# EOAAAN0R4AAA3ZGDAxw19U6mSR0cljGCAwB0R4ADAHRHgAMAdEcODnDU1DuZBnVwOIs6OADAZAhw
# AIDuCHAAgO7IwQGOmnon06QODssYwQEAuiPAAQC6I8ABALojwAEAuiPJGDhqCrpNg0J/nEWhPwBg
# MgQ4AEB3BDgAQHfk4ABHTUG3aVLoj2WM4AAA3RHgAADdEeAAAN2RgwMcNfVOpkEdHM6iDg4AMBkC
# HACgOwIcAKA7cnCAo6beyTSpg8MyRnAAgO4IcACA7ghwAIDuyMEBjpp6J9OgDg5nUQcHAJgMAQ4A
# 0B0BDgDQHTk4wFFT72Sa1MFhGSM4AEB3BDgAQHcEOABAd+TgAEdNvZNpUAeHs6iDAwBMhgAHAOiO
# AAcA6I4cHOCoqXcyTergsIwRHACgOwIcAKA7AhwAoDtycICjpt7JNKiDw1nUwQEAJkOAAwB0R4AD
# AHRHDg5w1NQ7mSZ1cFjGCA4A0B0BDgDQHQEOANAdOTjAUVPvZBrUweEs6uAAAJMhwAEAuiPAAQC6
# IwcHOGrqnUyTOjgsYwQHAOiOAAcA6I4ABwDojhwc4KipdzIN6uBwFnVwAIDJEOAAAN0R4AAA3ZGD
# Axw19U6mSR0cljGCAwB0R4ADAHRHgAMAdEcODnDU1DuZBnVwOIs6OADAZAhwAIDuCHAAgO4IcACA
# 7kgyBo6agm7TpNAfyxjBAQC6I8ABALojwAEAuiMHBzhqCrpNg0J/nEWhPwBgMgQ4AEB3yk/pAIDe
# GMEBALojwAEAuiPAAQC6I8ABALojwAEAuiPAAQC6I8ABALojwAEAuiPAAQC6I8ABALojwAEAuiPA
# AQC6I8ABALojwAEAuiPAAQC6I8ABALojwAEAuiPAAQC6I8ABALojwAEAuiPAAQC6I8ABALojwAEA
# uiPAAQC6I8ABALojwOlQVf1GVb2nqq6vqmur6uqqemtV/X5VvauqXlZV37PB9q+qqk/Mtv9tY7Z9
# hTY8o6qeteD1D1TVY6vqLlX1dVX1j6rqv1XVvfbRTuhFz/1KVd22qt57M8vP1a9U1b2q6o1V9ZKq
# +o+zc/YN2z8CFqnW2r7bwBZU1T2SfCjJi1trz5x7/RZJXpLkiUke0Vr7gzW3/+Ikj26t7TzAmXV+
# /yvJC1tr/+7UsutPrf6lJE9rrf3artoHveqxX6mqH0jysiTf11q76Ix1lvYrVXXHJH+a5JmttdfP
# Xvv5JP9stu0vbaP9nM0ITr8um/29ev7F1tr1SV6e5OIkT91g+xeSrNWJjeAXk9zmjGX/O8krk7wp
# yYuS3E9wA6Pppl+pqntX1ZuT/GySLy9Z/Tz9yjOT3DLJb8299vIk90ry06M0mpXcct8NYGsuJPlC
# kncsWPbts7+fWWfDVXWHJJdmuHl3qqp+PMn/SPIvz1jlz1tr/2qHTYIp6aZfaa29P8mPzvb9n5I8
# 8GZWP0+/8ugk/3MW7J3s4zNV9f7Zsp33l1NnBKdflyV5Z2vtiwuWPTnJZ5O8cM1tPyTJRdnxCE5V
# fW2SK1prb9jlfoGv6q5fGUNV3T7JPTOM9Jz2sSTfv9sWkRjB6VJV3TXDt6lXnnr9kiQvSHJJkoe0
# 1j44e/0eSZ42e8/r5gOIqnpKhqDiirlNXZ7ko621P1uw70szzMN/JsNw9Z2TPKm19vkRDu1ZSX5p
# yTpfU1XPTnKnDPPk90jyrNbah0bYP0xWx/3KeSzrV05yhj634L3XJrlDVV0sD2e3BDh9ujD7e/eq
# ek6Gz/nBGb5h/FRr7QknK86SA5+R4dvXk5P8QpL5EZLHJfmTU9t/aBZ8y6qqn8zQoV3RWvvY7LWf
# S/KwJL+3yQHNOrjPt9b+fMmqlyT59dba/52977FJ3lFV92+tfXyTNsDEddevrGBZv3KH2XrXLXjv
# tbO/X5fkk1tvKV9liqpPF5L8XZInttae11r7N0l+JMmHk/zMqXUvT3J1a+0rSR6Z5AMnC2bDrvfL
# XKcz+6XA/XOqI6qqB2X4ZvfEuU7oAbO2vHOTg5l1lk9L8uJl67bWvvOkE5r5zSS3z9DBAuvrql9Z
# xTn6la+crLrg7RfP/i78hRbbI8Dp02VJ3j3rXJIkrbUvJPntJI+uqrvPrfu+JG+uqrsk+aEkV80t
# e3BuOid+1jz5c5N8OsmjquqXq+olGTqsx7TWPrXh8Twhw7enZb90uIlZwt+nkvzjDdsAU9dbv7K2
# Bf3KzY3M3C5D4PM3224XN2aKqjNV9Y1JvivDzxlP+9bZ3ztn+NaV1tpHZ+/7iQw34Fvm1r8sw5z4
# NXOvXZ7kr1pr89/ILk7y8CSvmq+NMYaq+qYkf7+1tugXCHVq3bcnSWvtslPrXZTk743ZLpiS3vqV
# VZyzX/l4hiDm6xds4nZJPttau3bBMrbICE5/Tm7CP1yw7PIMN+EnFiz74SRvO5UEd1mStydJVX3H
# 7LWHzr1279lrd8pwLc13WGN5eJJ7V9Wb5v5782zZY2b//rHZv783Q2dy2p2TfGQLbYOp6K1fWcXS
# fmUWvLwnNwR78+6Z5I+31jrOJMDpz4UMnc2ijui+s78fT5KqultVnYyC3C03nie/TYafNp7Uu7iy
# qm6XoU7FyTDySUGvT2X49cDJXPNXVdV3V9XaRa5aa1e11h7RWnvUyX9JnjRb/Juz1/7z7N9vzTAc
# Pr//701yqySvW7cNQF/9yhnOKut/3n7lv+RULZ3ZL8numuR3xmsm5yXA6c/lST7SWls0J/zhk/9R
# VRcleV674VkdH8rwjenEszNMYf5FVd03w5z6LTJ0AtdU1QMz6+xmuTGvyJBM+FVV9fAMv6R47QjH
# Ne9Wp/6eeFGSV8w60cw62adnSEZ80chtgCnpvV+59bDpWlQh/bz9yq8luV1V/fO51/51hsc3vGrE
# tnJOnkXVgVkdiquSfHOS+2T4qeK7kryxtfbSufUuTfIrGYZ8r0vykpM579lQ8cuTvD9DbsurklyR
# Yej4miRXttauq6orM/w884OttafPbfuiDAW+7pLkLzMEH3/UWnvNiMd5+yS/m6H0+TfNjuE9GZ5J
# 9buzdX4wyVMy/NrjDknem+QFrbVFP98EztB7vzI7vtfOtn2fDEHWX2f4+fqrT54nNVv3XP1KVd0/
# Q02gD2b4ldXXJ3nqqV9gsSMCHACgO6aoAIDuCHAAgO4IcACA7ghwAIDubLOSsezlCbqh/MVAEvuk
# 1fJVRuEimyB9DXMW9jVGcACA7ghwAIDuCHAAgO5sLQfn9PwofVp13tt1MR1yIhjTsr5DTg6nGcEB
# ALojwAEAuiPAAQC6s7UcHPOf07DqvPhprhNgkWU5NZsup39GcACA7ghwAIDuCHAAgO6og8NKls1j
# bzrP7brph5wHVrHte19OzvQYwQEAuiPAAQC6I8ABALqjDg4rWXWefIw6OK4l6MuifmHs+3zZ9uTk
# 9M8IDgDQHQEOANAdAQ4A0B11cLhZq9a9WTXnZp3rxLV1HOQ0cOI89+yqz5ba9fs5PkZwAIDuCHAA
# gO4IcACA7tQW5xlNYHZg03yXTXN01n0PB2FXyVIugAOzTj7Mqvfxpjkzq7ZRP3PQFvY1RnAAgO4I
# cACA7ghwAIDuCHAAgO4o9MeNrFrYb5ltFP5b9SF67IekzOkY457bd6G/ZSQdHx8jOABAdwQ4AEB3
# BDgAQHe2loNjfvI4rTpPveq89DZybrb9fuDGNs1HWeee3LQQ39htlJNz+IzgAADdEeAAAN0R4AAA
# 3VEHZ+LGzpnZdPl55rHHfsge2yEnoR+b1qDpoQ373j+rM4IDAHRHgAMAdEeAAwB0p7Y4T2gC8ghs
# mo+yj3nmsXNozJVvza6SnXyAI1v1uU6b1qg5xDaMvf912sC5LexrjOAAAN0R4AAA3RHgAADdUQdn
# YsZ+Xstp2/jct93m01y745BvcDy2fc2fJx9m323YxX2vVs5uGcEBALojwAEAuiPAAQC6s7UcHHOL
# h2nVeeZNnx01xnUwdptP23WOD+zbtnNB1tnevtuwj/3LydkuIzgAQHcEOABAdwQ4AEB31MHp3Kr5
# Javm3Ow6p2edNizb5rZzfKZKPsHhWHbNblojZhe5JPtuwxj73/cxTI0RHACgOwIcAKA7AhwAoDu1
# xTk+k4cHYNN8kW3n6GzjeTCrXtOb5h+YJz/TrpKVfACnrHpNb/ueWece2XQfUzhGvmphX2MEBwDo
# jgAHAOiOAAcA6I46OJ0Z+7lKh5Bzs+m886rz2Luuq9Mr+QK7s+k1t2ke2qbbH2Mfm7bhGI5RTs5q
# jOAAAN0R4AAA3RHgAADdUQenM5vmwGy6fNX9LVt/kW3X1tl1zk/H1MHZEteYc5A4B3PUwQEApkGA
# AwB0R4ADAHRHHZwjt2rdm2Wfy6bL9/Ecp23vc9fb68WE8wFGt+p92eO5dw6cg1UZwQEAuiPAAQC6
# I8ABALqztRycqc/97crYOTOb2sZznHb97Khd5zW5V5h3nntg0/pVx2DsGl3OwXGeg00YwQEAuiPA
# AQC6I8ABALqjDs4ROc/86djPUdp0f2PM+R5aHtEu2tPD/TO1+f517eKzPoZcjG2fB+fgOM7BmIzg
# AADdEeAAAN0R4AAA3VEH54isMz+7ab7IpjVolq2/jbyibR/zqsbI2XE/9WMXeRBj134a2zr1rlZ1
# 6OdgF204hnOwTUZwAIDuCHAAgO4IcACA7ghwAIDuKPR3wNZJPl01oXXsz2nsB1Ge5z1jPxxz2f6W
# 2XZ71n3PrvWWsLiuVe+BRedt022M0YZNnOd63fYx7PscjNGGfb//2BjBAQC6I8ABALojwAEAulNb
# nGM77sm7AzBGnsWmOTrLjJ2fMsY+VjX2OTqGz21HdpUodFAHv2oexBj3xKb37dhtXCcXZOx9bPr+
# sbe/i30c2jnYoYV9jREcAKA7AhwAoDsCHACgO+rgHJBtPARy7HySsdu4i4dvrtqGsfd3CJ/bPhzw
# fP2oNj3Xh1AHZ5ltb3+MfTgH+z8Hh8YIDgDQHQEOANAdAQ4A0B11cA7IOnkX+6jlcHNW3f86c8Kb
# bmPTc7TpOV8n52LX9TFG0mUdnEM4t4fQhn1zDvZ/DsaoZzQSdXAAgGkQ4AAA3RHgAADdUQdnj1at
# KXOec7rqeR+7zs2qdRpW3f4Y2xj72tz0mNdpz65zq9bRS07EprVHemnDvjkH+z8H6/x/0D4/ByM4
# AEB3BDgAQHcEOABAd7aWg9Pj/OfYxsjNGDv3YuzcjF1cB/t4VtSY7z+Pbef5uF9vsIs6R6vsfx9t
# OAT7/hwOwb7PwTp1zA7pczCCAwB0R4ADAHRHgAMAdEcdnB3atMbMeYxd12ZsYzx7atV97Pv969j3
# 57aLYzgU2+6rtvE8trHbcAj2/Tkcgn2fg96uRSM4AEB3BDgAQHcEOABAd9TB2aFNnxO1yNjPXVp1
# /U33P8azpw59+Tr3wrY/t9P2nfOzS9vOAVh1e9s4t6vel4eQi7frz2Hf52AXbZj6tWgEBwDojgAH
# AOiOAAcA6E5ta96xqvqZtF/Tps8NWba9dd9zSO8/j0OYKx/TeY5nG9fKKm1atr1z5oftqhjWzR7s
# pnllY+elrePYj2GM+lfHfg7GaMO+j+EQPsczLNyoERwAoDsCHACgOwIcAKA7W8vByZJ58SkYuzbJ
# GHVxTtv1c5vGyDPax/NTNrGL9m5aa2JLOT97ycHZ9FiX2fX2d7GPfW9/G/vY9P0+x8P4HM95DHJw
# AIBpEOAAAN0R4AAA3dnas6gOPS9iG8Z+ns82nkW163nuZdbJT9lF7Z0xHWJ79/F8rW3ZtK/Zdo7X
# LnLIHINzcAjb38U+Vsn7MYIDAHRHgAMAdEeAAwB0Z5t1cAAA9sIIDgDQHQEOANAdAQ4A0B0BDgDQ
# HQEOANAdAQ4A0B0BDgDQHQEOANAdAQ4A0B0BDgDQHQEOANAdAQ4A0B0BDgDQHQEOANAdAQ4A0B0B
# DgDQHQEOANAdAQ4A0B0BDgDQHQEOANCd/w+3IKkehjb4lQAAAABJRU5ErkJggg==
# " />

# These patterns didn't passed unnoticed to Stephen Wolfram (of
# Mathematica© fame). He created an interesting taxonomy for cellular
# automata rules

#$
fig, ax = plt.subplots(ncols=4, figsize=(10, 10))

CAutomaton(63, 3, 'random').iterate_and_plot(rule_id=250, niter=100, ax=ax[0])
CAutomaton(63, 3, 'random').iterate_and_plot(rule_id=1, niter=100, ax=ax[1])
CAutomaton(63, 3, 'random').iterate_and_plot(rule_id=30, niter=100, ax=ax[2])
CAutomaton(63, 3, 'random').iterate_and_plot(rule_id=126, niter=100, ax=ax[3])

fig.tight_layout()
plt.show()

# <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAsgAAAEYCAYAAABBfQDEAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
# AAALEgAACxIB0t1+/AAAIABJREFUeJzt3XvsPc9d1/HX9kdpS6FY2gIKWJAGihIKqFACbS0EtcFE
# kWC8gtSEyEUqQRC0UCxCtApRSKSABpVyqZeYAJaoMWiJUFFEuQgUaEVu1iIUsUBL2/GPPYfOb7s7
# 5/1+z8zu7Pk+H8kvv/ac2Zk5e+bsbz/vfc/MlFISAAAAgNkjju4AAAAAMBJukAEAAIAMN8gAAABA
# hhtkAAAAIMMNMgAAAJDhBhkAAADIcIMMAAAAZN7u6A4cZZqmfyTpgyQ9TdKvSfoPkt4s6TGSHi3p
# v0j66pTSDwbr/0ZJHyvpiZLeJ6X0Uy36faPND5P0lzV/hveU9L2Sviil9HOLcj8m6YWS/p2k10v6
# PZfjPjOl9GNZufeX9GWSfkpSunyWz00p/e/enwVt3eN4z9p+B0mvSCl90F5toq97HK/TND1d0qdq
# /jyPkfQOkr4spfQDi3Jcd0/mHsdr1nbx+mq977iUfT9JL9B8jt5w+fcXp5T+X6fu10kpPbD/SHpf
# SW+R9KLF64+Q9Hc0f4HPqqj/b0v6qZ0+y4dK+leSHnf5/4+V9O8lvUbSkxdl37L45w2SPm1R5p0l
# /YykP5m99gWSflDSI4/+7vgnNEbuZrxnbf5eSf9J0puPPr/80/y7vZvxKulDJH2bpLfPXvt7kn5Z
# 0tOy17junvSfexqvWZvF66vzvuN3av6j7+mX//9ukl4t6QVHf3db/zzoKRbPvPz7X+cvppTeIunF
# kh4p6XkV9T9L82DZw5dovsn9v5KUUnq95r4/SdLfWJT9n5K+VtK/kPQiSR+UUvrqRZnP0/yE4Vuy
# 114s6f0l/bnmvcce7ma8T9P01Gmavl3Sp0t60x5tYnd3M14lfZKkj5P0R7LXXibpnSQ9N3uN6+55
# 3c14dVxfTfcd0zS9neb7jS9PKb3i8vLba76h/sX2n6CNB/0G+VmSfl3Sd628996Xf/9SpOJpmh4n
# 6YO13wX4WZK+c5qmJ11fSCn9V80Rio9ZlH11SunPp5Q+IaX0+SlLq8h8oqT/ePlxX+v7JUk/enkP
# 53M34z2l9KMppT+UUvoUST8madqjXezqbsar5kfsvyzp/2SvvePl36/PXuO6e153M14d11frfccn
# aT4H/zAr99MppXdNKX1V4+4386DfID9T0nenlN6w8t5nSnqdpL8ZrPsZkh7SfhfgV0l6V815bbk3
# aM4NMpum6Z0kPUVzpHnp5yX97kgHcbh7Gu+4f3czXlNK35BSenxK6d9mL3+o5ujcN0tcd+/A3YxX
# B+t9x5+Q9OPXSPNZPMiT9N5T8180X7t4/UmSvlTzI4JnpJReeXn9fSX9xcsxL0kpvTQ75rMkPSel
# 9JysqmdL+rmU0k+stP3Bkj5N81+Tj9SceP8ZqS5R/emS3jFlEzmmafptmgfvdy7KPmqapudLeoKk
# 39CcO/X5KaUfv7z/5Mu/1wbz6yU9bpqmR6aUfqOiv9jRHY533LF7H6/TNL2P5qjap6e3TtziuntS
# 9z5eC27ed0zTNEn6KEmvmKbpGZJ+v+anJ+8t6a9dIs5DemBvkDU/GpCk3zFN0ws0n4uP1PwX/HNT
# Sp96LThN0yMk/SXNfwV+pqS/IumlWV2fLOmHFvX/Pq38tTdN05/V/MN4Tkrp5y+vfa6kj5b0rdEP
# k1L6VUm/unj5szRPGviri9efJOnrU0o/e2n/T0n6rmmanpZSeo2kx13KvXGlqevjwN8i6bXR/mJ3
# dzXecffucrxO0/Rxkj5c0h/WPHHrH2Rvc909r7scr7cY7zueIOlRmiflfUBK6Qsv/XyWpJdP0/T0
# lNJ/793XkKNnCR71j+a/9F4v6aHstUdrXvrspYuyHyPp4y//+zsk/ZPsvXfSHIV9bvbaO19e+9RF
# PR+h+eL3EdlrHybp2yU9sfHne4qkX5H0QkPZR1zOxd+9/P8P1zzAv2il7Ldc3nv3o79D/nGNh7sd
# 75rz2t5y9Dnmn3b/3PN4vdT7kKR/I+l7JD3h8hrX3ZP+c8/j1XN91cp9h+Yb47dovpF+1KL8T0v6
# tqO/v61/HuQI8jMl/eeU0puvL6SUfn2apn8q6aumafqClNKrLm/9iKTXTtP0HprXIvyErJ6P1Nvm
# Bm3lC32x5hmbHz9N0x+9lPkRSX88tX189yhJ3yTpa1JKX3SrfErpLdM0/YLmqMbzVI5QPFbz2py/
# 0qKv2M3djnfcpbserymlN0/T9MJLH16seQIe193zuuvxalG477iuUvET6W3zs39W0seOmjr0QN4g
# T9P0bpLeT/OyI0u//fLvJ2pOQFe6LHg9TdMf03yBellW/pmac4N+Mnvt2ZL+V3r4phuP1PyX49el
# lD6v0Ud5G5d8n6+X9LKU0hevvP9ySUopPXPx1kOS3uXyv1+j+WL8+JUmHivpdWlezgUncM/jHffn
# HsfrNE1P1bwGcr4pyH+7/PvjL5sxcN09oXscr16l+46U0m9M0/Rara/g8QbNedPvonn8D+VBXcXi
# enP4PSvvPVvzRWpt16I/IOk7F3/pPFPSy6XfnHghzflC19eeenntCZrPdz7we/gSST+cD9Jpmv5M
# 9v6HaL7YLj1R8yLeulyEv19v/XHnniJp2KR6rLrn8Y77c1fj9bJE1/dL+r6sD9K805o0L6H1ENfd
# 07qr8Rp0677jFZrnPi09SvNN8pB59Q/qDfKzNA/atQH9gZd/v0aSpml6r8tfR5L0XprXBNTlvcdo
# Xnrnuu7h50zT9Fg9fL3C68Lgv6B5dvIjlw1O0/QB0zRVLwI/TdOnaN7x5ksXb31U9r+/Q/Njnfy4
# D9G8aPdLspf/peacuLzc+2reSvKf1fYVu7rL8b6QGteH49zbeH2j5id0r9LDo2gfcPn396aUrqkT
# XHfP597G65rN66vxvuObJT15mqZHZ8dNkp4q6VtTtu73SB7UG+Rna96yce2vlmuekKZpekjzMiTX
# wfHjmv9yu3q+5jSV/zFN0wdqzv95hObB9JPTNH24Lj+alNKbJH2NpD+YNzZN08dontH6DTUfaJqm
# j5b0tzTPon1J9s+3aE78v3qRpK+5/Bivg/SzJX335b2rr5b02Gma/nT22l+Q9MOSvq6mr9jd3Y33
# hUfPVU+u9b4xrLsarymlX9d8bf7KlNLrsreep/kR+6dlr3HdPZ+7Gq8rNq+vjvuOl2pOKfqM7LVP
# 1Bw9PjxFZMv01u/qvk3zeoTfKOm3Svpdmv+qf4Wkf56ynVymeU3Br9T86OKNkr7imvtzeeTxYs27
# Gk2aL1jP0fwI5CclfU5K6Y3TNH2O5mVWXplS+uys7oc0LxT+HpJ+RnPU9vtSSv+4wef7Rc2zXSe9
# 9a+96//+6ymlF2RlP0rzUiy/pnlpoR+Q9KUppTcu6nya5jUcX6l5sD9e0vPSZXk4jOsBGO9P0vwf
# gfe4fL6keZeyH5L091NK31TbBvZz7+P1Uv8na36s/iZJ7655vH5hWqxty3V3fPc+Xq3XV+d9x+Ml
# fYXmFM9rWsnzU0qvru1vLw/MDTIAAABg8aCmWAAAAACruEEGAAAAMtwgAwAAAJndNwqZpilJ0lru
# 81tXP5nlZa7vXV9blt16b9nOsp5S+2t1lnK2S8evlfHUbWmvdL6s/V2qPd+Wdtf6XeqL5kkAR0vS
# dn8Dn+ltypbO/VY93u9pbZxs/dZKvxnv2CspjQ/P8db+brVb4j2na22klI4ex6sn1jtOlmXXynuP
# t/TJ8t5WW2t923rNU3fr6721H6X/Pm61a70u3ah7yDGc81w/8/Ke62+pzug13VK3l+e+wPvfsMj1
# c61dS/no2N2wWRkRZAAAACDDDTIAAACQOWKZt+Kj6c2DAo+b18pHH3G0elzieHS1WUfkkbv1cUmE
# 9ZFGq3YHeKwnsXObmfc3G63rhEtWHjqOl+lu3hQzTyqLJ5XnVp8sPKkStalHvftkOb5UxpJi4Xnk
# fpYUC0sKT21agKXdFnVu1V3bJ+99gTc9x9qP3n260TdSLAAAAACLIybpdT+uVLa2/dpI7F7RilYT
# DTxt7dXeCO7987VwHQstoyTRiU0jOjrivdV+7ffVQ+252usJWvQ4S4SvVbtr9vzvRU/R//Zbop7W
# yZit6izVvfZe5CmEdxKop07vhFxPn/Iy0botvx8iyAAAAECGG2QAAAAgs3uKxdm1fPTUc5LKso29
# nPXRnNfRj8fPxDt5IjrJI5rS8aDaOpfRyWc9eR+NtpwY6mmr5QSlW8f0mNTofW8U3hSH5XHec2k5
# z960TEuaiyfVoNTGWn2lFIdleUu7LdJdIn2y/gZKk4yviCADAAAAGSLIA9hjKTa0xfdzG5P0yo6O
# zLWOoHZe2jHUXssdwyJ9i07eutWOp08WPSa278ETkfUedxX9nbScCLfVt1t17tG31teRHpP0Su2V
# EEEGAAAAMkSQBzLyX+p4uKOjf2dCDvKYLDl4W8fkajcPiPLmSnr61KO/rTZZsERER8wj78G7lFrN
# 8dHIZDSn1tuWpZ89c5BrI+2t+uRd+q6ECDIAAACQ4QYZAAAAyJBiAQSQDnMbk/TKRnmsHXk0e6t8
# 7aNNi9pJa0dPTCv1qZSO0SOVxfOY3LvkXk/RSZGl9AnLsmXR5fiifbLUuXzP+5k8fbO2e6tstE/W
# 5e1qf8dEkAEAAIAMEWQg4OjIyZkwSW9MW1GZUuTJu+nBrTZrtJq0dtR46TGRrvZpwB5L9vVQG0Vs
# GbWsnTi4LGv9PVraOHpS4959qkUEGQAAAMgQQQYCRo6mjIIc5LKjI92e89RqSbS1PM7o99VqeTlv
# Tm2r8RX9XXgj5lvnaY8NS/bS48mE5xyUlj2Lbq7hyfu91cet6O5eOdslkT61WGbOchwRZAAAACBD
# BBkIGDGKMipykMfWatZ59Hvz9MNbhzcf0lO+tr/eVRFaRcyP2tilp9abVazVZc1BtpTpOc5qI8+t
# cratavu7LFN7HcoRQQYAAAAy3CADAAAAGVIsgICzTAQ7EpP0ykZ5jN16UlGprpaPPz11eNMJLOVr
# +2uZ6OSdHOmZRFWqy5r+cfQYXn4XLSdc9kxBiSz3dqvd1ilAVpbl3baOyfU4p7XXNCLIAAAAQIYI
# MhBwdOTkTJikN6bIhK7oBhJ7TQyL1NFq0lsLtVsYe+ru1c6e9pwI13JpsVbtWr+31tfEVufdelxt
# X6LtEUEGAAAAMkSQgYCRoyqjIAe57OhItycatTxmjffzRPNeS1rnQVryGa05jxZ75L32qPsorbd1
# Xquz5xKHte3memymUdNuNO/fEvnukcO8hggyAAAAkOEGGQAAAMiQYgEEnPWR5BGYpHcu3qXFrrxp
# BT2W2IpMKvQuiWbph6eMtXzPZbSidY/2W2uxRKFnyb3apcWi7XqOXyu/x0Q46/mytOuZlNhyTBJB
# BgAAADLT3n8BTtM01p+cOJ2U0uGzsBjHt0WvLbUL3p9okt7RHX3YiY0uG+aJ2rWIPrbaxMO60cat
# 9ltEoLfqbLHByVZUvVHdQ4zh2u+7VG6v64ml3Zab+dw6plUba6y//Uh0OtDOZoeJIAMAAAAZIsg4
# nQGiFtIi+oZte0QUPHUM5NBxvHUtjkbs1yKirTYI6ZFT6x2XluhbbY5nq6XvLH1rVPdQYzi6kY1F
# j+tLj+h0z818PG20jNjXLp9447sjggwAAABYcIMMAAAAZEixwOmMkGLBOL6NSXplR4/j6xj2PNbf
# Krcsu/U435uW4Jl0tlX+Vhlvek/to+itftSIpEhY248+nt6D5zrcclLoHjvStajzVhstJmoeIZqS
# t3GNIsUCAAAAsGCjECDghBPCDsNGIWPzLL5fG/nqsTlItHztZDVLW9ENJLxqz51nwuNIG4V4Jnh6
# +91jU4rWdVrHkmWDjuX3O+KEaMt3Gb3GrCGCDAAAAGSIIAMBo+RijSwa0S3ljbVaqH4EZ4i+WY6P
# bo7h4f1OI/nCt8p5Nj+JLiHXM3pY6lv0fB3Nm78eOc4SkW2x4UZtnZb3StHWyOe+1c9Wejx5soxx
# IsgAAABAhhtkAAAAIEOKBRBw9OPxM2GS3pg8j/Vb7YbYYqJU7aSz6HuWJeQ875XaiD6y75Hucobf
# U3S5Msv58paxfBeeOlsuUdhqkt6tfrYS+bxraSPR1CEiyAAAAECGjUJwOkdvsCAxji3YKKRsgHGc
# pHYTltbKeTYTsba7x4Qyz5Js0fa9G6t4vos9ItCX44YYw2taPfWw6LEkWuC7uHl87UYha2qv17fq
# W9NiE5OsDjYKAQAAACzIQQYCzpCXNwpykM/Bk59YKuN9b+8NQqJqz8Ge/bDkxLbMnR5FjyXVou21
# 2qDE+tupzaf29HuvTVS22m2xtJuln0SQAQAAgAwRZCDgLHmuR2KjkLKjo3S1uYOttnitXcx/rfzR
# eZB7j1PP541GoEfUcxWKaJ2tNigp9S26ukup7tabj1jPaaRd7yYm0d8aEWQAAAAgww0yAAAAkGGZ
# N5zOAEsLSYXlhfBwLZdbOnqCVGOHjuPrtbi0tFhW1lW357uo3RCh9Ei1ZXrPVpkS77J4yzLe5e08
# S+Z5H4FvHHf0tbjJjz66JFqPJShrlxHsuQFPtE/LNqLt16YlbbTBMm8AAACABZP0gICzTAQ7EpP0
# yo6OeG+133LzgNoJeKVop2fyVY+NM2rHYili7lXb3z02XxlRdGLaskx0fK2Vq/0Oo0+CWn6WW33z
# tl87oTi65B4RZAAAACBDBBkIODr6dyZsFDImzxJKa8dYciWjebMelg0vWiyVZckTXr5nrdtTxsIb
# PbzHTUNKaiOSy3q8Tzgiy6bl/7t1G3l5y5yAteNqc7YtUea1umuXkGOjEAAAAMCIG2QAAAAgQ4oF
# EPCgTGKpwSS9sqMfXVsm6ZUe5dZOYGs1Iazl0k+RR9beiXiWc1p7bqKP1711Hc2znJ/1M7beSc87
# sdWbYuBpp0cbkTqjSzquHdNq+cM1RJABAACADBFkIODo6N+ZMElvTJFoZXSZt5Z1tzpu7zpr2/P0
# qfY3dDa1EyZLEUlPPWvlvRNboxt27L1M2lLr5d7W6ow+6Yg+BSGCDAAAAGSIIAMBI+fljYIc5LJR
# o3Utl3mrrbt2yafaHN7a78javic/2dvuVp2lSGN0DOxt+dm857tVmdo89lt1eurp2YZ3ebituqzt
# RpaibIkIMgAAAJDhBhkAAADIkGIBBBz9aPFMmKQ3Jssyb6VjIhN2euzmZumTd0yUduCzqN2lL9Km
# ty3vRKkRU5da7YhX237tZLtSnbVLolnayOtqlb5hLeNZns0y8bElIsgAAABAhggyEDBiNGU0TNIr
# OzrS3TraWlt3y2WaWk3WW6vD8xlabkLiabf2fLUqu7e9IouW79k70dMyBkrvHbXBSYRlIt6t95Zl
# ov+dKR1HBBkAAADIEEEGAkaOooyGHOSxlaKtlkisJ684mnvo1WMzjGV/o/2vzRvtcd68G22MIrLh
# R1SLTSrOsFFIzzzfnr/12uXx1hBBBgAAADJEkIGAkaMqoyAHuWyUSHc0Mtb6u1jL44y2YYki9Vid
# wbMSQMvztxXdttZp6fco4zXXM0e11EZtlNdSfu+NQlqNWW+fInXvtQILEWQAAAAgww0yAAAAkCHF
# AggY8XHjqJikN7Y9JnbtNXnMM5FuTeuxYx3LPSdvbZ0D70TCHhOsannSVHosiRZNZbG0u/dGIaU6
# I0vX9ajbs5nIWnnv+SKCDAAAAGSIIAMBZ5kIdiQm6ZWNEn2rjQpZovreSUFbx5fKWLVcBuoW64Sh
# rXa952vtuK33ek7OHEE0AmyJOnqivNF2PfVt1XmrrtIGJ9Z6PJvyROuuHavRpwhEkAEAAIAMEWQg
# 4CxRlBGQgzym5bmM5vvWqo0Ae6O+e0ZHe2wY0uMpSm1+8yiiea/eOnu2u8dGIaXXvePL8vTDozaH
# 2LqsnuXJGRFkAAAAIMMNMgAAAJAhxQIIOMtEsCMxSa/s6MfTW+1bH//W7vjlKWMtbzmnnl32rO3e
# qu/We57vosfyX62+y73Vjq8ev8FoGkXtcmeW9yx11qZatVxWb2uSXYs0MMvYIYIMAAAAZKa9oxjT
# NI2V1Y/TSSmNEMpgHBt5J+lF6zo6Ihtw6Di+XotLSyl5IjDeiGZ0eTlPBNizBJRVaZJgZOm8tfLR
# 72LteM8mJIHo9NHX4tCPvjbifqu+rTojUfgWTwq2jtv7qUCrcxJtd+N72uwAEWQAAAAgQw4yEDBi
# Pt5oyEEuGzXiXcoz9kY2PQv9W6NLniixpY/ecp7xFd1QYe2YyOculWu5wcpRok8hSu9Fl1nzvOfp
# b7Tf3r71/H5bL2/Xst0SIsgAAABAhhtkAAAAIEOKBRAw4uPGUbGT3n2KTPSp/W6j9Zcm0q2Vs6R7
# eJeU6/l4ObJjX4vl9Ub5rbVamuxWXVt1eifLtRpn1l3jLGPAO7H0Fu/ExVbttxynRJABAACADBFk
# IOAsE8GOxCS9sqOjb63bjy7X5o3wWSLAnr55l57yLInWoj0LzyTIaITt6PFqUTtxca2MZ6JpXt7S
# lnejk+hvJvJZot93j8/bql3vRkdEkAEAAIAMEWQg4AzRlFGQgzy2VhF3S6TLGsltlddsqa9HbnDv
# XOsWx3mXkGudo9rCUUuTWaK1ayL9tdbtjc5u9Wftc0d+Yy0i0K3ywaPLvRFBBgAAADJEkIGAs+S5
# Hokc5LKjI3GtIj6W46Nb20bzmtfe89RZqjsSqbO2X7sZSDRyXWLJBz9Kj6j21u8iGiWOrhTRc9UQ
# b0TVu0rI8vVWT3m8+eBL3qdURJABAACADDfIAAAAQIYUCyDg6EeLZ8IkvTF5lqOy6Jk+UXo0anls
# 6l3eKbpcm+W9lsvDLd/zni+LM6Qs7b00WXSS3rKMd8m/1p8zusHJmmhqSe0kO891hEl6AAAAQAUi
# yEDAGaIqR2OSXtnRke7Iphol0e85uoFF9L2t9tf6EI0y94gS147rnhMlj7L8TC0mhnm2ZS71ydKu
# t57lcd4IcOn16ARXT3S21QTXltHpEiLIAAAAQIYIMhAwclRlNOQgj82yjJc38lO73Frtck6totP3
# sIlIbX2lc3n0by2ar9t67OyVb1uqL/Kbi+ZOrzlq05ZlGUs9kq2/RJABAACADDfIAAAAQIYUCyDg
# LBPBjsQkvbKjH09HJm1ZJ8Z5llurbder1WS16HJx0cfU0ZQBS9+iqSijiKYqRI/bc0Ka9fijUiSi
# Ewc9dV/V1m1NhbkiggwAAABkiCADAWeIqoyCSXrn0CM6b6nT267n+61dWs1SV8tIrGWCWKsoYO3T
# gJH0iBIfdR2xRGRbRfq9EdVS+5F69qo7er6IIAMAAAAZIshAwBmiKkcjB7lstEh37cYZljpLEVFr
# u5HcX2vZ1rm41n63inR7xv49bhiS23szjlqWJxSW43tGgD1Lx3mf+vSouzYaTQQZAAAAyHCDDAAA
# AGRIsQACRn7cOBom6Y3Jk4Zg2UUtultdiXfZs63PFJ2MVZva4S3Tapm3VpMjre0frcckvWXZHp+7
# 5bJ6kcl9tefGWi6aXhSpu+U5JYIMAAAAZKa9/xqcpmm8Pz9xKimlw2dhMY5va7XMT4slfUZ09Di+
# jmFPlNV6bj3lW23ckddRim5bIt9rZT3RaU/fvH3xlolE0R1RuKHG8OK9m8e3mjzmdcSkTK+eG360
# bM9zDjaeCG1WQAQZAAAAyJCDDASMmIc3KnKQz8V6/lptShEtH81drN0cwpurvdV+7XJ60XHujbb2
# yO1srcdSbntsWNGyb62+i+gybVv15Fotq+f9/N686isiyAAAAECGHGScztG5mxLj2IIc5LIBxvHD
# TmwpKhON0NWUtZbvkStZmxftjTButVuKMpfatb63VdbSx+vLNyvta7PDra4DtWNw7+tRz1zevfOi
# PfMF1o4xfk/kIAMAAAAW3CADAAAAGSbpAQGjTE45AybpjS2yYUjp+FL5Vqkaefkek4lK7UXrjjwu
# jvYjukGLJbWj9nz31HPjDWu7R01q7DnZrdUmJBZ5PZFULesEXUv/iCADAAAAGSbp4XQGmNzEODZg
# kl7ZAOM4SfUT036zsp2jy6XjWkXPostJrZWNnAvrhKPId+ate8SNQrQYw8WCzgmTnuNabHITEX36
# MeLEwejv0dPWRhtM0gMAAAAsyEEGAkbLvRsZOchjar39a4/84rWyniXNvLmSnpznaK6p91zU1u0R
# WObtUJGNN9bKRTcFqd2wouWSbKXP5MnlbWWt/eiGLEve7zkaMSeCDAAAAGS4QQYAAAAyTNLD6Qww
# uYlxbMAkvbKjx/F1DLeemGats1R3JNXBerylXU+qQctHuq12ZNtxYtnRPzbzJD1zhY2X42u5jGCr
# cdVzCbqeyxfWfs/spAcAAABUIIKM0zk68nbBODbquQRTpI6BDBFBLilFayOT3Won61mP63H81uct
# RZCjTz9qN5vwTkirWIZrqDHcctLbUo9rVI+lBi39KNn7yZ9noqW37q3jF3UQQQYAAAAsWOYNCDhL
# nuuRosuulaIFe+Sp7eXoiHer9j3LjkVzka2R69bHW/t5q/1bx3kimN7ca0s0P7os3mi8Wwl7IrjR
# qLxlubVbdW2VabH03PI479OPrf7WLqtnbTP6u7J8TiLIAAAAQIYbZAAAACDDJD2cztETQy4Yx0ZM
# 0tt09Di+ecKiu86ZGg+mX0SWWfMeb+lTqZ+l1A7PBLzoEnI9lkbcOF9DjWFresFRaVijLaUWXYKu
# dmnH0nEW1pQWYxtM0gMAAAAsmKQHBJxlItiRmKRXdnTEe2uSijcC02NprT0mEK456glFZIMR6+Sk
# rXI9N4vYW3TS1x6fd22S3lFLqUWXoKudXGipu/baXjshbw0RZAAAACBDBBkIOGuk5QjenMnosj3R
# iPWDyhK1tJSpjQBZlneLPhWI5hCX6qpdrq22H2ttlc6TJ/fZu3zY0VpFVHtcM3r+Ztbeq80Tbh1p
# j0age26YoapsAAANhklEQVQU4l0GkAgyAAAAkOEGGQAAAMiQYgEEjPi4cTRM0isbLRXE0p/oxDDv
# skzRPtSUzfvSKmUhqnYHwJbfZaTuo7TYva3Vd1eqr3Z3vrUyI0+ki+zkZ22DnfQAAACAnbBRCE5n
# gMXpJTYKMWOjkE2HjuOta7F1M5BWS5O1nPxm2SikVKdlo45SPdGJj55Jct7z3nkJuaOvxTc3Clk9
# qHJpw6URnlq12nAj2lb0Oh+ZgMdGIQAAAMAByEEGAkaIGIyOHOSyoyPerXN5eyxZVRvZ80R0rf3z
# RGR7bKJS207LJeRG0TNf1/tkY8/f9Yh5wtaca0vfonnkW++xUQgAAABQgQgyEHB09O9M2ChkTFtR
# FcvKDWvlamfkl6y12zIPslXfSv3pGXn2nJM9zt9eohHFSLQ0+qShh2j7rY6LRom90e2tutgoBAAA
# ADgAN8gAAABAhmXecDoDLC3EODZoNUGpdpLfqI4ex5YxbEkf8DzKjaZKWB9vr5XfOsY7gc/TvuX4
# 2kfZa+WiG0HcKpuXX7w3xBhuOTGt1fdbKhMVHR9LtZ+7tu4Wyy6W6iqVXzmeZd4AAAAACyLIOJ2j
# I28XjGMjNgrZNHz0Lbo5xVWD6M7NPnnr9mwG0nLCkUdtdNsbIaz43EOM4auWkdEWG9d46tyjrZGW
# JmyNjUIAAACAzogg43RGiCAzjm8jB7ns6HG8FX2z5rh6IqjR6I434tUqR/NWO3k90XxKi2h0u6Q2
# urw8NNSJRjzX4ehTqtpNa0Y4zlJP9LrbM+c60n7JxhwIIsgAAACABTfIAAAAQIYUC5zO0Y+mLxjH
# RkzS2zTE4+naSWuex7WlneW8qRJrPJMK90jdsS5rV9uW57PUTvxbfIdHX4tvfvDo8mGuTuy83FrL
# pdQsIudr750EKybtkmIBAAAAWLzd0R0AzugsE8GOdP2LvjZSlx/fc2mtvR0d8bZEWS3Rxp5Rfcvk
# wL2Xi6v9TLUbhXjr9NR9lt/OVXRZu1Zj9lpPNCrf47hlWWvdpeMjSwR6J/RaWL5T65MoyzkkggwA
# AABkiCADAUdH/87EG+Gr3QCC7yamVbQ31yMiGYmMWaOJnqXuapfq8kbnLZFzTxTtnvL5e0RLW0Xj
# 94ouWyzrji5RaI0uL8v0XPrTct681yMiyAAAAECGG2QAAAAgQ4oFEHC2ySxHYJJe2WiPsb2PQZfn
# ea9H9pEUnGj7lrZa7KRXO64tx3vat6adHM3y/dRO5Gs1mbXUt+hxtctjWr/TVikse/S75bWGCDIA
# AACQYaMQnM4Ai9NLbBRixkYhm44ex0m6uRHEww6ILnsWXYLJM2mu1CfrklOeKKl3spvndxDdCKFH
# tPfG5MQhxvBVq40wbtXV6knW3pt59FxuLbr5SutrjPc4FcYwEWQAAAAgQw4yEDBiPt5oyEEuOzri
# 3WqzgWiO57IeK0subW1uaY+c5Ujd3qh6bXsWPTaAqFUbdfQuuecZ8z2Xcjt6uTXrez2XifNuHuJB
# BBkAAADIkIOM0yEH+VzIQd509DhePWHeCGHPXMtotDS6mYfneG/UcatMqU5rBLln/umNiOihY9hy
# P1Eb5e2pZd8iv9Xodbflk7w9rzEbbZGDDAAAAFhwgwwAAABkSLHA6YyQYsE4vq3TI1338aMaYByb
# l8iqeHwZqrt0fKtHydGl46Kf27MMVqm/e6edbNVzeW2IFIueKRI97pF6XqNaTZbtuUybNUVkj1SY
# 0hgmggwAAABkiCDjdI6OWlwwjo2YpLdpiOjbUnTThNJkN0vdLTZr2GqvNlpbes/yuW+JRJf3jqqv
# lTn6WhydpGesu0k9vevcqntNzyjx0SrOJRFkAAAAwIKNQoCAEf+CHg0bhZQdHfHear9HlN6zgYe1
# 3Wg/PdGwBvmNpnJb7XiP7xFVP8PvybIZR+13Ed0gxTq+Ir8tby5vj808jr6O1X7PpfJEkAEAAIAM
# N8gAAABAhhQLIODox0pn4p08UrtcGN+NjWXZsBsTtDaPs2j1mNqbfrHn4+La3e6s5zs6GdHynqfM
# USxjsOV3Ed1psbbOUt2W91qlUUT73Uo0bcV7rSKCDAAAAGSIIAMBZ5i4cjQm6ZWNGpGLTtCKfs8t
# o3B79MnS7lr73qXbPHVb3rNE3Ur9sE4I21P0KYQ34nyrjPV7jta5dbx3QlqP6PKyTM8xEY3Kr7H0
# kwgyAAAAkCGCDAQcHTk5E3KQx+Q5Tz0i96UtkEuRskgUzDumekTxPOX3zENt0ZeR9Yx8lyKztRuU
# HJVXvcYzHntEknvmXLPMGwAAAGDEDTIAAACQIcUCCDjLRLAjMUmvbJRH160mI/X4PK0monmXS7tV
# 3616Siznsuf59qSP3Cp/NO9nsRznafdq7Xuq3cHPe62rnXgYTUfw/Oa89jgnJUSQAQAAgAwRZCBg
# xGjKqJikNyZPdMbyXssF+i3HtZqIFp0A2KOM53hvhG4rSm3txxkiyWtKn2WPzTmivwtv1DbyvYwQ
# gfa0scc5yRFBBgAAADJEkIGAs+S5Hokc5LJRInGWXNponu1WW1Z75dla2vVspuHdcMNzvOW4Unv3
# 9Bu6skSJS2qXS7PWHYnAthgDpT5ttW8VOc/RCHDLc8IybwAAAIATEWQgYJTo3xmQg3wuLc7fVh0t
# VnywlLe0Fx1nnnoi5SLHWyLOpY1ZrnpuqtFTq00ubtW1LOMdQ5GNOrxjf4+VPaLjJBoBjrQVaW+J
# CDIAAACQ4QYZAAAAyEx7Pz6Zpmn85zUYWkrp8BkkjOPb9lwcvnT8qI4ex9cx7Nk4Y6OezfeidZcm
# q7WaRNXysfzyuB51l1jSJzx1ry19t/FdHP1j2/yglutIq7FjXSqwJDKuW7W1VlePCa6lMhbRc3Kj
# vc0PRQQZAAAAyBBBxukMELWQCpELPFw06uCt6wyTiRaOHscPO2Fr0cdWy4dZ6o5GZEvlayNlPY/v
# EWnznEPvb+4MEeSWT49qo7V7L6e3Z3vR6LK1rlZ1G9siggwAAABYsMwbEHCWPNcjsVFI2dERb895
# 8uYZeyO/W3V631uK5kfvcXz0nFrq8i4J1yq39Sh7b3xh+S72WE5vbZm4PXKAeyyrt3e/LXURQQYA
# AAAy3CADAAAAGVIsgICjH4+fCTvpjclznnruArcmuuNX7SPZvT+nR49Jjcu614z8e9pzZ7hSWkA0
# lWatXG0aWaudAEt1ln57tTv5WfrRYlK3pS4iyAAAAECGZd5wOgMsLcQ4NmCjkLKjx/Fyo5Ds9c1j
# vBOOPE8PvBNoPJPcvNGsPTYa8dZd+p4873nKbPUlO+7oH1vzjUKqO9Txunf0hhutsFEIAAAAcEJE
# kHE6A0QtJDYKMWOjkE1Hj+Mk+c5pNLrcKg90rVzLbZWXx/XYKKSkVHdtRM8S1bfkNy8MMYavem5W
# URJdtu0sG4W0urYefZ7YKAQAAACowA0yAAAAkCHFAqczQooF4/g2JumVHT2Ol2O4diJbbTrDWrlW
# O/jVpmFY27eUt/ShZdpGpJ7SOV0cd/SPbTNNqGVaj+d4S309dtLztLfHublVl6XunSYlkmIBAAAA
# WBBBxukcHXm7YBwbMUlv0xARZE+0dnG8q3xNG7XRTkuU+VY7nvZL5Vpt9NHyyYqnTyNFkC33E9Hl
# 3VpF/L2OnrTWauxFo9sWLf57kdVFBBkAAACwYKtpIOAsea5Huv6V33Kpq72XTupp1Ih3i2ixJ1pq
# acMaAY5YW0otOs4sn/tWHyyvL+uujXZ62h2J5XNHx67nu2zxZGur3VI7tTm5tedmrVzP8xRtP3qe
# iCADAAAAGSLIQMBZIiwj8Oa0VWx7e/N43NYyF7l0fKt88h7fd48oXmRcWyPnkfzm0ndxlqcwS968
# V8vnrF0ho0e0da1M5KlH7bkplesZObe+tyzjvVYQQQYAAAAy3CADAAAAGVIsgICzPoLcE5P0ykZN
# BalNcWnRnudxa4/vu/VGJda6In1sVS7ajxH0nkC3rKdHOkDtEoORPvX4PR89kS/apzVEkAEAAIAM
# EWQg4KyRliMwSe9coptqRJdi2zuaFNUzyuvdEGX5/6OR69p+HP1bi06YtEwM22rD+p73aVftEoOt
# +1Q7AbBnn1psFGKpiwgyAAAAkCGCDAScJc/1SOQglx0dfYtsTmFdpi1ap0dt9K+2vdpluGqXayup
# zQePPg3Y27JvLfJetz7v3suWtVxicLQ+tcydZqMQAAAAYCfcIAMAAAAZUiyAgKMfj58Jk/TGFFn6
# aU2rCTzRiTctH4+X9ExJ8aRNeHfC26o7mjIx0u+r1cSwtUf+pfp6Llvm2clu5D71XALP8n1Z+1RC
# BBkAAADIEEEGAkacsDIaJumVjRKJq+2HJaLp/d5aTbxpOcGsZ8Q9MgGwZd2jjMWo6MQwT121x6/V
# 1WOZuFH61GKJxj36xDJvAAAAgNF09r8cAQAAgJaIIAMAAAAZbpABAACADDfIAAAAQIYbZAAAACDD
# DTIAAACQ4QYZAAAAyHCDDAAAAGS4QQYAAAAy3CADAAAAGW6QAQAAgAw3yAAAAECGG2QAAAAgww0y
# AAAAkOEGGQAAAMhwgwwAAABkuEEGAAAAMtwgAwAAABlukAEAAIAMN8gAAABAhhtkAAAAIPP/ARM9
# iI0N7Qb+AAAAAElFTkSuQmCC
# " />

# <ul>
#     <li><p><strong>Class 1</strong> rules normally converge to
#         uniform states when subject to random initial conditions,
#         like rule 250 above;</p>
#     </li>
#     <li><p><strong>Class 2</strong> rules never really converge,
#         but get stuck in simple periodic patterns, like rule 1
#         above;</p>
#     </li>
#     <li><p><strong>Class 3</strong> rules are completely aperiodic
#         and chaotic. Looking from a distance they usually look like
#         white noise, like rule 30 above;</p>
#     </li>
#     <li><p><strong>Class 4</strong> rules are also aperiodic, but
#         unlike class 3 rules they show some sort of organized
#         structure even when looking at a distance, like rule 126.
#         These are the most interesting rules, as they lie somewhere
#         between order and chaos, which Wolfram referred as
#         "interesting complexity".</p>
#     </li>
# </ul>

# You can take a look at all the 256 existing rules with \(k=3\) <a
# href="http://plato.stanford.edu/entries/cellular-automata/supplement.html">here</a>,
# see if you can tell to which class each rule belongs.

# I totally encourage you to play with this simple code. Try seeing what
# happens when you use \(k=5\) or \(k=7\), but keep in mind that the number of
# available rules grows with \(2^{2^k}\) (with \(k=9\) you have more possible
# rules than atoms in the universe :O), and most of them look like they belong
# to class 3. It's also very simple to generalize this code to cellular
# automata with more than two states, you just have to remember to codify the
# rules in base \(N_{states}\) instead of base 2. You might also wanna try
# extending it to more then one dimension. <a
# href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's game of
# life</a> is probably the most famous cellular automata, and it's a
# 2-dimensional one.

# If you're interested to know more about cellular automata, <a
# href="http://plato.stanford.edu/entries/cellular-automata/">Stanford
# Encyclopedia of Philosophy</a> has an awesome article about it.
