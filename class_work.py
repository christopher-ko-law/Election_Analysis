pet = [{"Name":"Spot",
        "Age": 4,
        "Hobbies":["Running","Fetch","Sleeping"],
        "Alarm":{"Saturday":"10am",
                "Sunday":"8am"}
        },
        {"Name":"SpotTwo",
        "Age": 7,
        "Hobbies":["Running","Fetch","Sleeping"],
        "Alarm":{"Saturday":"2am",
                "Sunday":"1am"}
        }
        ]

print(pet[1]["Name"] + " " + str(pet[1]["Age"]))

#print("Hobbies: " + str(len(pet["Hobbies"])))

#print("Spot wakes up on Saturday at " + pet["Alarm"]["Saturday"])