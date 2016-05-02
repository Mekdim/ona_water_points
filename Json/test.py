onaurl = raw_input("Insert the Json url \n")
def calculate(onaurl):
    
    import urllib2
    import json
    response = urllib2.urlopen(onaurl)

    data = json.load(response)
    is_found = False
    is_found_second = False
    count = 0
    for item in data:
        if (item['water_point_condition'] =='functioning'):
            count = count + 1;
    returned_dict = {}
    u = {}
    c = {}
    d  = {}
    for item in data:
        for x in c:
            if (item['communities_villages'] == x):
                c[item['communities_villages']] = c[x] + 1
                is_found = True
        if (is_found != True):
            c[item['communities_villages']] = 1
        is_found = False
    for item in data:
        for x in d:
            if (item['communities_villages'] == x):
                is_found_second = True
        if (is_found_second != True):
            if (item['water_point_condition'] != 'functioning'):
                d[item['communities_villages']] =  1
            else:
                d[item['communities_villages']] =  0
        if (is_found_second == True):
            if (item['water_point_condition'] != 'functioning'):
                d[item['communities_villages']] =  d[item['communities_villages']] + 1
            else:
                d[item['communities_villages']] =  d[item['communities_villages']]
        is_found_second = False
    for item in d:
        d[item] = (d[item] / float(c[item]))*100
    x = sorted(d.items(), key=lambda x: x[1], reverse=True)
    returned_dict["number_functional"] = count
    returned_dict["number_of_water_point_per-each_com"] = c
    returned_dict["community_ranking"] = x
    print returned_dict
calculate('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')