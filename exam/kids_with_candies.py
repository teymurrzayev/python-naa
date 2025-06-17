def kids_with_candies(candies, extra_candies):
    max_candy = max(candies)
    return [c + extra_candies >= max_candy for c in candies]
