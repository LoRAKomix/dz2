import yaml

def read_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = read_config("config.yaml")
    print(config)
