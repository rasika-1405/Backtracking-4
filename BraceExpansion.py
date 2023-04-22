"""
Rasika Sasturkar
Time Complexity: O(k^(n/k)), k is avg. length of each block & n is length of string
Space Complexity: O(n)
"""


def expand(s: str):
    result = []
    # null case
    if s is None:
        return result

    blocks = []
    i = 0
    while i < len(s):
        block = []
        char = s[i]
        if char == "{":
            i += 1
            while s[i] != "}":
                if s[i] != ",":
                    block.append(s[i])
                i += 1
        else:
            block.append(char)
        i += 1
        block.sort()
        blocks.append(block)

    def backtrack(blocks, idx, s):
        # base case
        if idx == len(blocks):
            result.append(s)
            return

        # logic
        block = blocks[idx]
        for i in range(len(block)):
            char = block[i]
            s += char  # action
            backtrack(blocks, idx + 1, s)  # recurse
            s = s[:-1]  # backtrack

    backtrack(blocks, 0, "")
    return result


def main():
    """
    Main function - examples from LeetCode problem to show the working.
    This code ran successfully on LeetCode and passed all test cases.
    """
    print(expand(s="{a,b}c{d,e}f"))  # return ['acdf', 'acef', 'bcdf', 'bcef']
    print(expand(s="abcd"))  # return ['abcd']


if __name__ == "__main__":
    main()
