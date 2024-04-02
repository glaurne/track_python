

import yaml

track_yaml = """
Blue cones:
- - -36.1
- 14.2
- - -38.7
- 18.6
- - -36.5
- 21.3
- - -38.1
- 24.5
- - -36.0
- 29.0
- - -38.7
- 34.2
- - -36.2
- 39.0
- - -39.2
- 8.6

Orange cones:
- - 0
- 0

Yellow cones:
- - -3.3
- 31.0
- - -15.6
- -3.4
- - -29.1
- 26.1
- - -37.3
- 12.0
- - -37.3
- 16.1
- - -37.3
- 20.3
- - -37.3
- 22.7
- - -37.2
- 26.9
- - -37.2
- 31.7
- - -37.6
- 36.5
"""

points = yaml.safe_load(track_yaml)

with open('track.yaml', 'w') as file:
    yaml.dump(points, file)

print(open('track.yaml').read())