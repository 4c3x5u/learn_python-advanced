# strings and bytes aren't directly interchangable
# strings contain unicode, bytes are raw 8bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(f'b: {b}')

    s = 'This is a string!'
    print(f's: {s}')

    # try combining them
    # print(b+s)

    # decode b and then combine it with s
    s2 = b.decode('utf-8')
    print(s+s2)

    # decode s and then combine it with b
    b2 = s.encode('utf-8')
    print(b+b2)

    #encode the string using utf-32
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    main()
