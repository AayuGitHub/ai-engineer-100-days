config = {
    "model": "small",
    "temperature": 0.2
}

settings = config

settings["temperature"] = 0.9
print(config["temperature"])
print(settings is config)

settings = {
    "model": "large"
}

print(config)

x = [10, 20]
y = x

x += [30]
print(y)
# print(x)