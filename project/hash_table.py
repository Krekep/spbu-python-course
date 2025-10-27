from collections.abc import MutableMapping
from typing import Any, Dict, Iterator, List, Tuple, Union, Optional

class HashTable(MutableMapping):
    def __init__(self, dict_data: [Dict[Any, Any]] = None) -> None:
        """
        Initialize the hash table.
        Args:
            dict_data: Dictionary with initial data to populate the table.
        """
        self.dict_data = dict_data
        self.hesh_table: Dict[int, Union[Tuple[Any, Any], List[Tuple[Any, Any]]]] = (
            self.make_hesh_table(self.dict_data)
        )
    
    @staticmethod
    def hesh_function(key: Any) -> int:
        """
        Static method to compute the hash of a key.
        Args:
            key: Key to be hashed.
        """
        data = str(key).encode('utf-8')
        my_hash = hash(data)
        id = abs(my_hash) % 1000
        return id

    @staticmethod
    def make_hesh_table(dict_data: Dict[Any, Any]) -> Dict[int, Union[Tuple[Any, Any], List[Tuple[Any, Any]]]]:
        """
        Create a hash table from a dictionary.
        Args:
            dict_data: Source dictionary to convert to hash table.
        """
        hesh_table: Dict[int, Union[Tuple[Any, Any], List[Tuple[Any, Any]]]] = {}
        for key in dict_data:
            k = HashTable.hesh_function(key)
            if k in hesh_table:
                k_value = hesh_table[k]
                if isinstance(hesh_table[k], list):
                    k_value.append((key, dict_data[key]))
                else:
                    hesh_table[k] = [k_value, (key, dict_data[key])]
            else:
                hesh_table[k] = (key, dict_data[key])
        return hesh_table
    
    def __getitem__(self, key: Any) -> Any:
        """
        Get the value associated with the key.
        Args:
            key: Key to look up.
        """
        hesh_k = self.hesh_function(key)
        if hesh_k not in self.hesh_table:
            raise KeyError(f"Key not found")    
        data2 = self.hesh_table[hesh_k]
        
        if isinstance(data2, list):
            for k, v in data2:
                if k == key:
                    return v
        else:
            k, v = data2
            if k == key:
                return v
        raise KeyError(f"Key not found")

    def __setitem__(self, key: Any, value: Any) -> None:
        """
        Set the value for the key in the table.
        Args:
            key: Key to set.
            value: Value to associate with the key.
        """
        hesh_k = self.hesh_function(key)
        
        if hesh_k not in self.hesh_table:
            self.hesh_table[hesh_k] = (key, value)
            return
            
        data2 = self.hesh_table[hesh_k]
        
        if isinstance(data2, list):
            for i, (k, v) in enumerate(data2):
                if k == key:
                    data2[i] = (key, value)
                    return
            data2.append((key, value))
        else:
            k, v = data2
            if k == key:
                self.hesh_table[hesh_k] = (key, value)
            else:
                self.hesh_table[hesh_k] = [data2, (key, value)]

    def __delitem__(self, key: Any) -> None:
        """
        Delete the key-value pair from the table.
        Args:
            key: Key to delete.
        """
        hesh_k = self.hesh_function(key)
        if hesh_k not in self.hesh_table:
            raise KeyError(f"Key not found")
            
        data2 = self.hesh_table[hesh_k]
        
        if isinstance(data2, list):
            for i, (k, v) in enumerate(data2):
                if k == key:
                    del data2[i]
                    if len(data2) == 1:
                        self.hesh_table[hesh_k] = data2[0]
                    elif len(data2) == 0:
                        del self.hesh_table[hesh_k]
                    return
        else:
            k, v = data2
            if k == key:
                del self.hesh_table[hesh_k]
                return
                
        raise KeyError(f"Key not found")
    
    def __iter__(self) -> Iterator[Any]:
        """
        Iterate over all keys in the table.
        """
        for data2 in self.hesh_table.values():
            if isinstance(data2, list):
                for k, v in data2:
                    yield k
            else:
                k, v = data2
                yield k

    def __len__(self) -> int:
        """
        Get the number of key-value pairs in the table.
        """
        lens = 0
        for data2 in self.hesh_table.values():
            if isinstance(data2, list):
                lens += len(data2)
            else:
                lens += 1
        return lens
    
    def __contains__(self, key: Any) -> bool:
        """
        Check if the key exists in the table.
        Args:
            key: Key to check.
        """
        hesh_k = self.hesh_function(key)
        if hesh_k not in self.hesh_table:
            return False   
        data2 = self.hesh_table[hesh_k]
        
        if isinstance(data2, list):
            for k, v in data2:
                if k == key:
                    return True
        else:
            k, v = data2
            if k == key:
                return True       
        return False
