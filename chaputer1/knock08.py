def cipher(target):
    result = ''
    for c in target:
        if c.islower():  # islowerは小文字か判定
            result += chr(219 - ord(c))
        else:
            result += c
    return result
# ord:アスキーコードを所得
# chr:アスキーコードから文字へ

if __name__ == '__main__':
    target = "I am an NLPer."
    # 暗号化
    result = cipher(target)
    print('暗号化:' + result)

    # 復号化
    result2 = cipher(result)
    print('復号化:' + result2)

