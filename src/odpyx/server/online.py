def onlineV1Ping():
    data = {
        "alertTime": 600,
        "interval": 3590,
        "message": "OK",
        "result": 0,
        "timeLeft": -1,
    }

    return data


def onlineV1LoginOut():
    data = {"error": "Not Found", "message": "Not Found", "statusCode": 404}

    return data
