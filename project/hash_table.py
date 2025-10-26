from collections.abc import MutableMapping

class HashTable(MutableMapping):
    def __init__(self, dict_data=None):
        self.dict_data = dict_data
        self.hesh_table = self.make_hesh_table(self.dict_data)
    
    @staticmethod
    def hesh_function(key):
        data = str(key).encode('utf-8')
        my_hash = hash(data)
        id = abs(my_hash) % 1000
        return id

    @staticmethod
    def make_hesh_table(dict_data):
        hesh_table = {}
        for key in dict_data:
            k = HashTable.hesh_function(key)
            if k in hesh_table:
                if isinstance(hesh_table[k], list):
                    hesh_table[k].append((key, dict_data[key]))
                else:
                    hesh_table[k] = [hesh_table[k], (key, dict_data[key])]
            else:
                hesh_table[k] = (key, dict_data[key])
        return hesh_table
    
    def __getitem__(self, key):
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

    def __setitem__(self, key, value):
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

    def __delitem__(self, key):
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
    
    def __iter__(self):
        for bucket in self.hesh_table.values():
            if isinstance(bucket, list):
                for k, v in bucket:
                    yield k
            else:
                k, v = bucket
                yield k

    def __len__(self):
        lens = 0
        for data2 in self.hesh_table.values():
            if isinstance(data2, list):
                lens += len(data2)
            else:
                lens += 1
        return lens
    
    def __contains__(self, key):
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