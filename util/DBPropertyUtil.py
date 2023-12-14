class DBPropertyUtil:
    @staticmethod
    def get_connection_properties(property_file_path='D:/Python/Challenge/util/property_file.txt'):
        global file
        try:
            file = open(property_file_path, 'r')
            properties = {}
            for line in file:
                key, value = line.strip().split('=')
                properties[key.strip()] = value.strip()
            return properties
        except Exception as e:
            print(f"Error reading property file: {e}")
            return None
        finally:
            if file:
                file.close()


