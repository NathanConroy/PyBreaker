# PyBreaker
A Python Circuit Breaker for Your Project

## What Is a Circuit Breaker in Software?
A circuit breaker is a means to protect your system from its subsystems. For instance, if your refrigerator draws too much current, it's a fire risk to your home. In this case, a good cicuit breaker will enter an "open" state and shut off electical flow between your house and the refrigerator - preventing disaster. Once the problem is addressed and normal electrical flow may resume, the circuit breaker is reset to a "closed" state and the house again supplies the refrigerator with power.

A circuit breaker in software works much the same way. Borrowing from electrical terminology, circuit breakers have "open" and "closed" states. A closed circuit breaker will allow "normal" communication between a system and its subsystem. An open circuit breaker will disconnect communication between the two systems.

For example, let's say we have an online restaurant menu. When someone visits to your website, we try to fetch the latest menu information. So the website first calls the backend for the menu. Then the backend calls the database for the menu. If all goes well, the database returns the menu to the backend, and the backend serves this menu to the web client.

But what if the database fails in some way, and the backend does not get information about the menu? The system might be programmed to tell the web client that the menu is currently unavailable. But this will disrupt business - as some customers will look for other restaurants whose menus are available. What we'd like to do instead is (a) when we detect that the database is unavailable we'd (b) still like to return some useful information to the customer - even if it the information is of degraded quality - such as a last sucessfully fetched menu. Then after some time we'd (c) like to check if that the database has returned to a healthy state and we can resume full optimal operations.

Here is where a circuit breaker is useful. With a circuit breaker we can define both how and when (a), (b) and (c) happen. For (a) we can configure the circuit breaker to open when we try calling the database 10 times and the call fails each time. For (b) we can configure the call to return a previously cached response when the circuit breaker is open. And for (c) we may configure the circuit breaker to allow a database call after, say, 10 minutes. If the call succeeds, the circuit breaker returns to the closed state. If it fails, it retries in 10 minutes again.

## How to use PyBreaker

To be written ...
