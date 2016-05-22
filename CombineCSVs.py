import os
import Tkinter, tkFileDialog


root = Tkinter.Tk()
root.title("Combine CSVs")


def combineFiles():
    startString = "REF"
    opendir = tkFileDialog.askdirectory(parent=root, initialdir="/", title='Please select location of CSVs')
    savedir = tkFileDialog.askdirectory(parent=root, initialdir="/", title='Please select location where you want final CSV saved')
    dirFile = os.path.join(savedir, "combined.csv")
    newFile = open(dirFile, "w")

    newFile.write(startString + "," + "TYPE" +"," + "ADDR" + "\n")
    for filename in os.listdir(opendir):
        if filename.endswith(".csv"):
            pathName = os.path.join(opendir,filename)
            currentFile = open(pathName, "r")
            for line in currentFile:
                splitLine = line.split(",")
                if splitLine[0] != startString and splitLine[0] != "":
                # skip lines that start with REF
                    newFile.write(splitLine[0] + "," + splitLine[1] + "," + splitLine[2][:-1] + "," + filename + "\n")
            currentFile.close()
    newFile.close()
    raise SystemExit

runLabel = Tkinter.Label(root, text = "Click 'Run' to begin")
runLabel.grid(row=1, column=1, padx = 10, pady = 10)

runButton = Tkinter.Button(root, text = "Run", command = combineFiles)
runButton.grid(row=2, column=1, padx = 10, pady = 10)

root.mainloop()


