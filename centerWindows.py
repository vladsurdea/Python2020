
class CenterWindows():

    def __init__(self, roots):
        self.roots = roots

    # Brings all windows to center
    def windowsOnCenter(self):
        # Gets the requested values of the height and width.
        windowWidth = self.roots.winfo_reqwidth()
        windowHeight = self.roots.winfo_reqheight()
        # print("Width", windowWidth, "Height", windowHeight)

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.roots.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.roots.winfo_screenheight() / 2 - windowHeight / 2)

        # Positions the window in the center of the page.
        self.roots.geometry("+{}+{}".format(positionRight, positionDown))
        return self.roots
