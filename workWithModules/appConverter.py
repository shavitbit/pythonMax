import workWithModules.converters
# i can import a function from module
from workWithModules.converters import kg_to_lbs

# ..and than use the imported function like that
kg_to_lbs(555)
# or with all the function in the module like that
mishkal = workWithModules.converters.kg_to_lbs(13)
mishkal1 = workWithModules.converters.lbs_to_kg(13)

print(mishkal)
print(mishkal1)