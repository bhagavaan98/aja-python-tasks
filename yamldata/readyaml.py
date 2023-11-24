import yaml
with open("yamlemployye.yaml", 'r') as file:
    data = yaml.safe_load(file)
name = data["name"]
id = data["id"]
salary = data["salary"]
print(name,id,salary)