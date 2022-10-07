"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('agtagtcg', 5)
    ['agtag', 'gtagt', 'tagtc', 'agtcg']

    """
    lst = []
    for i in range(len(x)):
        value = x[i:i+k:1]
        if len(value) == k: 
            lst.append(value)
    return lst

        

def unique_kmers(x: str, k: int) -> list[str]:
    """
    Computer all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']
    """
    lst = []
    for i in range(len(x)):
        value = x[i:i+k:1]
        if len(value) == k: 
            if value not in lst:
                lst.append(value)
    return lst




def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    FIXME: do you want more tests here?
    """
    value = kmer(x, k)
    count = {}

    for i in value: 
        if i not in count:
            count[i] = 0
        count[i] = count[i] + 1

    return count

print(count_kmers("agtagtcg", 3))