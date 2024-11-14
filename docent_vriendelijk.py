class Docent:
    def __init__(self):
        self.enabled = True

    def parseText(self, text: str):
        if self.enabled == False:
            return text
        text = text.replace("coke", "muesli")
        text = text.replace("bom", "mysterieus pakketje")
        return text