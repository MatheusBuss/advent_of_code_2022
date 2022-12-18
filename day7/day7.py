file = open('commands.txt', 'r')


class Directory():
    def __init__(self, name: str, parent) -> None:
        self.name = name
        self.parent = parent

    def set_children(self, children):
        self.children = children

    def update_child(self, target):
        for i in range(len(self.children)):
            if self.children[i] == target.name:
                self.children[i] = target
                break

    def get_child_by_name(self, target):
        for child in self.children:
            if child.name == target:
                return child

    def updir(self):
        return self.parent

    def set_size(self, size):
        self.size = size


class File():
    def __init__(self, name: str, parent: Directory, size: int) -> None:
        self.name = name
        self.parent = parent
        self.size = size


commands = [line.strip() for line in file]

root = '/'

fake_parent = Directory('fake_parent', None)

fake_parent.set_children([Directory(root, fake_parent)])

folders = {}

current_folder = fake_parent

i = 0

while i < len(commands):
    if commands[i] == '$ cd ..':
        current_folder = current_folder.updir()
    elif commands[i].startswith('$ cd'):
        name = commands[i].split()[-1]
        current_folder = current_folder.get_child_by_name(name)
        folders[name] = {'object': current_folder, 'size': None}
        contents = []
        i += 2
        while i < len(commands) and (not commands[i].startswith('$')):
            if commands[i].startswith('dir'):
                contents.append(
                    Directory(commands[i].split()[-1], current_folder))
            else:
                file_size, file_name = commands[i].split()
                contents.append(
                    File(file_name, current_folder, int(file_size)))
            i += 1
        i += -1
        current_folder.children = contents
        current_folder.parent.update_child(current_folder)
    i += 1

root_folder = folders['/']['object']


def calculate_sizes(folder: Directory) -> int:
    size = 0
    for child in folder.children:
        if isinstance(child, Directory):
            size += calculate_sizes(child)
        else:
            size += child.size
    folder.set_size(size)
    folders[folder.name]['size'] = size
    folders[folder.name]['object'] = folder
    return size


calculate_sizes(root_folder)


def calculate_specific_size(folder: Directory, threshold: int, total: int) -> int:
    if folder.size <= threshold:
        total += folder.size
    for child in folder.children:
        if isinstance(child, Directory):
            total = calculate_specific_size(child, threshold, total)
    return total


print(f'Specific size: {calculate_specific_size(root_folder, 100_000, 0)}')

total_size = 70_000_000
necessary = 30_000_000
occupied = root_folder.size

diff = total_size-occupied
missing = necessary-diff


def list_sizes(folder: Directory, cumulative: list) -> list:
    cumulative.append(folder.size)
    for child in folder.children:
        if isinstance(child, Directory):
            cumulative = list_sizes(child, cumulative)
    return cumulative


sizes = list_sizes(root_folder, [])

sizes.sort()

i = 0
while sizes[i] <= missing:
    i += 1

print(f'Smalles folder size: {sizes[i]}')
