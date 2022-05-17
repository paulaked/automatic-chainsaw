import json

car_data = {"name": "tesla", "engine": "electric"}

print(car_data)
print(car_data["name"])

car_data_json_string = json.dumps(car_data)

print(car_data_json_string)
