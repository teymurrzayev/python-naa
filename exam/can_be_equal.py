def can_be_equal(target: list[int], arr: list[int]) -> bool:
    if sorted(target)!=sorted(arr):
        return False
    if target == arr:
        return True
    return True