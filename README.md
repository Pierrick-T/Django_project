# Django_project

## Objectives ##

So here is your objective: Could you please write a Django application that consists of

    - Two Django models. The first model is a "User" model with only a single "name" field (without any password) and a second model named "PhysicalPort" with a single field "location" ( CharField(max_length=30) ).

    - There should be a many-to-one relationship between the User and the PhysicalPort Model.

    - A simple Django view returning a PhysicalPort in plain text

    - The project should be tracked in git. Please commit often!
    
    - Optionally, you can create a Dockerfile for building a container image

To use: 
`localhost:8000/<physicalport_id>` to get the physical port
`localhost:8000/<physicalport_id>/users` to get the users