


def count(x: str) -> dict[str, int]:
    """
    Counts how many times each of the letters A, C, G and T occur in a string

    >>> count('agtagtcg')
    {'A': 2, 'C': 1, 'G': 3, 'T': 2}
    """

    count = {"A":0, "C":0, "G":0, "T":0}

    for i in x: 
        i = i.upper()
        if i not in count:
            raise Exception()
        else: 
            count[i] = count[i] + 1

    return count

try:
    count("h")
    print("All is well")
except:
    print("Error")


#print(count('agtagtcgh'))



def raises_error(x):
    if x < 0:
        raise Exception("Negative", x)
    if x > 0:
        raise Exception("Positive", x)
    return 42
def f(x):
    return raises_error(x)
def g(x):
    try:
        print(f(x))
    except Exception as e:
        if e.args[0] == "Negative":
            print("g:", e.args[0])
            return f(0)
        else: raise


try:
    print(g(-1))
    print(g(1))
except Exception as e:
    print("Outer", e.args[0])