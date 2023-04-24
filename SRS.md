This our SRS file


## Robot To Cloud Computing

### Requirement overview

Client Specs
- Create a website that allows a robot to connect and upload data and also allows users to login and view said data.
- Create API keys to allow the robots to communicate with the server and verify that they are allowed to send data.
- *Stretch goal:* add the ability to send data to the server to be computed and then sent back to the robot for use 
(ie: take video feed, process it, and return objects of interest)

    Given the teams moderate knowledge of django, databases, web dev, and api functionality, this project should be 
feasible. The django framework will be the core of this project, with our main use case being the handling of 
registering robots in the database, and monitoring them as well. 

    For the success of this project the team will be split between back-end and front-end for at least the beginning of development.
Many individuals will have to spend some time reviewing Django and its syntax. When it comes to communication with the robot 
ROS may be used, which may also need to be researched. Planning and coordination between front-end and back-end teams will 
be essential to achieve the greatest functionality.

Functionality requirements:

| Priority | Feature              | Description                                                                                         |
|----------|----------------------|-----------------------------------------------------------------------------------------------------|
| 1        | API Key Distribution | Means for Robot to obtain API key, via some validated request                                       |
| 1        | Validation           | Only authorized robots are allowed to obtain API key, key needed to send data                       |
| 1        | Robot Monitoring     | Server is able to handle sent data and display relevant data on the user page                       |
| 1        | User login           | Server requires login to view data and access to future features                                    |
| 1        | Database             | Means of storing key Human user and robot data (Username, Password) (APIKey, Name, Classifications) |
| 2        | Computations         | Server returns requested computations to robot for its use. TBD what computations are needed        |
| 3        | Control              | For starters, a user may activate a robot remotely via server. Scope of this feature TBD            |

To build the MVP, 

| Enabled Feature | Development Tasks                                                                |
|-----------------|----------------------------------------------------------------------------------|
| Display Data    | A verified robot with key is able to send data, most recent data displayed in UI |

