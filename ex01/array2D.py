def slice_me(family: list, start: int, end: int) -> list:
    ret = []
    try:
        assert family[start:end], "Error: cannot slice given list"
        ret = family[start:end]
        shape = (len(family), len(family[0]))
        nshape = (len(ret), len(ret[0]))
        print("My shape is: ", shape)
        print("My new shape is: ", nshape)
        print(ret)
    except AssertionError as e:
        print(f"AssertionError: {e}")
