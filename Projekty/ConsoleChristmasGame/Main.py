from Projekty.ConsoleChristmasGame.Helper import Helper
from Projekty.ConsoleChristmasGame import Action



subClasses = Helper.FindAllSubclasses(type(Action.Action))

for subclass in subClasses:
    print(subclass)