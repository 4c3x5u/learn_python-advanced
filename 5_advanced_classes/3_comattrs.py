class MyColor:
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use __getattr__ to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return self.red, self.green, self.blue
        elif attr == "hexcolor":
            return f"#{self.red:02x}{self.green:02x}{self.blue:02x}"
        else:
            raise AttributeError

    # use __getattr__ to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # use __getattr__ to dynamically return a value
    def __dir__(self):
        return "red", "green", "blue", "rgbcolor", "hexcolor"


def main():
    my_color = MyColor()

    # print the value of a computed attribute
    print(my_color.rgbcolor)
    print(my_color.hexcolor)

    # set the value of a computed attribute
    my_color.rgbcolor = (125, 200, 86)
    print(my_color.rgbcolor)
    print(my_color.hexcolor)

    # access a regular attribute
    print(my_color.red)

    # list the available attributes
    print(dir(my_color))


if __name__ == "__main__":
    main()
