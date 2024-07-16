
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
    for b in bmi:
        try:
            if b > limit:
                ret.append(True)
            else:
                ret.append(False)
        except AssertionError as e:
            print(f"AssertionError: {e}")
    return ret
