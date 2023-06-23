# QuickPathStr

*Copyright (c) 2023 Sean Yeatts. All rights reserved.*

This module provides syntax for working with strings in the context of file
management. It's designed to reinforce a universal nomenclature by which files,
their types, and their directories may be referred.

## API Reference
The core of the API is captured within the ```Filepath``` class:

```python
class Filepath:
# Deconstructs a complete filepath into its constituent elements
    def __init__(self, complete: str) -> None:
        self.complete   = complete                          # Ex: C:\Users\myself\Desktop\MyFile.txt
        self.directory  = str(Path(self.complete).parent)   # Ex: C:\Users\myself\Desktop
        self.name       = str(Path(self.complete).name)     # Ex: MyFile.txt
        self.root       = str(Path(self.complete).stem)     # Ex: MyFile
        self.extension  = str(Path(self.complete).suffix)   # Ex: .txt
```
