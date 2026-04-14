api_data = {                          
    "current_condition": [             
        {                             
            "temp_C": "18",
            "weatherDesc": [          
                {"value": "Sunny"}     
            ]
        }
    ],
    "area": [
        {"city": "Beijing"}
    ]
}
are=api_data["current_condition"][0]["temp_C"]
print(" number :",are)
name=api_data["area"][0]["city"]
weather=api_data["current_condition"][0]["weatherDesc"][0]["value"]
print("city name:",name)
print("weather name",weather)