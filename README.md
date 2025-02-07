# GridGame Backend Example

### About
This is a sample implementation of <i>Option 2</i> of the Cenith take-home GridGame assignment - which is to design a backend that could support the playing of the GridGame. 

### Details
In a 100 by 100 2-D grid world, you are given a starting point A on one side of the grid, and an ending point B on the other side of the grid. Your objective is to get from point A to point B.

Each grid space can be in a state of [“Blank”, “Speeder”, “Lava”, “Mud”]. You start out with 200 points of health and 450 moves. Below is a mapping of how much your health and moves are affected by landing on a grid space.

```
[jjj
“Blank”: {“Health”: 0, “Moves”: -1},
“Speeder”: {“Health”: -5, “Moves”: 0},
“Lava”: {“Health”: -50, “Moves”: -10},
“Mud”: {“Health”: -10, “Moves”: -5},
]
```

## Structure
- `openapi.yml` - The API of the backend. You would wire the client against this specification. 
- `GridGame/` - The source code of the backend application

## Running 

Initial Setup:
1. Create a virtual environment and enable it.  `python -m venv .venv` & `source ./venv/bin/activate`
2. Install requirements `pip install -r requirements.txt`

Running:

3. Start the server. 