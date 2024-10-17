def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(a=1, b=2, c=3)