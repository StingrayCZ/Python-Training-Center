# 14th Lesson SDA (20.11.2021)

• funkce </p>
• malinko nakousneme i funkce vyssich radu </p>
• seznamy, iteratory, generatory </p>
• dekoratory </p>
• lambdy (viz bod 1) </p>
• planovac letu (mini Kiwi) </p>

## Kiw

```Py
def unique_flight_combinations(flights: t.Iterable[dict]) -> set[tuple[str, str]]:    
                                   
    #    result = []               
    #                              
    #    for flight in flights:    
    #        source_destination = (flight["source"], flight["destination"])    
    #        result.append(source_destination)    
    #                              
    #    return set(result)        
    
    # Alternativni implementace    
    result = set()    
    
    for flight in flights:    
        source_destination = (flight["source"], flight["destination"])    
        result.add(source_destination)    
    
    return result    
    
    
def unique_flight_combinations_bonus(flights: t.Iterable[dict]) -> set[str]:    
    result = set()    
    
    for flight in flights:    
        source_destination_str = f"{flight['source']}->{flight['destination']}"    
        result.add(source_destination_str)    
    
    return result    


def parse_flight_info(raw: dict) -> dict:
    return {
        "source": raw["source"],
        "destination": raw["destination"],
        "flight_number": raw["flight_number"],
        "price": int(raw["price"]),
        "bags_allowed": int(raw["bags_allowed"]),
        "bag_price": int(raw["bag_price"]),
        "departure": datetime.fromisoformat(raw["departure"]),
        "arrival": datetime.fromisoformat(raw["arrival"])
    }


def list_parsed_from_csv(parser_function, csv_file: str) -> list[dict]:           
    unparsed_records = list_from_csv(csv_file)                                                                             
                                                                                                               
    result = []                                                                                                            
    for record in unparsed_records:
        pprint(record)
        parsed = parser_function(record)
        pprint(parsed)
        print("\n\n")
        result.append(parsed)                                                                                                                
                                                                                                                          
    return result

parsed_records = list_parsed_from_csv(parse_flight_info, csv_file="flights.csv")

```
