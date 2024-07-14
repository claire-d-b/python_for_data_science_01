
def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    i = 0
    j = len(height)
    ret = []
    try:
        assert j == len(weight), "Error: length of the lists differ"
        for w in weight:
            ret.append(w / (height[i] * height[i]))
            i += 1
    except AssertionError as e:
        print(f"AssertionError: {e}")
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret = []
    try:
        for b in bmi:
            assert b <= limit
            ret.append(True)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        ret.append(False)
    return ret
