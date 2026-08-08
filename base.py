# base.py
# Base class that handles common CSV loading for all data classes

class BaseData:
    """
    Base class with common functionality for loading CSV data.
    All other classes (Match, Batsman, Bowler, etc.) inherit from this.
    """
    
    def __init__(self, filepath):
        """
        Initialize with filepath and load data
        """
        self.data = []
        self.load_data(filepath)
    
    def load_data(self, filepath ):
        """
        Read CSV file and populate self.data
        All values stored as strings
        """
        try:
            file = open(filepath, 'r')
            lines = file.readlines()
            file.close()
            
            header = lines[0].strip().split(',')
            
            for line in lines[1:]:
                values = line.strip().split(',')
                row_dict = {}
                for i in range(len(header)):
                    row_dict[header[i]] = values[i]
                self.data.append(row_dict)
                
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")