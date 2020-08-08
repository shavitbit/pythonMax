from pathlib import Path

path = Path("c:\\temp")
print(path.exists())
print(path.absolute())

new_dir_name = "c:\\temp\\maxDevopsTeam"
new_dir = Path(new_dir_name)
print(new_dir.absolute())
print(new_dir.exists())
new_dir.mkdir()
print(new_dir.exists())

if new_dir.exists():
    print('delete folder ' + str(new_dir.absolute()))
    new_dir.rmdir()

# get-chilled-Item or get the files in directory
for file in path.glob('*'):  # or *.* for files only
    print(file)
