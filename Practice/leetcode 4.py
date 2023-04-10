def longestCommonPrefix( strs):
    longest_prefix = ''

    for first_chr in zip(*strs):
        print("zip",first_chr)
        if len(set(first_chr)) == 1:
            print("set",first_chr)
            longest_prefix += first_chr[0]
        else:
            break

    return longest_prefix

str= ('flow','flash')
longestCommonPrefix(str)
