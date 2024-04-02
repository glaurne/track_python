import yaml

#initialize a dictionary with all the yaml entries
data2 = {
    'cones_left': [],
    'cones_orange': [],
    'cones_orange_big':[],
    'cones_right':[],
    'tk_device':[],
    'starting_pose_front_wing': [0.0, 0.0, 0.0],
    'lap_threshold':180
}

#this inserts an x and y value into the conesleft array! for blue
data2['cones_left'].append([1.7667433023452759, 1.4703056812286377])

#this inserts an x and y value into the cones right array!
data2['cones_right'].append([1.1,1.0])

#this file is the format we want!!!!! Look at the file
with open('output_with_false.yaml', 'w') as file:
    #by using default_flow_style = false, it puts in the correct, yaml format that we want!
    yaml.dump(data2, file, default_flow_style=False)


#if you look at this one, this is not the format we want, look at this file and you'll see 
with open('output_with_true.yaml', 'w') as file:
    #by using default_flow_style = false, it puts in the correct, yaml format that we want!
    yaml.dump(data2, file, default_flow_style=True)