# Title
Hardware diagnose - Expert System

## Overview
This is a hardware fault diagnosis expert system, based on rule reasoning, the user by 
selecting the relevant symptoms of the hardware fault, the system will deduce the possible 
fault cause. The system uses Python's 'tkinter' library to provide a graphical interface, 
combined with a preset knowledge base and inference engine, to help users quickly diagnose 
hardware problems.

## Structure
ExpertSys/  
├── knowledge_base.json  
├── knowledge_base.py  
├── inference_engine.py  
├── main.py  
├── README.md            # Project desription file  
├── LICENSE              # License File

## Functions
1. **Conditional Selection**:   
The user checks the symptom conditions of the hardware failure, and the system infers the 
possible causes of the failure based on these conditions.
2. **Inference engine**:  
According to the preset rules, the system reasoning based on the conditions selected by the 
user gives the conclusion with the highest matching degree.
3. **Result**:  
The system presents the inference results to the user in a GUI interface.

## Dependencies
- Python 3.x
- Tkinter（Used for graphical interfaces）
- json（Used to load knowledge base files）

## Usages
### 1. Installing dependencies
1. **Ensure you have already installed Python 3.x，then directly run `main.py` for `tkinter` 
is a part of the library of Python and there's no need to install singly.**
2. **Download and clone the following repository**:  
   ```bash
   git clone git@github.com:RamessesN/ExpertSystem.git
   ```

### 2. Loading the knowledge base
Database file `knowledge_base.json` contains rules and conditions for hardware fault diagnosis.
For instance：
```json
{
  "conditions": [
    "The computer won't start",
    "The power indicator isn't working",
    "The power indicator is working",
    "No display after the computer is turned on",
    "The fan is working properly"
  ],
  "rules": [
    {
      "if": ["The computer won't start", "The power indicator isn't working"],
      "then": "Power Problem"
    },
    {
      "if": ["The power indicator is working", "No display after the computer is turned on"],
      "then": "Motherboard Problem"
    },
    {
      "if": ["No display after the computer is turned on", "The fan is working properly"],
      "then": "Graphics card problem"
    }
  ]
}
```

### 3. Running
Run main.py to start: ```python3 main.py```

### 4. User Interface
1. **After starting，Users are be allowed to select options in the interface like “The power 
indicator isn't working” or “The computer won't start”.**
2. **After clicking the "Reasoning" button, the system will reason and return a possible fault 
conclusion based on the selected conditions.**
3. **The results will be displayed at the bottom of the interface.**

## File Description
1. **knowledge_base.json**:  
This file contains all rules and conditions for hardware fault diagnosis. Rules define the type 
of faults that the system should derive when certain conditions are met.
2. **knowledge_base.py**:  
Responsible for loading the knowledge_base.json file and converting its contents into Python 
objects for use by the inference engine.
3. **inference_engine.py**:  
Contains the logic of the inference engine, reasoning according to the symptom conditions provided 
by the user, and returns the matching fault cause.
4. **main.py**:  
User interfaces are provided that allow users to select fault symptoms and view inference results. 
The tkinter library was used to implement the graphical interface.

## Development and Contribution
Contribute code or ask questions! If you have any suggestions or areas for improvement, please feel 
free to make them.

## License
This project is licensed under the MIT license and free use, modification, and distribution are 
welcome.