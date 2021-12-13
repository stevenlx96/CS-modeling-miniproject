##Use case
This design studio mainly helps the domain of any implement of Petri net.
The Petri net can be applied to varies induestries such as money deposite, product shipment and so on.

##Install:
-use 'docker-compose up -d' as initial building process at the project folder
-use 'docker-compose exec webgme bash' to start working on your localhost:8888

##Modeling
By creating a new instance of PNet, the user will have access to the places, including the initial and the end, and the transactions. Users could drag them and make any type of Petri net as they want. Note that the connections between the places and the transactions, the arcs, are strictly limited that it can not connect any two places or transactions directly.

##Features
By selecting the model the user just created, the user could select the toolbar on the top left and use the Plugin called TypeCheck. It will classify the type of Petri net of the created model, and return the result as notification.