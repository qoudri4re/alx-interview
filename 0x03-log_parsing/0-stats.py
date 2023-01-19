import re

metrics = {"totalFileSize": 0, "statusCodes":
           {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
           }
entries = 0
interrupt = False
while entries < 10 and not interrupt:
    try:
        entry = input()
        match = re.search(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>.*)\] ' +
                          '"(?P<method>\w+) (?P<path>.*) (?P<protocol>HTTP/\d\.\d)" (?P<status>\d+) (?P<size>\d+)', entry)

        if match:
            metrics["totalFileSize"] += int(match.group("size"))
            if int(match.group("status")) in metrics["statusCodes"]:
                metrics["statusCodes"][int(match.group("status"))] += 1
            entries += 1

    except (KeyboardInterrupt, EOFError):
        entries = 10
        interrupt = True
print("File size: ", metrics['totalFileSize'])
statusCodes = list(metrics["statusCodes"].keys())
statusCodes.sort()
for statusCode in statusCodes:
    if metrics["statusCodes"][statusCode]:
        print(statusCode, ": ", metrics["statusCodes"][statusCode])
