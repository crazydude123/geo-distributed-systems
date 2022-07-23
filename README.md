# geo-distributed-systems

VjDB - geo-distributed key-value store

Folder information

1. payload.txt contains the end-user payload
2. childA and childB contain their respective lookup tables in lookup_childA.txt and lookup_childB.txt
3. parent has the global state of the application in lookup_parent.txt


How to run?

1. Start the parent and children servers by ```python3 parent.py``` or ```python3 child.py```

The payload plays out to the system and latencies are recorded in results.txt

Graphing

normal.py and normal1.py are used to output all/most of the graphs
