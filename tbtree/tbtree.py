import os
import pathlib

pipe = "|"
elb = "|__"
fork = "|---"
pipe_pre = "|   "
space = "   "

class DirTree:
    #take root directory as argument, creates ._generator
    def __init__(self, root_dir):
        self._generator = _TreeGen(root_dir)
    #var tree holds results of build_tree, loop to print each result
    def generate(self):
        tree = self._generator.build_tree()
        for i in tree:
            print(i)

class _TreeGen:
    #takes root_dir as argument, ._tree is empty list
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []
    #returns tree diagram, head and body
    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree
    #adds name of root directory to top
    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree_append(PIPE)
    #takes directory path and generates tree
    def _tree_body(self, directory, prefix=""):
        #file and subdirectories to entries
        entries = directory.iterdir()
        #sorts directories first
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            #if entry is last in directory, use elb, else use fork
            connector = elb if index == entries_count - 1 else fork
            #if entry is directory call _add_directory, if not call _add_file_
            if entry.is_dir():
                self._add_directory(
                    entry, index, entries_count, prefix, connector)
            else:
                self._add_file(entry, prefix, connector)
        #appends directory entry to tree list
        def _add_directory(self, diretcory, index, entries_count, prefix, connector):
            #appends a new directory to ._tree
            self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
            #prefix determined by index value
            if index != entries_count - 1:
                prefix += pipe_pre
            else:
                prefix += space
            #call tree body with new arguments, append prefix for next directory
            self._tree_body(directory=directory, prefix=prefix)
            self._tree.append(prefix.rstrip())
        #appends file entry to tree list
        def _add_file(self, file, prefix, connetcor):
            self._tree.append(f"{prefix}{connector} {file.name}")
            
    

