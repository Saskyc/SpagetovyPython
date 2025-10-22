from Projekty.ConsoleChristmasGame import *

class Helper:

    '''Zdroj:
    https://stackoverflow.com/questions/5881873/python-find-all-classes-which-inherit-from-this-one'''
    def FindAllSubclasses(classType):
        import sys, inspect
        subclasses = []
        callers_module = sys._getframe(1).f_globals['__name__']
        classes = inspect.getmembers(sys.modules[callers_module], inspect.isclass)
        for name, obj in classes:
            if (obj is not classType) and (classType in inspect.getmro(obj)):
                subclasses.append((obj, name))
        return subclasses
