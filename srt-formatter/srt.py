import pysrt, os
from tkinter import filedialog as fd
from sys import exit

def main():

    subFile = getFile()

    if subFile == "":
        exit()

    subs = pysrt.open(subFile)

    for count, sub in enumerate(subs):

        # strip off whitespace on both ends and replace double spaces with single space
        sub.text = sub.text.strip()
        sub.text = sub.text.replace("  ", " ")

        # if previous sub ends with period, capitalize the current sub
        if count == 0 or newSentence(subs[count-1].text):
            sub.text = f"{sub.text[0].upper()}{sub.text[1:]}"

        # if the first letter is not capitalized, prepend with dash and space
        if openStart(sub.text):
            sub.text = f"- {sub.text}"

        # if the last char is a letter, append with a space and a dash
        if openEnd(sub.text):
            sub.text = f"{sub.text} -"

        # if the sub ends with a comma, remove it and append with a space and a dash
        if (endsWithComma(sub.text)):
            sub.text = f"{sub.text[:len(sub.text) - 1]} -"

    # get the filename of the current file, add "-formatted" to it, and save it
    saveAndOpen(subFile, subs)
    exit()

def getFile():

    filetypes = (("subtitle files", "*.srt"),)
    subs = fd.askopenfilename(filetypes=filetypes)
    return subs

def openStart(txt):

    return txt[0].islower()

def openEnd(txt):

    return txt[-1].isalpha()

def endsWithComma(txt):

    return txt[-1] == ","

def newSentence(txt):

    return txt[-1] == "."

def saveAndOpen(subFile, subs):

    name, extension = os.path.splitext(subFile)
    newFile = f"{name}-formatted{extension}"
    subs.save(newFile)
    folderList = subFile.split("/")
    folder = "/".join(folderList[0:-1])
    os.startfile(folder)

if __name__ == "__main__":
    main()