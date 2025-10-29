import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from task5.main import HashTable

class HashTableDemo:
    """
    Class for demonstrating hash table functionality with detailed output.
    """
    
    def __init__(self) -> None:
        """
        Initializes hash table demonstration object.

        Initializes:
            ht : HashTable (Hash table for demonstration with initial size 4)
        """
        self.ht = HashTable(initial_size=4, load_factor=0.75)
    
    def print_state(self, title: str = "") -> None:
        """
        Prints current hash table state.

        Parameters:
            title : str (Optional title for state output)

        Prints:
            Table size, capacity, load factor, internal structure,
            keys, values and key-value pairs.
        """
        if title:
            print("\n{title}")
        
        print("Size: {len(self.ht)}")
        print("Capacity: {self.ht.capacity}")
        print("Load factor: {self.ht.load_factor:.2f}")
        
        print("Internal structure:")
        for i, bucket in enumerate(self.ht._buckets):
            if bucket:
                items_str = " -> ".join(["'{k}':{v}" for k, v in bucket])
                print("  Bucket [{i}]: {items_str}")
            else:
                print("  Bucket [{i}]: empty")
        
        print("Keys: {list(self.ht.keys())}")
        print("Values: {list(self.ht.values())}")
        print("Key-value pairs: {dict(self.ht.items())}")
    
    def demo_basic_operations(self) -> None:
        """
        Demonstrates basic hash table operations.

        Operations:
            - Element addition
            - Value updates
            - Value retrieval
            - get method usage with default values
        """
        print("Basic operations")
        
        print("1. Element addition:")
        self.ht["apple"] = 10
        self.print_state("After adding 'apple': 10")
        
        self.ht["banana"] = 20
        self.print_state("After adding 'banana': 20")
        
        self.ht["orange"] = 30
        self.print_state("After adding 'orange': 30")
        
        print("\n2. Value update:")
        self.ht["apple"] = 100
        self.print_state("After updating 'apple': 100")
        
        print("\n3. Value retrieval:")
        print("ht['apple'] = {self.ht['apple']}")
        print("ht['banana'] = {self.ht['banana']}")
        print("ht.get('orange') = {self.ht.get('orange')}")
        print("ht.get('missing', 'default') = {self.ht.get('missing', 'default')}")
    
    def demo_collisions(self) -> None:
        """
        Demonstrates collision handling in hash table.

        Creates:
            Small table (3 buckets) to force collisions
        
        Shows:
            - Key distribution across buckets
            - Chain formation during collisions
            - Element search in chains
        """
        print("\nCollisions")
        
        self.ht.clear()
        self.ht = HashTable(initial_size=3, load_factor=1.0)
        
        print("Created table with 3 buckets for collision demonstration")
        
        test_items = [
            ("cat", 1), ("dog", 2), ("bird", 3),
            ("fish", 4), ("frog", 5), ("snake", 6)
        ]
        
        for key, value in test_items:
            hash_val = hash(key)
            bucket_idx = hash_val % 3
            print("Key '{key}' -> hash: {hash_val} -> bucket: {bucket_idx}")
            self.ht[key] = value
        
        self.print_state("After adding elements with collisions")
        
        print("\nChain search:")
        for key in ["cat", "fish"]:
            if key in self.ht:
                print("Key '{key}' found: {self.ht[key]}")
    
    def demo_resize(self) -> None:
        """
        Demonstrates automatic hash table resizing.

        Process:
            - Creates table with small initial size
            - Adds elements until load factor threshold
            - Shows moment of capacity increase
        """
        print("\nAutomatic resizing")
        
        self.ht = HashTable(initial_size=4, load_factor=0.75)
        print("Created table with 4 buckets, load_factor=0.75")
        
        items_to_add = [
            ("one", 1), ("two", 2), ("three", 3),
            ("four", 4), ("five", 5), ("six", 6)
        ]
        
        for i, (key, value) in enumerate(items_to_add, 1):
            print("\n{i}. Adding '{key}': {value}")
            old_capacity = self.ht.capacity
            self.ht[key] = value
            
            if self.ht.capacity > old_capacity:
                print("RESIZE OCCURRED: {old_capacity} -> {self.ht.capacity}")
            
            self.print_state("After adding '{key}'")
    
    def demo_deletion(self) -> None:
        """
        Demonstrates element deletion operations.

        Operations:
            - Existing element deletion
            - Element deletion from chains
            - Attempt to delete non-existent elements
        """
        print("\nElement deletion")
        
        self.ht = HashTable(initial_size=4, load_factor=0.75)
        test_data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        
        for k, v in test_data.items():
            self.ht[k] = v
        
        self.print_state("Initial state before deletion")
        
        print("\n1. Existing element deletion:")
        del self.ht["b"]
        self.print_state("After deleting 'b'")
        
        print("\n2. Element deletion from chain:")
        for i, bucket in enumerate(self.ht._buckets):
            if len(bucket) > 1:
                key_to_delete = bucket[0][0]
                print("Deleting '{key_to_delete}' from chain in bucket {i}")
                del self.ht[key_to_delete]
                self.print_state("After deleting '{key_to_delete}'")
                break
        
        print("\n3. Attempt to delete non-existent element:")
        try:
            del self.ht["missing"]
        except KeyError as e:
            print("Error: {e}")
    
    def demo_advanced_methods(self) -> None:
        """
        Demonstrates advanced hash table methods.

        Methods:
            - setdefault: default value setting
            - pop: deletion with value return
            - popitem: arbitrary element deletion
            - update: bulk element update
        """
        print("\nAdvanced methods")
        
        self.ht.clear()
        
        print("1. setdefault method:")
        result1 = self.ht.setdefault("python", "awesome")
        print("ht.setdefault('python', 'awesome') = '{result1}'")
        
        result2 = self.ht.setdefault("python", "changed")
        print("ht.setdefault('python', 'changed') = '{result2}'")
        
        print("\n2. pop method:")
        self.ht["java"] = "enterprise"
        popped = self.ht.pop("java")
        print("ht.pop('java') = '{popped}'")
        
        default_pop = self.ht.pop("missing", "default_value")
        print("ht.pop('missing', 'default_value') = '{default_pop}'")
        
        print("\n3. popitem method:")
        self.ht["javascript"] = "web"
        self.ht["go"] = "concurrent"
        item = self.ht.popitem()
        print("ht.popitem() = {item}")
        
        self.print_state("After popitem()")
        
        print("\n4. update method:")
        self.ht.update({"rust": "safe", "kotlin": "android"})
        self.ht.update([("swift", "ios"), ("dart", "flutter")])
        self.ht.update(scala="jvm", elixir="functional")
        
        self.print_state("After update()")
    
    def demo_iteration(self) -> None:
        """
        Demonstrates various hash table iteration methods.

        Iteration methods:
            - Direct key iteration
            - Value iteration
            - Key-value pair iteration
            - Key membership checking
        """
        print("\nHash table iteration")
        
        self.ht.clear()
        self.ht.update({"x": 10, "y": 20, "z": 30})
        
        print("Initial table:", dict(self.ht.items()))
        
        print("\n1. Key iteration:")
        for key in self.ht:
            print("Key: {key}")
        
        print("\n2. Value iteration:")
        for value in self.ht.values():
            print("Value: {value}")
        
        print("\n3. Key-value pair iteration:")
        for key, value in self.ht.items():
            print("Pair: {key} -> {value}")
        
        print("\n4. Membership checking:")
        print("'x' in ht: {'x' in self.ht}")
        print("'w' in ht: {'w' in self.ht}")
    
    def demo_error_handling(self) -> None:
        """
        Demonstrates error handling and exceptional situations.

        Error cases:
            - Access to non-existent key
            - Deletion of non-existent key
            - popitem from empty table
            - Incorrect table initialization
        """
        print("\nError handling")
        
        self.ht.clear()
        
        print("1. Access to non-existent key:")
        try:
            value = self.ht["ghost"]
        except KeyError as e:
            print("KeyError: {e}")
        
        print("\n2. Deletion of non-existent key:")
        try:
            del self.ht["phantom"]
        except KeyError as e:
            print("KeyError: {e}")
        
        print("\n3. popitem from empty table:")
        empty_ht = HashTable()
        try:
            empty_ht.popitem()
        except KeyError as e:
            print("KeyError: {e}")
        
        print("\n4. Incorrect initialization:")
        try:
            bad_ht = HashTable(initial_size=0)
        except ValueError as e:
            print("ValueError: {e}")
        
        try:
            bad_ht = HashTable(load_factor=2.0)
        except ValueError as e:
            print("ValueError: {e}")
    
    def run_all_demos(self) -> None:
        """
        Runs complete demonstration of all hash table functions.

        Demonstration sequence:
            - Basic operations
            - Collision handling
            - Resizing
            - Element deletion
            - Advanced methods
            - Iteration
            - Error handling
        """
        print("Hash table demonstration")
        
        self.demo_basic_operations()
        self.demo_collisions()
        self.demo_resize()
        self.demo_deletion()
        self.demo_advanced_methods()
        self.demo_iteration()
        self.demo_error_handling()
        
        print("\nDemonstration completed")


if __name__ == "__main__":
    """
    Main entry point for hash table demonstration execution.

    Creates:
        demo : HashTableDemo (Demonstration object)
    
    Executes:
        run_all_demos : method (Runs complete demonstration)
    """
    demo = HashTableDemo()
    demo.run_all_demos()