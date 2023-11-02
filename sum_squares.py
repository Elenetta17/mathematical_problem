def func(n):
    """
    This function take as input a positive integer n
    and returns the sum of squares of numbers up to n (n included)
    
    NB: If I had translated the function of the exercise directly into code, 
    I would have written a nested loop, pretty inefficient. Thinking about what
    the function does, it is evident that the function is equivalent to sum the squares,
    and thus it can be translated in an algorithm with complexity O(n) instead of O(n^2)
    """
    if n < 0 or type(n) != int:
        raise ValueError("The input should be a positive integer")
        
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += i**2
    return sum_squares


