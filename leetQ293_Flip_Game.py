
def flip_game(s):
    s = [c for c in s]
    for i in range(len(s)):
        if i+1 < len(s) and s[i] == '+' and s[i+1] == '+':
            s[i] = s[i+1] = '-'
            print ''.join(s)
            s[i] = s[i+1] = '+'

def possible_moves(s):
    for i in range(len(s)):
        if s[i:i+2] == '++':
            print s[:i] + '--' + s[i+2:]


if __name__ == '__main__':
    s = '+'
    possible_moves(s)
